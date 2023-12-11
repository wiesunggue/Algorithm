# https://www.acmicpc.net/problem/1281

# simplex 구현 알고리즘
# 수리적인 이론만 보고 구현해서 비효율적일 가능성이 있음

# 1. simplex 알고리즘은 제약이 EQUALITY FORM으로 작성되어야 함
# equality form은 AX=B, X>=0 minimize F(X)로 이루어짐
# AX <= B와 CX = D의 꼴이 있다면 A'X'=B의 꼴로 제약식을 변경해야 함
# 현재 simplex 알고리즘의 문제점은 inv 연산 -> 근 찾기 과정에 의해서 해당 연산의 오버헤드가 매우 크다는 점
import sys
input = sys.stdin.readline
def swap_rows(matrix, i, j):
    matrix[i], matrix[j] = matrix[j].copy(), matrix[i].copy()


def inv(matrix):
    n = len(matrix)

    # 단위 행렬 생성
    identity = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]

    # 기존 행렬과 단위 행렬을 합침
    augmented_matrix = [row + identity_row for row, identity_row in zip(matrix, identity)]

    # 가우스-조던 소거법 수행
    for i in range(n):
        # 피벗이 0이 되지 않도록 조정
        if augmented_matrix[i][i] == 0.0:
            # 피벗이 0이면 행을 바꿔줌
            for k in range(i + 1, n):
                if augmented_matrix[k][i] != 0.0:
                    swap_rows(augmented_matrix, i, k)
                    break
            else:
                raise ValueError("Matrix is singular and doesn't have an inverse.")

        pivot = augmented_matrix[i][i]
        # 피벗을 1로 만듦
        for j in range(n * 2):
            augmented_matrix[i][j] /= pivot
        # 다른 행들을 0으로 만듦
        for k in range(n):
            if k != i:
                factor = augmented_matrix[k][i]
                for j in range(n * 2):
                    augmented_matrix[k][j] -= factor * augmented_matrix[i][j]

    # 역행렬 추출
    inverse_matrix = [row[n:] for row in augmented_matrix]

    return inverse_matrix

def matmul(A,B):
    '''행렬곱 A*B를 계산하여 반환하기'''
    matR = [len(B[0]) * [0] for i in range(len(A))]

    for i in range(len(matR)):
        for j in range(len(matR[i])):
            for k in range(len(A[i])):
                matR[i][j] += A[i][k] * B[k][j]

    return matR

def transpose(A):
    M = len(A)
    N = len(A[0])
    new_mat = [[0]*M for i in range(N)]
    for i in range(N):
        for j in range(M):
            new_mat[i][j] = A[j][i]
    return new_mat

def minus(a):
    return 1 if a>0 else -1

def find_leaving_index(X_b,A_b,A_q):
    '''leaving index를 탐색한다.
    반환값: leaving index, epillon'''
    # case 1 2-5x=0
    # case 2 -2+5x=0
    # 두가지 경우에 다 잘 동작해야 한다.
    temp = matmul(inv(A_b),A_q)

    ans_set = []
    for i in range(len(X_b)):
        if temp[i][0] > 1e-10:
            ans_set.append(X_b[i][0]/temp[i][0])
        else:
            ans_set.append(0)
    ans = 10**20
    idx = -1
    for i in range(len(X_b)):
        if ans_set[i]<ans and ans_set[i]>0:
            ans = ans_set[i]
            idx = i
    return idx,ans

# Polytope의 꼭짓점들을 지나면서 minimizer를 찾는다
def simplex_find_initial(goal,equations):
    '''simplex의 초기 Basis를 결정하기
        초기 Basis는 Z변수를 각 방정식에 추가하고, Z에 해당하는 부분을 Basis라고 정의한다.
        이후 해당 값에서 Simplex 탐색을 하여 Z가 포함되지 않은 Basis를 구한다.'''
    A, X, B = equations
    aux_goal = [0 for i in goal] + [1] * len(A)
    aux_B = [[i] for i in B]
    aux_basis = set([len(goal)+i for i in range(len(A))])
    aux_A = [A[i]+[int(i==j)*minus(B[j]) for j in range(len(A))] for i in range(len(A))]
    total_set = set(list(range(len(aux_A[0]))))
    counter = 0
    trans_A = transpose(aux_A)
    while True:
        counter +=1
        print(f'initial iteration {counter}th')
        # find X_b
        aux_V = total_set.difference(aux_basis)
        aux_V = sorted(aux_V)
        aux_basis = sorted(aux_basis)
        A_b = transpose([trans_A[i] for i in aux_basis])
        X_b = matmul(inv(A_b), aux_B)
        C_b = [[aux_goal[i]] for i in aux_basis]
        A_v = transpose([trans_A[i] for i in aux_V])
        C_v = [[aux_goal[i]] for i in aux_V]
        # lamda 구하기
        lamda = matmul(inv(transpose(A_b)), C_b)
        temp = matmul(transpose(A_v), lamda)
        mu_v = [0] * (len(C_v))
        for i in range(len(C_v)):
            mu_v[i] = C_v[i][0] - temp[i][0]

        # entering index 구하기
        # dantzig's rule로 계산하자 -> mu_v중에 가장 작은 값을 기준으로 업데이트 한다.
        idx = -1
        temp_min = 0
        for i in range(len(mu_v)):
            if mu_v[i] < temp_min:
                temp_min = mu_v[i]
                idx = i
        # mu_v의 모든 값이 양수면 최적해이므로 탐색 종료한다
        if idx == -1:
            break
        entering_idx = aux_V[idx]

        # leaving index 구하기
        A_q = [[i] for i in trans_A[entering_idx]]
        idx, epillon = find_leaving_index(X_b, A_b, A_q)
        leaving_idx = aux_basis[idx]
        # basis업데이트
        aux_basis = set(aux_basis)
        aux_basis.discard(leaving_idx)
        aux_basis.add(entering_idx)
    return aux_basis

def Simplex(goal,equations):
    '''simplex의 전략
    1. Initialization Phase
        초기 Basis를 찾는다.
    2. Optimization Phase
        Basis의 원소를 하나씩 교체해가면서 최적의 Basis를 찾는다'''
    A,X,B = equations
    basis = set(simplex_find_initial(goal,equations))
    print('initial basis',basis)
    B = [[i] for i in B]
    total_set = set(list(range(len(A[0]))))
    if basis.difference(total_set): # 빈 집합이 아니면 초기값 탐색이 실패
        basis = set(list(range(len(basis))))
    counter =0
    trans_A = transpose(A)
    while True:

        counter += 1
        print(f'iteration {counter}th')
        # find X_b
        V = total_set.difference(basis)
        V = sorted(V)
        basis = sorted(basis)
        print(basis,V,len(trans_A))
        A_b = transpose([trans_A[i] for i in basis])
        X_b = matmul(inv(A_b),B)
        C_b = [[goal[i]] for i in basis]
        A_v = transpose([trans_A[i]for i in V])
        C_v = [[goal[i]] for i in V]

        # lamda 구하기
        lamda = matmul(inv(transpose(A_b)),C_b)
        temp = matmul(transpose(A_v), lamda)
        mu_v = [0] * (len(C_v))
        for i in range(len(C_v)):
            mu_v[i] = C_v[i][0] - temp[i][0]

        # entering index 구하기
        # dantzig's rule로 계산하자 -> mu_v중에 가장 작은 값을 기준으로 업데이트 한다.
        idx = -1
        temp_min = 0
        for i in range(len(mu_v)):
            if mu_v[i]<temp_min:
                temp_min = mu_v[i]
                idx = i
        # mu_v의 모든 값이 양수면 최적해이므로 탐색 종료한다
        if idx== -1:
            break
        entering_idx = V[idx]

        # leaving index 구하기
        A_q = [[i] for i in trans_A[entering_idx]]
        idx,epillon = find_leaving_index(X_b,A_b,A_q)
        leaving_idx = basis[idx]

        # basis업데이트
        basis = set(basis)
        basis.discard(leaving_idx)
        basis.add(entering_idx)

        # 테스트 코드
        ans_X = [0] * len(goal)
        for i in range(len(basis)):
            ans_X[basis[i]] = X_b[i][0]
        sol = 0
        for i in range(len(goal)):
            sol += goal[i] * ans_X[i]
        print(f'{counter}th solution',sol)
    ans_X = [0] * len(goal)
    for i in range(len(basis)):
        ans_X[basis[i]] = X_b[i][0]
    sol = 0
    for i in range(len(goal)):
        sol += goal[i]*ans_X[i]
    return sol

#N,M = map(int,input().split())
#arr = [list(map(int,input().split())) for i in range(N)]
N,M = 100,100
import random,time
arr = [[random.randint(1,20000) for i in range(M)] for j in range(N)]
goal = [1] * (N+M)
A = []
B = []
for i in range(N):
    for j in range(M):
        if i!=0 and j!=0:
            break
        A.append([0 if i!=t else 1 for t in range(N)]+[0 if j!=k else 1 for k in range(M)])
        B.append(arr[i][j])
# 독립인 행은 반드시 N+M-1개가 된다 -> 최대 제약식의 개수 = 511개
s = time.time()
print(int(Simplex(goal,(A,[],B))+0.5))
e = time.time()
print('실행시간: ',e-s)