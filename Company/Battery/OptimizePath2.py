import casadi as ca
import numpy as np
import matplotlib.pyplot as plt

# --- Parameters ---
N = 1000  # Number of time slices
L_x = 5.0  # Rectangle width
L_y = 5.0  # Rectangle height
r = 1.0  # Corner radius

a_max = 2.0  # Maximum acceleration magnitude (m/s^2) - Assuming symmetric for accel/decel
v_max = 3.0  # Maximum speed (m/s)

# Path Definition (Centerline, centered at origin)
hx = L_x / 2.0
hy = L_y / 2.0
path_segments = []

# 1. Top Straight Segment
path_segments.append({'type': 'line', 'x1': -hx + r, 'y1': hy, 'x2': hx - r, 'y2': hy})
# 2. Top-Right Arc
path_segments.append({'type': 'arc', 'cx': hx - r, 'cy': hy - r, 'r': r, 'start_angle': np.pi / 2, 'end_angle': 0})
# 3. Right Straight Segment
path_segments.append({'type': 'line', 'x1': hx, 'y1': hy - r, 'x2': hx, 'y2': -hy + r})
# 4. Bottom-Right Arc
path_segments.append({'type': 'arc', 'cx': hx - r, 'cy': -hy + r, 'r': r, 'start_angle': 0, 'end_angle': -np.pi / 2})
# 5. Bottom Straight Segment
path_segments.append({'type': 'line', 'x1': hx - r, 'y1': -hy, 'x2': -hx + r, 'y2': -hy})
# 6. Bottom-Left Arc
path_segments.append(
    {'type': 'arc', 'cx': -hx + r, 'cy': -hy + r, 'r': r, 'start_angle': -np.pi / 2, 'end_angle': -np.pi})
# 7. Left Straight Segment
path_segments.append({'type': 'line', 'x1': -hx, 'y1': -hy + r, 'x2': -hx, 'y2': hy - r})
# 8. Top-Left Arc
path_segments.append({'type': 'arc', 'cx': -hx + r, 'cy': hy - r, 'r': r, 'start_angle': -np.pi,
                      'end_angle': -3 * np.pi / 2})  # or start pi, end pi/2

# Start Point Selection
# Options: 'top', 'right', 'bottom', 'left'
start_segment_center = 'top'  # User can change this

if start_segment_center == 'top':
    start_x, start_y = 0.0, hy
elif start_segment_center == 'right':
    start_x, start_y = hx, 0.0
elif start_segment_center == 'bottom':
    start_x, start_y = 0.0, -hy
elif start_segment_center == 'left':
    start_x, start_y = -hx, 0.0
else:
    raise ValueError("Invalid start_segment_center. Choose 'top', 'right', 'bottom', or 'left'.")

# --- Optimization Setup using CasADi ---
opti = ca.Opti()

# Decision Variables
# State variables (position and velocity at each node k)
px = opti.variable(N + 1)
py = opti.variable(N + 1)
vx = opti.variable(N + 1)
vy = opti.variable(N + 1)

# Control variables (acceleration at each interval k)
ax = opti.variable(N)
ay = opti.variable(N)

# Total time (scalar variable to minimize)
T_total = opti.variable()

# --- Objective Function ---
opti.minimize(T_total)

# --- Constraints ---
dt = T_total / N  # Time step duration

# Dynamics constraints (Trapezoidal Collocation/Integration)
for k in range(N):
    px_next = px[k] + (vx[k] + vx[k + 1]) * dt / 2.0
    py_next = py[k] + (vy[k] + vy[k + 1]) * dt / 2.0
    vx_next = vx[k] + ax[k] * dt
    vy_next = vy[k] + ay[k] * dt
    opti.subject_to(px[k + 1] == px_next)
    opti.subject_to(py[k + 1] == py_next)
    opti.subject_to(vx[k + 1] == vx_next)
    opti.subject_to(vy[k + 1] == vy_next)

# Control constraints (Acceleration limits)
for k in range(N):
    opti.subject_to(ax[k] ** 2 + ay[k] ** 2 <= a_max ** 2)
    # If deceleration limit d_max is different, add:
    # vel_sq = vx[k]**2 + vy[k]**2
    # projection = (ax[k]*vx[k] + ay[k]*vy[k])
    # opti.subject_to( ca.if_else(vel_sq > 1e-6, projection >= -d_max * ca.sqrt(vel_sq), 1) ) # Avoid division by zero

# State constraints (Velocity limits)
for k in range(N + 1):
    opti.subject_to(vx[k] ** 2 + vy[k] ** 2 <= v_max ** 2)


# Path constraints (Stay close to the path centerline)
# Define helper functions for distance calculations using CasADi symbols
def distance_point_line_segment_sq(px, py, x1, y1, x2, y2):
    # Squared distance from point (px, py) to line segment (x1,y1)-(x2,y2)
    dx = x2 - x1
    dy = y2 - y1
    if dx == 0 and dy == 0:  # Segment is a point
        return (px - x1) ** 2 + (py - y1) ** 2

    # Projection parameter t = dot(P-A, B-A) / |B-A|^2
    # Clamped to [0, 1] for segment
    t = ((px - x1) * dx + (py - y1) * dy) / (dx ** 2 + dy ** 2)
    t_clamped = ca.fmax(0, ca.fmin(1, t))

    # Closest point on the infinite line
    closest_x_line = x1 + t * dx
    closest_y_line = y1 + t * dy

    # Closest point on the segment
    closest_x = x1 + t_clamped * dx
    closest_y = y1 + t_clamped * dy

    # Squared distance
    dist_sq = (px - closest_x) ** 2 + (py - closest_y) ** 2
    return dist_sq


def distance_point_arc_sq(px, py, cx, cy, r, start_angle, end_angle):
    # Ensure angles are in [0, 2pi] or [-pi, pi] consistently if needed
    # This simplified version assumes angles are comparable

    # Vector from center to point
    vec_x = px - cx
    vec_y = py - cy
    dist_from_center_sq = vec_x ** 2 + vec_y ** 2

    # Angle of the point relative to the center
    point_angle = ca.atan2(vec_y, vec_x)

    # Normalize angles if necessary (e.g., to [0, 2pi])
    # start_angle_norm = ca.fmod(start_angle + 2*np.pi, 2*np.pi)
    # end_angle_norm = ca.fmod(end_angle + 2*np.pi, 2*np.pi)
    # point_angle_norm = ca.fmod(point_angle + 2*np.pi, 2*np.pi)

    # Check if the angle is within the arc's range (handle wrap around carefully)
    # This logic is simplified and might need adjustment depending on angle conventions
    on_arc = 0  # Placeholder - complex to do robustly in CasADi without defining angle ranges carefully
    # A robust way often involves checking cross/dot products with start/end vectors

    # Closest point on the circle
    dist_from_center = ca.sqrt(dist_from_center_sq + 1e-9)  # Add epsilon for stability
    closest_on_circle_x = cx + r * vec_x / dist_from_center
    closest_on_circle_y = cy + r * vec_y / dist_from_center

    # For simplicity here, we calculate distance to the infinite circle.
    # A more rigorous approach projects onto the arc segment boundaries if outside angular range.
    dist_sq = (px - closest_on_circle_x) ** 2 + (py - closest_on_circle_y) ** 2

    # Ideally, you'd only return this distance if the closest point on the circle
    # actually falls within the angular range of the arc segment. Otherwise,
    # the distance should be to the closest endpoint of the arc.
    # Implementing this robustly with symbolic variables is complex.
    # As a fallback, we use the distance to the infinite circle, which acts
    # as a strong incentive to be near the arc.
    return dist_sq


# Apply path constraint for each point (using squared distance for smoother gradients)
# We calculate the minimum squared distance to *any* segment and constrain it.
path_constraint_tolerance_sq = (0.05) ** 2  # Allow small deviation (squared)

for k in range(N + 1):  # Apply to all points including start/end
    min_dist_sq = ca.inf  # Initialize with infinity

    for seg in path_segments:
        dist_sq_current = ca.inf
        if seg['type'] == 'line':
            dist_sq_current = distance_point_line_segment_sq(px[k], py[k], seg['x1'], seg['y1'], seg['x2'], seg['y2'])
        elif seg['type'] == 'arc':
            # Using the simplified distance_point_arc_sq for now
            dist_sq_current = distance_point_arc_sq(px[k], py[k], seg['cx'], seg['cy'], seg['r'], seg['start_angle'],
                                                    seg['end_angle'])

        min_dist_sq = ca.fmin(min_dist_sq, dist_sq_current)

    # Constraint: minimum squared distance must be less than tolerance squared
    opti.subject_to(min_dist_sq <= path_constraint_tolerance_sq)

# Boundary conditions
opti.subject_to(px[0] == start_x)
opti.subject_to(py[0] == start_y)
opti.subject_to(vx[0] == 0)
opti.subject_to(vy[0] == 0)

opti.subject_to(px[N] == start_x)  # Return to start position
opti.subject_to(py[N] == start_y)
opti.subject_to(vx[N] == 0)  # End with zero velocity
opti.subject_to(vy[N] == 0)

# Lower bound for time (must be positive)
opti.subject_to(T_total >= 1e-2)

# --- Initial Guesses ---
# Simple guess: Constant speed along a simplified path, estimate time
path_length_approx = 2 * (L_x - 2 * r) + 2 * (L_y - 2 * r) + 2 * np.pi * r  # Approx length
T_guess = path_length_approx / (0.5 * v_max)  # Guess time based on average speed
opti.set_initial(T_total, T_guess)

# Guess states linearly interpolating start/end (crude)
opti.set_initial(px, np.linspace(start_x, start_x, N + 1))  # Keep X constant initially
opti.set_initial(py, np.linspace(start_y, start_y, N + 1))  # Keep Y constant initially
opti.set_initial(vx, np.zeros(N + 1))
opti.set_initial(vy, np.zeros(N + 1))
opti.set_initial(ax, np.zeros(N))
opti.set_initial(ay, np.zeros(N))
# Better guesses would follow the path shape roughly

# --- Solve ---
# Use IPOPT solver
opti.solver('ipopt')  # Good general-purpose NLP solver

try:
    sol = opti.solve()
    print("Optimization successful!")

    # --- Extract Results ---
    T_final = sol.value(T_total)
    px_opt = sol.value(px)
    py_opt = sol.value(py)
    vx_opt = sol.value(vx)
    vy_opt = sol.value(vy)
    ax_opt = sol.value(ax)
    ay_opt = sol.value(ay)

    # Calculate derived values
    dt_final = T_final / N
    time_points = np.linspace(0, T_final, N + 1)
    speed_opt = np.sqrt(vx_opt ** 2 + vy_opt ** 2)
    accel_magnitude_opt = np.sqrt(ax_opt ** 2 + ay_opt ** 2)  # Magnitude for N intervals

    print(f"Minimum Time: {T_final:.4f} seconds")

    # Store results (optional, e.g., in a dictionary or pandas DataFrame)
    results = {
        "time": time_points,
        "px": px_opt,
        "py": py_opt,
        "vx": vx_opt,
        "vy": vy_opt,
        "speed": speed_opt,
        # Note: acceleration is for intervals 0 to N-1
        "ax": np.append(ax_opt, np.nan),  # Append NaN for length consistency
        "ay": np.append(ay_opt, np.nan),
        "accel_mag": np.append(accel_magnitude_opt, np.nan),
        "dt": dt_final,
        "T_total": T_final
    }

    # --- Plotting ---
    plt.figure(figsize=(12, 10))

    # Path and Trajectory
    plt.subplot(2, 2, 1)
    # Plot reference path
    theta = np.linspace(0, 2 * np.pi, 200)
    plt.plot(hx - r + r * np.cos(theta), hy - r + r * np.sin(theta), 'k--', linewidth=1, label='Corner Guides')
    plt.plot(-hx + r + r * np.cos(theta), hy - r + r * np.sin(theta), 'k--', linewidth=1)
    plt.plot(hx - r + r * np.cos(theta), -hy + r + r * np.sin(theta), 'k--', linewidth=1)
    plt.plot(-hx + r + r * np.cos(theta), -hy + r + r * np.sin(theta), 'k--', linewidth=1)
    plt.plot([-hx + r, hx - r], [hy, hy], 'g-', label='Path Centerline')  # Top
    plt.plot([hx, hx], [hy - r, -hy + r], 'g-')  # Right
    plt.plot([hx - r, -hx + r], [-hy, -hy], 'g-')  # Bottom
    plt.plot([-hx, -hx], [-hy + r, hy - r], 'g-')  # Left
    # Plot optimized trajectory
    plt.plot(px_opt, py_opt, 'b-', label='Optimized Trajectory')
    plt.scatter([start_x], [start_y], color='red', zorder=5, label='Start/End')
    plt.title('Path vs Optimized Trajectory')
    plt.xlabel('X position (m)')
    plt.ylabel('Y position (m)')
    plt.axis('equal')
    plt.grid(True)
    plt.legend()

    # Speed Profile
    plt.subplot(2, 2, 2)
    plt.plot(time_points, speed_opt, label='Speed')
    plt.axhline(v_max, color='r', linestyle='--', label='v_max')
    plt.title('Speed Profile')
    plt.xlabel('Time (s)')
    plt.ylabel('Speed (m/s)')
    plt.grid(True)
    plt.legend()
    plt.ylim(bottom=-0.1)

    # Acceleration Profile (Magnitude)
    plt.subplot(2, 2, 3)
    # Plot acceleration magnitude over the intervals
    plt.plot(time_points[:-1], accel_magnitude_opt, label='Acceleration Magnitude', drawstyle='steps-post')
    plt.axhline(a_max, color='r', linestyle='--', label='a_max')
    plt.title('Acceleration Magnitude')
    plt.xlabel('Time (s)')
    plt.ylabel('Acceleration (m/s^2)')
    plt.grid(True)
    plt.legend()
    plt.ylim(bottom=-0.1)

    # Acceleration Components (ax, ay)
    plt.subplot(2, 2, 4)
    plt.plot(time_points[:-1], ax_opt, label='ax', drawstyle='steps-post')
    plt.plot(time_points[:-1], ay_opt, label='ay', drawstyle='steps-post')
    # plt.axhline(a_max, color='r', linestyle='--', label='a_max')
    # plt.axhline(-a_max, color='r', linestyle='--')
    plt.title('Acceleration Components')
    plt.xlabel('Time (s)')
    plt.ylabel('Acceleration (m/s^2)')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()

except RuntimeError as e:
    print(f"Optimization failed: {e}")
    # You might want to inspect opti.debug.value(variable) for failed solution
    print("\nTrying to access debug values (might not be feasible if solver crashed early):")
    try:
        T_fail = opti.debug.value(T_total)
        px_fail = opti.debug.value(px)
        py_fail = opti.debug.value(py)
        print(f"Failed T: {T_fail}")

        # Plot failure state if desired
        plt.figure()
        plt.plot(px_fail, py_fail, 'r-x', label='Failed Trajectory')
        # Plot reference path again
        theta = np.linspace(0, 2 * np.pi, 200)
        plt.plot(hx - r + r * np.cos(theta), hy - r + r * np.sin(theta), 'k--', linewidth=1, label='Corner Guides')
        plt.plot(-hx + r + r * np.cos(theta), hy - r + r * np.sin(theta), 'k--', linewidth=1)
        plt.plot(hx - r + r * np.cos(theta), -hy + r + r * np.sin(theta), 'k--', linewidth=1)
        plt.plot(-hx + r + r * np.cos(theta), -hy + r + r * np.sin(theta), 'k--', linewidth=1)
        plt.plot([-hx + r, hx - r], [hy, hy], 'g-', label='Path Centerline')  # Top
        plt.plot([hx, hx], [hy - r, -hy + r], 'g-')  # Right
        plt.plot([hx - r, -hx + r], [-hy, -hy], 'g-')  # Bottom
        plt.plot([-hx, -hx], [-hy + r, hy - r], 'g-')  # Left
        plt.scatter([start_x], [start_y], color='red', zorder=5, label='Start/End')
        plt.title('Failed Trajectory Attempt')
        plt.xlabel('X position (m)')
        plt.ylabel('Y position (m)')
        plt.axis('equal')
        plt.grid(True)
        plt.legend()
        plt.show()

    except Exception as debug_e:
        print(f"Could not retrieve debug values: {debug_e}")