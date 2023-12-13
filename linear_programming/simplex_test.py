# https://www.acmicpc.net/problem/1281

# simplex 구현 알고리즘
# 수리적인 이론만 보고 구현해서 비효율적일 가능성이 있음

# 1. simplex 알고리즘은 제약이 EQUALITY FORM으로 작성되어야 함
# equality form은 AX=B, X>=0 minimize F(X)로 이루어짐
# AX <= B와 CX = D의 꼴이 있다면 A'X'=B의 꼴로 제약식을 변경해야 함
import time
import numpy as np
import random
def swap_rows(matrix, i, j):
    matrix[i], matrix[j] = matrix[j].copy(), matrix[i].copy()

def inv(matrix):
    '''역행렬 게산하는 함수 입력을 이중 List로 받고, 이중 list로 반환한다'''
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
def identity_matrix(size):
    """Create an identity matrix of given size."""
    return [[1 if i == j else 0 for j in range(size)] for i in range(size)]

def matmul(mat1,mat2):
    '''행렬곱 mat1*mat2를 계산하여 반환하는 함수, 행렬은 이중 리스트로 구현됨'''
    matR = [len(mat2[0]) * [0] for i in range(len(mat1))]

    for i in range(len(matR)):
        for j in range(len(matR[i])):
            for k in range(len(mat1[i])):
                matR[i][j] += mat1[i][k] * mat2[k][j]

    return matR

def transpose(matrix):
    """행렬을 입력받아 입력받은 행렬의 전치 행렬을 반환하는 함수, 입력은 이중 리스트이다"""
    M = len(matrix)
    N = len(matrix[0])
    new_mat = [[0]*M for i in range(N)]
    for i in range(N):
        for j in range(M):
            new_mat[i][j] = matrix[j][i]
    return new_mat

def convert_constraint(ineq,eq,goal):
    '''1. simplex 알고리즘은 제약이 EQUALITY FORM으로 작성되어야 함
    즉, AX <= B와 CX = D의 꼴이 있다면 A'X'=B의 꼴로 제약식을 변경해야 함 ////아직 사용하지 않음'''

    A,B = ineq # 튜플로 입력받은 2차원 배열(A)과 벡터(B) (AX>B는 음수를 곱해서 AX<B로 변환)
    C,D = eq

    # 해야할 일 2가지
    # 1. equality form에서 X+와 X-를 구분하여 양수 대신 실수 전체에서 동작하도록 설정
    # 2. iniequality form에서 slack변수를 추가해서 A(X+-X-)+S = B꼴로 변경
    new_arr = []
    new_vector = []
    variable = []
    new_goal = [] # TODO 수정해야함
    # equality 처리하기
    for i in range(len(C)):
        new_arr.append(C[i]+inverse_arr(C[i]))
        variable.append(f'eq{i}X+')
    for i in range(len(C)):
        variable.append(f'eq{i}X-')

    # inequality 처리하기
    for i in range(len(A)):
        new_arr.append(A[i]+inverse_arr(A[i])+[0 if i!=k else 1 for k in range(len(A))])
        variable.append(f'eq{len(C)+i}X+')
    for i in range(len(A)):
        variable.append(f'eq{len(C)+i}X-')
    for i in range(len(A)):
        variable.append(f'eq{len(C)+i}slack+')
    new_vector = B+D

    return goal,(new_arr,variable,new_vector) # equality form반환
def minus(a):
    '''리스트를 입력받아 양수는 1 음수는 -1가지도록 하는 함수'''
    return 1 if a>0 else -1

def find_leaving_index(X_b,A_b,A_q):
    '''leaving index를 탐색한다.
    #A_b^-1 * A_q * x = X_b의 해를 푼다
    leaving index를 찾기 위해서 각 방정식의 해를 구하고, 해 중 최소인 양수 해를 선택한다.
    만약 최소가 되는 양수 해가 없다면 -1을 반환
    Returns: leaving index, epillon'''
    size = len(X_b) # 입력받은 방정식의 개수
    temp = matmul(inv(A_b),A_q)

    ans_set = [0]*size
    # 각 방정식의 해를 구한다.
    for i in range(size):
        if temp[i][0] > 1e-10: # 분모가 1e-10보다 작으면 분모가 0이라고 판단한다.
            ans_set[i] = X_b[i][0]/temp[i][0]
        else:
            ans_set[i] = 2**64

    # 양수인 해 중 가장 작은 값을 찾는다.
    ans = min(ans_set)
    idx = ans_set.index(ans) # 만약 모든 해가 문제가 있다면 idx = -1이 반환됨
    return idx,ans

# Polytope의 꼭짓점들을 지나면서 minimizer를 찾는다
def simplex_find_initial(goal,equations):
    '''simplex의 초기 Basis를 결정하기
        초기 Basis는 Z변수를 각 방정식에 추가하고, Z에 해당하는 부분을 Basis라고 정의한다.
        이후 해당 값에서 Simplex 탐색을 하고 Basis를 반환한다.'''
    A, X, B = equations
    # aux문제로 만들기 위해서 모든 방정식에 slack변수를 추가한다.

    # num_of_eq: 부등식의 개수, num_of_var: 변수의 개수
    num_of_eq, num_of_var = len(A),len(goal)
    aux_goal = [0 for i in goal] + [1] * num_of_eq
    aux_B = [[i] for i in B]
    aux_basis = set([num_of_var+i for i in range(num_of_eq)]) # 초기 기저는 추가된 변수
    aux_A = [A[i]+[int(i==j)*minus(B[j]) for j in range(num_of_eq)] for i in range(num_of_eq)]

    # 새롭게 정의된 문제 Aux문제
    # aux_num_of_eq, aux_num_of_var
    aux_num_of_eq, aux_num_of_var = len(aux_A), len(aux_A[0])
    total_set = set(range(aux_num_of_var))
    # B와 V의 개수
    num_of_B, num_of_V = len(aux_B), aux_num_of_var-len(aux_B)

    aux_trans_A = transpose(aux_A)

    counter = 0
    while True:
        counter +=1

        # aux V 업데이트
        aux_V = total_set.difference(aux_basis)
        aux_V = sorted(aux_V)
        aux_basis = sorted(aux_basis)

        # 연산에 필요한 기본 변수 생성하기
        A_b = transpose([aux_trans_A[i] for i in aux_basis])
        X_b = matmul(inv(A_b), aux_B)
        C_b = [[aux_goal[i]] for i in aux_basis]
        A_v = transpose([aux_trans_A[i] for i in aux_V])
        C_v = [[aux_goal[i]] for i in aux_V]

        # lamda 구하기
        lamda = matmul(inv(transpose(A_b)), C_b)
        temp = matmul(transpose(A_v), lamda)
        mu_v = [0] * (num_of_V)
        for i in range(num_of_V):
            mu_v[i] = C_v[i][0] - temp[i][0]

        # entering index 구하기
        # dantzig's rule로 계산하자 -> mu_v중에 가장 작은 값을 기준으로 업데이트 한다.
        temp_min = min(mu_v)
        # mu_v의 모든 값이 양수면 최적해이므로 탐색 종료한다
        if temp_min>=-1e-15:
            break
        idx = mu_v.index(temp_min)
        entering_idx = aux_V[idx]

        # leaving index 구하기
        A_q = [[i] for i in aux_trans_A[entering_idx]]
        idx, epillon = find_leaving_index(X_b, A_b, A_q)
        leaving_idx = aux_basis[idx]
        #print(f'{counter}th important info',mu_v,aux_basis,'entering',entering_idx,'leaving',leaving_idx,'c:',C_v,'temp:',temp)

        # basis업데이트
        aux_basis = set(aux_basis)
        aux_basis.discard(leaving_idx)
        aux_basis.add(entering_idx)
        #print('basis',aux_basis)
        #time.sleep(1)
    #print('final aux_baiss',aux_basis)

    # 해당 문제에서는 최적해를 계산할 이유가 없다.
    return aux_basis

def Simplex(goal,equations):
    '''simplex의 전략
    1. Initialization Phase
        초기 Basis를 찾는다.
    2. Optimization Phase
        Basis의 원소를 하나씩 교체해가면서 최적의 Basis를 찾아서 이때의 최적해를 반환한다'''
    A,X,B = equations
    num_of_eq, num_of_var = len(A),len(goal)
    basis = set(simplex_find_initial(goal,equations))
    total_set = set(list(range(num_of_eq)))

    # 주의!!!!!!
    # 심플렉스 연산 결과 basis에 aux의 변수가 basis로 들어갔다면 해당 제약식은 모순이 존재한다
    if len(basis.difference(total_set)) == 0:
        raise Exception("The Equation has a Contradict!")
    B = [[i] for i in B]
    trans_A = transpose(A)

    # B와 V의 개수
    num_of_B, num_of_V = len(basis), num_of_var - len(basis)

    counter =0
    while True:
        counter += 1

        # V 업데이트
        V = total_set.difference(basis)
        V = sorted(V)
        basis = sorted(basis)

        # 연산에 필요한 기본 변수 생성하기
        A_b = transpose([trans_A[i] for i in basis])
        X_b = matmul(inv(A_b),B)
        C_b = [[goal[i]] for i in basis]
        A_v = transpose([trans_A[i]for i in V])
        C_v = [[goal[i]] for i in V]

        # lamda 구하기
        lamda = matmul(inv(transpose(A_b)),C_b)
        temp = matmul(transpose(A_v), lamda)
        mu_v = [0] * (num_of_V)
        for i in range(num_of_V):
            mu_v[i] = C_v[i][0] - temp[i][0]

        # entering index 구하기
        # dantzig's rule로 계산하자 -> mu_v중에 가장 작은 값을 기준으로 업데이트 한다.
        temp_min = min(mu_v)
        # mu_v의 모든 값이 양수면 최적해이므로 탐색 종료한다
        if temp_min>=-1e-15:
            break
        idx = mu_v.index(temp_min)
        entering_idx = V[idx]

        # leaving index 구하기
        A_q = [[i] for i in trans_A[entering_idx]]
        idx,epillon = find_leaving_index(X_b,A_b,A_q)
        leaving_idx = basis[idx]

        # basis업데이트
        basis = set(basis)
        basis.discard(leaving_idx)
        basis.add(entering_idx)

    # 각 변수가 가지는 값을 저장하기(Basis에 대해서만 계산된 것을 0을 포함한 식으로 변환한다)
    ans_X = [0] * num_of_var
    for i in range(num_of_B):
        ans_X[basis[i]] = X_b[i][0]
    sol = 0
    print(ans_X,X_b,basis)

    # 제약식을 만족하면서 최소를 이루는 해 계산하기
    for i in range(num_of_var):
        sol += goal[i]*ans_X[i]
    return sol

#N,M = map(int,input().split())
#arr = [list(map(int,input().split())) for i in range(N)]
arr = [[2,1,2],[3,1,1]]

def tln(n,m):
    '''테스트용 함수'''
    N,M = 10,10
    goal = [1] * (N+M)
    A = []
    #B = []
    for i in range(N):
        for j in range(M):
            if i!=0 and j!=0:
                break
            A.append([0 if i!=t else 1 for t in range(N)]+[0 if j!=k else 1 for k in range(M)])
    A = np.array(A)
    return np.linalg.matrix_rank(A)!=len(A)
#N=256
#M=256
#cnt=0
#for i in range(N):
#    for j in range(M):
#        cnt += tln(i,j)
#print(cnt)
s = time.time()
inv([[random.randint(1,100) for i in range(100)] for j in range(100)])
e = time.time()
print('inv연산 한번 수행시간: ',e-s)
# 독립인 행은 반드시 N+M-1개가 된다 -> 최대 제약식의 개수 = 511개
N = 2
M = 4
A = []
B = []
arr = [[random.randint(1,20000) for i in range(M)] for j in range(N)]
goal = [1] * (N+M)

for i in range(N):
    for j in range(M):
        if i!=0 and j!=0:
            break
        A.append([0 if i!=t else 1 for t in range(N)]+[0 if j!=k else 1 for k in range(M)])
        B.append(arr[i][j])
B = [100,200,300,400]
A = [[1,0,1,0,0,0],
     [1,0,0,1,0,0],
     [1,0,0,0,1,0],
     [1,0,0,0,0,1],
     ]
goal = [100,0,0,0,0,0]
print(A,B)
import numpy as np
print(np.linalg.matrix_rank(np.array(A)), len(A))
s = time.time()
print(Simplex(goal,(A,[],B)))
e = time.time()
print('simplex 수행시간: ',e-s)
#print(*np_mat(mat),sep='\n')

# 1. 독립이란 무엇인가?
# 단순하게 Reduced row echelon form(Rref)을 만드는 것(혹은 유효한 rank를 가지는) 부등식을 선택하는 것이라 생각을 했으나
# 부등식의 독립은 해당 방식으로 계산하면 안됨 -> a+b+c+d<100, a+b<10, c+d<10 일때 독립이 되도록 하는 부등식은 어떻게 되어야 하는가?
# [1 1 1 1]   [100]
# [1 1 0 0] < [10]
# [0 0 1 1]   [10]
# 해당 식에서는 Rref독립이 되는 부등식을 찾는다면 1,2번 부등식이지만 3번 부등식을 버리게 될 경우 최적해는 달라짐


#minimize a+b+c+d+e, subject to Ax = b 이고 Ax=B가 아래와 같습니다
#[1 0 1 0 0 0][a] = [15]
#[1 0 0 1 0 0][b] = [2]
#[1 0 0 0 1 0][c] = [3]
#[1 0 0 0 0 1][d] = [4]
#[0 1 1 0 0 0][e] = [6]
