import numpy as np
from math import pi

from pyomo.environ import (
    ConcreteModel, Var, NonNegativeReals, Reals, Objective, Constraint,
    RangeSet, minimize, SolverFactory
)

from pyomo.environ import NonNegativeReals


# -------------------------------
# 1. 기본 파라미터 설정
# -------------------------------
N = 1000          # 타임슬라이스 개수
v_max = 5.0       # (예시) 최대 속도
a_max = 2.0       # (예시) 최대 가속도(등방 가정)
a_centripetal_max = 2.0  # (예시) 코너에서의 최대 횡가속도

r_var_min = 0.5   # r의 가능한 최소값 (문제에 맞게 조정 가능)
r_var_max = 2.0   # r의 가능한 최대값

# 5x5 정사각형 + 모서리 r=1 원호(90도)일 때의 둘레 길이
# 일반적으로 5×5 정사각형에 4개의 90도 원호(r=1)를 덧붙이면
# 직선 구간 길이 = (5 - 2*r)*4,    원호 구간 길이 = (π/2)*4 * r = 2π*r
# 여기선 r=1로 가정하면 => 직선 3*4=12 + 원호 2π=6.283... => 총 약 18.283.
# r이 변수인 경우엔 아래처럼 계산해야 함:
def perimeter_of_fillet_square(side=5.0, r=1.0):
    # 4 * (side - 2*r) + 2*pi*r
    return 4*(side - 2*r) + 2*pi*r

# -------------------------------
# 2. Pyomo 모델 생성
# -------------------------------
model = ConcreteModel(name="RoundedSquarePath")

# -------------------------------
# 3. 변수 정의
# -------------------------------
# 전체 소요시간 T
model.T = Var(domain=NonNegativeReals, bounds=(0, None), initialize=10.0)

# 코너 필렛 반지름 r (문제에서 r도 변수라고 했으므로)
model.r = Var(domain=NonNegativeReals, bounds=(r_var_min, r_var_max), initialize=1.0)

# 이산 시점 i = 0..N
model.i = RangeSet(0, N)

# s[i]: 경로 위 아크길이 좌표 (0 <= s[i] <= L)
# 여기서 L은 r이 결정되어야 알 수 있으므로,
# s[i]의 upper bound는 나중에 동적으로 걸거나, 혹은 크게 잡은 뒤 별도 제약으로 묶음.
model.s = Var(model.i, domain=NonNegativeReals, initialize=0.0)

# v[i]: 각 시점에서의 (스칼라) 속도
model.v = Var(model.i, domain=NonNegativeReals, bounds=(0, v_max), initialize=0.0)

# a[i]: 각 시점에서의 (스칼라) 가속도 (음수도 가능하게 하려면 Reals)
model.a = Var(model.i, domain=Reals, bounds=(-a_max, a_max), initialize=0.0)

# -------------------------------
# 4. 보조식 및 경로 곡률
# -------------------------------
# s[i]에 따른 (x[i], y[i])가 실제 2D 경로 상에 있어야 하나,
# 여기서는 "s->(x,y)" 변환 대신,
# 곡률 k(s)와 perimeter L = perimeter_of_fillet_square(5, r)를 사용.
# 곡률: 직선 구간 => 0, 코너(90도 원호) => 1/r
# 실제로는 구간별 piecewise function이 필요합니다.

def curvature_function(s, side=5.0):
    """
    예시) s가 어떤 구간에 있는지에 따라
    곡률 0 또는 1/r (코너 구간) 반환.
    실제 문제에서는 s구간 나눠서 정확히 정의해야 함.
    """
    # 여기서는 단순히
    #  - 4개 코너 구간을 각 (π/2 * r) 길이로 보고,
    #  - 그 이외 구간은 직선으로 처리.
    # ex) 코너 하나의 길이는 (π/2)*r
    #     직선 하나의 길이는 (side - 2r)
    #
    # 이 예시는 매우 단순화된 샘플임.
    return 0.0  # (실제로는 piecewise 로직으로 구분)

# -------------------------------
# 5. 시간간격(Δt) 관련 제약
# -------------------------------
# Δt = T / N
# 편의상 파이썬 쪽에서 Δt를 빼서 식에 넣기보다는,
# Pyomo 안에서 T, N, v, s 등을 연결하는 식으로 구성.

def s_relation_rule(model, i):
    """s[i+1] = s[i] + 0.5*(v[i] + v[i+1]) * (T/N)"""
    if i == N:
        return model.s[i] == model.s[i]  # 마지막은 skip(또는 wrap)
    return model.s[i+1] == model.s[i] + 0.5 * (model.v[i] + model.v[i+1]) * (model.T / N)

model.s_relation = Constraint(model.i, rule=s_relation_rule)

def v_relation_rule(model, i):
    """v[i+1] = v[i] + 0.5*(a[i] + a[i+1]) * (T/N)"""
    if i == N:
        return model.v[i] == model.v[i]  # 마지막은 skip(또는 wrap)
    return model.v[i+1] == model.v[i] + 0.5 * (model.a[i] + model.a[i+1]) * (model.T / N)

model.v_relation = Constraint(model.i, rule=v_relation_rule)

# -------------------------------
# 6. 곡률에 따른 횡가속도 제약
# -------------------------------
def centripetal_rule(model, i):
    """
    v[i]^2 * k(s[i]) <= a_centripetal_max
    """
    # s[i]에 따른 곡률 k(s[i])를 함수로부터 얻는다
    # (단, r 또한 변수이므로 실제로는 s[i], r 모두를 고려해 piecewise해야 함)
    # 여기서는 예시로 간단히:
    k_i = curvature_function(model.s[i])
    return (model.v[i]**2 * k_i) <= a_centripetal_max

model.centripetal_constraint = Constraint(model.i, rule=centripetal_rule)

# -------------------------------
# 7. s[i]의 범위 제약 (0 <= s[i] <= L)
# -------------------------------
def s_upper_bound_rule(model, i):
    """ s[i] <= 전체 둘레(L) """
    L = perimeter_of_fillet_square(5.0, model.r)
    return model.s[i] <= L

model.s_upper_bound = Constraint(model.i, rule=s_upper_bound_rule)

# -------------------------------
# 8. 시작점, 종료점 관련 제약
# -------------------------------
# 예) 시작점 s[0]는 "윗변 중앙" 근처로 두고 싶다면,
#    s[0] = 어떤 값 ~ 또 다른 값
# 여기서는 s[0]를 변수로 두되, [L/4 - δ, L/4 + δ] 등
# 적절 범위에 넣을 수도 있고, 원하는 구간으로 제약.
def start_point_rule(model):
    L = perimeter_of_fillet_square(5.0, model.r)
    # 예시: 윗변 중앙 근처 => 대략 s = 0 부근에 있다고 가정
    # (문제에 맞게 제약 범위 설정)
    return model.s[0] >= 0.0

model.start_point_constraint = Constraint(rule=start_point_rule)

# 예) 한 바퀴 돌아서 끝내려면 s[N] = s[0] + L
# 혹은 s[N] >= L 등등 문제 조건에 맞춰 조정
def end_point_rule(model):
    L = perimeter_of_fillet_square(5.0, model.r)
    return model.s[N] >= model.s[0] + L  # 한바퀴 이상 돌기

model.end_point_constraint = Constraint(rule=end_point_rule)

# 속도 초기 조건 (정지 상태에서 출발 etc.)
model.v[0].fix(0.0)
# 종료 시점 속도도 0으로 만들고 싶다면
# model.v[N].fix(0.0)

# -------------------------------
# 9. 목적함수: 총 시간 T 최소화
# -------------------------------
model.obj = Objective(expr=model.T, sense=minimize)

# -------------------------------
# 10. 솔버 설정 및 실행
# -------------------------------
solver = SolverFactory('ipopt')  # 예: ipopt 사용
result = solver.solve(model, tee=True)

# 해석 결과 출력
print("Status:", result.solver.status)
print("Termination condition:", result.solver.termination_condition)
print("Optimal T =", model.T.value)
print("Optimal r =", model.r.value)

# s[i], v[i] 등을 확인해볼 수 있음
s_vals = [model.s[i].value for i in range(N+1)]
v_vals = [model.v[i].value for i in range(N+1)]

print("s[0..N] =", s_vals)
print("v[0..N] =", v_vals)
