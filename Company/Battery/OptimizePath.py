import numpy as np
from scipy.optimize import minimize
import math
import time

# --- 기본 설정 ---
# 경로 설정
L = 5.0  # 사각형 가로 길이 (x축 방향)
W = 5.0  # 사각형 세로 길이 (y축 방향) - 정사각형이므로 L과 동일
r = 1.0  # 모서리 원호 반지름
N = 1000  # 타임 슬라이스 개수

# 물리 제약 조건
a_max = 2.0  # 최대 가속도 (m/s^2)
d_max = 3.0  # 최대 감속도 (m/s^2) - 양수 값으로 정의
v_max = 5.0  # 최대 속도 (m/s)

# 시작점 설정 (0~1 사이 값, 첫 번째 직선 구간의 시작점을 0, 끝점을 1로 가정)
# 예: 0.5는 첫 번째 직선 구간의 중간
start_fraction = 0.0  # 첫번째 직선 구간 시작 직후 (원호 직후)
# start_fraction = 0.5 # 첫번째 직선 구간 중간

# --- 경로 계산 ---
straight_len_x = L - 2 * r
straight_len_y = W - 2 * r
curve_len = 0.5 * np.pi * r  # 90도 원호 길이

# 경로 세그먼트 길이 정의 (시작: 첫 직선 구간 시작 직후)
segment_lengths = [
    straight_len_x, curve_len,  # 1번 직선 (오른쪽), 1번 코너
    straight_len_y, curve_len,  # 2번 직선 (위쪽),   2번 코너
    straight_len_x, curve_len,  # 3번 직선 (왼쪽),   3번 코너
    straight_len_y, curve_len  # 4번 직선 (아래쪽), 4번 코너
]

# 누적 경로 길이 계산
segment_cumulative_lengths = np.cumsum([0] + segment_lengths)
S_total = segment_cumulative_lengths[-1]  # 총 경로 길이

# 실제 시작 위치 (s 좌표) 계산
# 첫 번째 직선 구간의 시작 s 좌표는 0, 끝 s 좌표는 straight_len_x
s_start_offset = straight_len_x * start_fraction
actual_s_start = s_start_offset  # 경로 파라미터 s는 0부터 시작한다고 가정하고, 최적화 후 결과를 이동

print(f"--- 경로 정보 ---")
print(f"사각형 크기: {L} x {W}")
print(f"모서리 반지름: {r}")
print(f"직선 구간 길이 (X): {straight_len_x:.4f}")
print(f"직선 구간 길이 (Y): {straight_len_y:.4f}")
print(f"원호 구간 길이: {curve_len:.4f}")
print(f"총 경로 길이: {S_total:.4f}")
print(f"지정된 시작점 (첫 직선구간 분율): {start_fraction}")
print(f"계산된 시작 s 좌표 오프셋: {s_start_offset:.4f}")
print(f"총 타임 슬라이스: {N}")
print("-" * 20)
print(f"--- 제약 조건 ---")
print(f"최대 가속도: {a_max} m/s^2")
print(f"최대 감속도: {d_max} m/s^2")
print(f"최대 속도: {v_max} m/s")
print("-" * 20)


# --- 경로 상 위치(s)에 따른 상태 반환 함수 ---
def get_segment_type(s_pos):
    """ 주어진 경로상 위치 s_pos가 직선인지 곡선인지 판별 """
    s_mod = s_pos % S_total  # 한 바퀴 내 위치로 변환
    for i in range(len(segment_cumulative_lengths) - 1):
        if segment_cumulative_lengths[i] <= s_mod < segment_cumulative_lengths[i + 1]:
            # segment_lengths 인덱스는 i와 동일
            # 짝수 인덱스(0, 2, 4, 6)는 직선, 홀수 인덱스(1, 3, 5, 7)는 곡선
            return "straight" if i % 2 == 0 else "curve"
    return "straight"  # 마지막 지점 처리 (다음 루프의 시작과 동일)


# --- 최적화 문제 정의 ---

# 변수: x = [T, v_0, v_1, ..., v_{N-1}] -> 총 N+1 개의 변수
# T: 총 시간
# v_i: i번째 타임 슬라이스 *시작* 시점의 순간 속도 (v_N은 사용되지 않음)

# 목적 함수: 총 시간 T 최소화
def objective(x):
    T = x[0]
    return T


# 제약 조건 함수
def constraints(x):
    T = x[0]
    v = x[1:]  # v_0, v_1, ..., v_{N-1} (크기 N)

    if T <= 1e-6:  # T가 너무 작아지는 것을 방지 (수치적 안정성)
        return [np.inf] * (3 * N + 1)  # 제약조건 위반으로 처리

    dt = T / N  # 각 타임슬라이스의 시간 간격

    # 위치 계산 (s_0 = 0 부터 시작)
    s = np.zeros(N + 1)
    for i in range(N):
        # 오일러 1차 적분: s_{i+1} = s_i + v_i * dt
        s[i + 1] = s[i] + v[i] * dt

    # 가속도 계산 a_i = (v_{i+1} - v_i) / dt
    # v 배열 크기는 N, 따라서 마지막 속도 v_N이 필요.
    # 주기적 경계 조건 가정: v_N = v_0
    v_extended = np.append(v, v[0])  # v_0, v_1, ..., v_{N-1}, v_0
    a = np.diff(v_extended) / dt  # a_0, a_1, ..., a_{N-1} (크기 N)

    # 제약 조건 리스트 생성
    cons = []

    # 1. 총 이동 거리 제약 (Equality): s_N = S_total
    # s[N] = sum(v[i] * dt for i in 0..N-1)
    cons.append({'type': 'eq', 'fun': lambda x: np.sum(x[1:] * (x[0] / N)) - S_total})

    # 2. 속도 제약 (Inequality): 0 <= v_i <= v_max
    # scipy는 >= 0 형태를 사용
    for i in range(N):
        cons.append({'type': 'ineq', 'fun': lambda x, i=i: x[i + 1]})  # v_i >= 0
        cons.append({'type': 'ineq', 'fun': lambda x, i=i: v_max - x[i + 1]})  # v_max - v_i >= 0

    # 3. 가속도/감속도 제약 (Inequality): -d_max <= a_i <= a_max
    # 가속도: a_max - a_i >= 0
    # 감속도: a_i - (-d_max) >= 0 => a_i + d_max >= 0
    # 주의: a 계산 시 x[0](T)가 분모에 들어가므로 lambda 함수 내에서 재계산 필요
    for i in range(N):
        # a_i = (v_{i+1} - v_i) / dt = (v_{i+1} - v_i) * N / T
        def accel_constraint_upper(x, i=i):
            T_local = x[0]
            if T_local <= 1e-6: return -np.inf  # 제약 위반
            dt_local = T_local / N
            v_local = x[1:]
            v_next = v_local[(i + 1) % N]  # 주기적 경계 조건 v_N = v_0
            v_curr = v_local[i]
            a_local = (v_next - v_curr) / dt_local
            return a_max - a_local

        def accel_constraint_lower(x, i=i):
            T_local = x[0]
            if T_local <= 1e-6: return -np.inf  # 제약 위반
            dt_local = T_local / N
            v_local = x[1:]
            v_next = v_local[(i + 1) % N]  # 주기적 경계 조건 v_N = v_0
            v_curr = v_local[i]
            a_local = (v_next - v_curr) / dt_local
            return a_local + d_max

        cons.append({'type': 'ineq', 'fun': accel_constraint_upper})
        cons.append({'type': 'ineq', 'fun': accel_constraint_lower})

    # 4. 곡선 구간 속도 제약 (Inequality): v_i <= sqrt(r * a_max) (단순화된 제약)
    # 원심 가속도 a_c = v^2 / r <= a_max (가용 가속도를 모두 원심력에 사용한다고 가정)
    # -> v <= sqrt(r * a_max)
    v_max_curve = np.sqrt(r * a_max)

    # 실제로는 ( tangential_accel^2 + centripetal_accel^2 ) <= a_max^2 이지만,
    # 여기서는 간단하게 곡선 구간 전체에 대해 속도 상한을 적용합니다.
    # s 값 계산이 x에 의존하므로 lambda 함수 내에서 처리 필요.
    def curve_speed_constraint(x, i=i):
        T_local = x[0]
        if T_local <= 1e-6: return -np.inf  # 제약 위반
        dt_local = T_local / N
        v_local = x[1:]

        # 해당 시점 i의 경로상 위치 s_i 계산
        s_i = np.sum(v_local[:i] * dt_local)  # s_0=0 기준

        if get_segment_type(s_i) == "curve":
            # 곡선 구간이면 제약 적용: v_max_curve - v_i >= 0
            return v_max_curve - v_local[i]
        else:
            # 직선 구간이면 제약 없음 (항상 양수 반환하여 통과)
            return 1.0  # 값은 중요하지 않음, 양수이기만 하면 됨

    for i in range(N):
        cons.append({'type': 'ineq', 'fun': curve_speed_constraint})

    # 제약 조건 값 계산 (디버깅용, 실제 minimize에는 dict 리스트만 전달)
    # evaluated_cons = []
    # for c in cons:
    #     if c['type'] == 'eq':
    #         evaluated_cons.append(c['fun'](x))
    #     elif c['type'] == 'ineq':
    #         evaluated_cons.append(c['fun'](x))
    # print(f"T={T:.4f}, s_N={s[N]:.4f}")
    # print(f"Min/Max v: {np.min(v):.4f}/{np.max(v):.4f}")
    # print(f"Min/Max a: {np.min(a):.4f}/{np.max(a):.4f}")

    return cons  # 제약조건 딕셔너리 리스트 반환


# --- 최적화 실행 ---

# 초기 추정값 (Initial Guess)
# T_guess: 대략적인 시간 (예: 총 거리를 평균 속도로 나눈 값)
v_avg_guess = v_max / 2
T_guess = S_total / v_avg_guess
# v_guess: 초기 속도 프로파일 (예: 모든 슬라이스에서 평균 속도)
v_guess = np.full(N, v_avg_guess)

x0 = np.concatenate(([T_guess], v_guess))

# 변수 경계 (Bounds)
# T > 0 (약간의 여유 포함)
# 0 <= v_i <= v_max
bounds = [(1e-3, None)] + [(0, v_max)] * N

print("최적화를 시작합니다... (시간이 다소 걸릴 수 있습니다)")
start_time = time.time()

# 최적화 수행 (SLSQP: Sequential Least Squares Programming)
# 이 방법은 등식 및 부등식 제약 조건이 있는 비선형 문제에 적합합니다.
result = minimize(objective, x0, method='SLSQP', bounds=bounds, constraints=constraints,
                  options={'disp': True, 'maxiter': 50000, 'ftol': 1e-7})  # maxiter 증가

end_time = time.time()
print(f"최적화 완료. 소요 시간: {end_time - start_time:.2f} 초")

# --- 결과 처리 및 출력 ---
if result.success:
    print("\n최적화 성공!")
    optimized_T = result.x[0]
    optimized_v = result.x[1:]  # v_0, ..., v_{N-1}

    print(f"최소 이동 시간 (T): {optimized_T:.4f} 초")

    # 최적화된 결과로 상세 정보 계산
    dt_opt = optimized_T / N
    t_opt = np.linspace(0, optimized_T, N + 1)  # 시간 배열 (0부터 T까지 N+1개 점)

    # 위치 (s) 계산
    s_opt = np.zeros(N + 1)
    for i in range(N):
        s_opt[i + 1] = s_opt[i] + optimized_v[i] * dt_opt

    # 실제 시작점(s_start_offset) 기준으로 s값 조정
    # (예: s_start_offset 만큼 모든 s값을 더하고 S_total로 모듈러 연산)
    s_opt_shifted = (s_opt + s_start_offset) % S_total

    # 속도 (v) - 결과 v는 각 슬라이스 시작 시점 속도. v_N = v_0 가정.
    v_opt = np.append(optimized_v, optimized_v[0])  # v_0, ..., v_{N-1}, v_0 (크기 N+1)

    # 가속도 (a) 계산
    a_opt = np.diff(v_opt) / dt_opt  # a_0, ..., a_{N-1} (크기 N)
    # 마지막 슬라이스 직전의 가속도와 동일하다고 가정하여 크기 맞춤
    a_opt = np.append(a_opt, a_opt[-1])  # 크기 N+1

    # 결과 저장 (N+1개의 타임스탬프에 대해)
    # 각 t_opt[i] 에서의 (위치, 속도, 가속도)
    trajectory_data = {
        'time': t_opt,
        'position_s': s_opt_shifted,  # 조정된 s 경로 좌표
        'velocity': v_opt,
        'acceleration': a_opt
    }

    print(f"타임 슬라이스 개수: {N}")
    print(f"계산된 dt: {dt_opt:.6f} 초")
    print(f"최종 위치 s[{N}]: {s_opt[N]:.4f} (목표: {S_total:.4f})")
    print(f"최소/최대 속도: {np.min(v_opt):.4f} / {np.max(v_opt):.4f} m/s")
    print(f"최소/최대 가속도: {np.min(a_opt):.4f} / {np.max(a_opt):.4f} m/s^2")

    # # (선택) 처음 몇 개의 데이터 포인트 출력
    # print("\n--- 궤적 데이터 (처음 5개) ---")
    # print("  Time (s) | Position s (m) | Velocity (m/s) | Acceleration (m/s^2)")
    # for i in range(min(5, N + 1)):
    #     print(f"{trajectory_data['time'][i]:10.4f} | {trajectory_data['position_s'][i]:14.4f} | {trajectory_data['velocity'][i]:14.4f} | {trajectory_data['acceleration'][i]:19.4f}")

    # # (선택) 데이터 시각화 (matplotlib 필요)
    # try:
    #     import matplotlib.pyplot as plt
    #     fig, axs = plt.subplots(3, 1, figsize=(10, 10), sharex=True)
    #     axs[0].plot(trajectory_data['time'], trajectory_data['position_s'], label='Position (s)')
    #     axs[0].set_ylabel('Position s (m)')
    #     axs[0].grid(True)
    #     axs[0].legend()
    #
    #     axs[1].plot(trajectory_data['time'], trajectory_data['velocity'], label='Velocity')
    #     axs[1].axhline(v_max, color='r', linestyle='--', label=f'v_max ({v_max})')
    #     # 곡선 구간 속도 제한 표시 (어디가 곡선인지 알아야 함)
    #     curve_limit_indices = [i for i, s_val in enumerate(s_opt_shifted) if get_segment_type(s_val) == 'curve']
    #     if curve_limit_indices:
    #         axs[1].plot(trajectory_data['time'][curve_limit_indices], np.full(len(curve_limit_indices), np.sqrt(r * a_max)),
    #                     'g.', markersize=2, label=f'v_curve_limit ({np.sqrt(r * a_max):.2f})')
    #
    #     axs[1].set_ylabel('Velocity (m/s)')
    #     axs[1].grid(True)
    #     axs[1].legend()
    #
    #     axs[2].plot(trajectory_data['time'][:-1], trajectory_data['acceleration'][:-1], label='Acceleration') # 마지막 가속도는 추정값이므로 제외하고 표시
    #     axs[2].axhline(a_max, color='r', linestyle='--', label=f'a_max ({a_max})')
    #     axs[2].axhline(-d_max, color='m', linestyle='--', label=f'-d_max ({-d_max})')
    #     axs[2].set_xlabel('Time (s)')
    #     axs[2].set_ylabel('Acceleration (m/s^2)')
    #     axs[2].grid(True)
    #     axs[2].legend()
    #
    #     plt.suptitle('Optimized Trajectory along Rounded Rectangle Path')
    #     plt.tight_layout(rect=[0, 0.03, 1, 0.97])
    #     plt.show()
    #
    # except ImportError:
    #     print("\nmatplotlib이 설치되지 않아 그래프를 표시할 수 없습니다.")
    #     print("pip install matplotlib 를 실행하여 설치할 수 있습니다.")

else:
    print("\n최적화 실패:")
    print(result.message)

# trajectory_data 딕셔너리에 최적화된 시간, 위치(s), 속도, 가속도 데이터가 저장되어 있습니다.
# 각 배열은 N+1개의 요소를 가집니다 (시간 t=0 부터 t=T 까지).
# 가속도 배열은 마지막 요소가 그 직전 요소와 동일하게 채워져 있습니다.
