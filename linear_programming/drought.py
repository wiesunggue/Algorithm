# simplex 구현 알고리즘
# 수리적인 이론만 보고 구현해서 비효율적일 가능성이 있음

# 1. simplex 알고리즘은 제약이 EQUALITY FORM으로 작성되어야 함
# equality form은 AX=B, X>=0 minimize F(X)로 이루어짐
# AX <= B와 CX = D의 꼴이 있다면 A'X'=B의 꼴로 제약식을 변경해야 함
import time
def inverse_vector(A):
    '''벡터에 -를 곱한 값을 반환하기'''
    arr = A
    for i in range(len(A)):
        arr[i] = -A[i]

def identity_matrix(size):
    """Create an identity matrix of given size."""
    return [[1 if i == j else 0 for j in range(size)] for i in range(size)]


def multiply_row(row, scalar):
    """Multiply each element of a row by a scalar."""
    return [element * scalar for element in row]


def add_rows(row1, row2):
    """Add corresponding elements of two rows."""
    return [element1 + element2 for element1, element2 in zip(row1, row2)]


def gauss_jordan(matrix):
    """Apply Gauss-Jordan elimination to the given matrix."""
    num_rows = len(matrix)
    num_columns = len(matrix[0])

    for i in range(num_rows):
        # Make the diagonal element 1
        diagonal_element = matrix[i][i]
        matrix[i] = multiply_row(matrix[i], 1 / diagonal_element)

        # Eliminate non-diagonal elements
        for j in range(num_rows):
            if i != j:
                factor = matrix[j][i]
                matrix[j] = add_rows(matrix[j], multiply_row(matrix[i], -factor))


def inverse_mat(matrix):
    """Find the inverse of the given matrix using Gauss-Jordan elimination."""
    num_rows = len(matrix)
    augmented_matrix = [row + identity_matrix(num_rows)[row_num] for row_num, row in enumerate(matrix)]

    gauss_jordan(augmented_matrix)

    # Extract the inverse matrix from the augmented matrix
    inv_matrix = [row[num_rows:] for row in augmented_matrix]

    return inv_matrix

def matmul(A,B):
    '''행렬곱 A*B를 계산하여 반환하기'''
    matR = [len(B[0]) * [0] for i in range(len(A))]

    for i in range(len(matR)):
        for j in range(len(matR[i])):
            for k in range(len(A[i])):
                matR[i][j] += A[i][k] * B[k][j]

    return matR

def determinant(A):
    '''행렬식을 계산해서 반환하기(가우스 소거법이용하자)'''
    pass

def transpose(A):
    M = len(A)
    N = len(A[0])
    new_mat = [[0]*M for i in range(N)]
    for i in range(N):
        for j in range(M):
            new_mat[i][j] = A[j][i]
    return new_mat

def convert_constraint(ineq,eq,goal):
    '''1. simplex 알고리즘은 제약이 EQUALITY FORM으로 작성되어야 함
    즉, AX <= B와 CX = D의 꼴이 있다면 A'X'=B의 꼴로 제약식을 변경해야 함'''

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
    return 1 if a>0 else -1

def find_leaving_index(X_b,A_b,A_q):
    '''leaving index를 탐색한다.
    반환값: leaving index, epillon'''
    # case 1 2-5x=0
    # case 2 -2+5x=0
    # 두가지 경우에 다 잘 동작해야 한다.
    temp = matmul(inverse_mat(A_b),A_q)

    ans_set = []
    for i in range(len(X_b)):
        ans_set.append(X_b[i][0]/temp[i][0])
    ans = 10**20
    idx = -1
    for i in range(len(X_b)):
        if ans_set[i]<ans and ans_set[i]>0:
            ans = ans_set[i]
            idx = i
    print('leaving idx',X_b,A_b,A_q,temp,idx,ans)
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
    while True:
        counter +=1
        print('aux_basis',aux_basis)
        # find X_b
        aux_V = total_set.difference(aux_basis)
        aux_V = sorted(aux_V)
        aux_basis = sorted(aux_basis)
        trans_A = transpose(aux_A)
        A_b = transpose([trans_A[i] for i in aux_basis])
        X_b = matmul(inverse_mat(A_b), aux_B)
        C_b = [[aux_goal[i]] for i in aux_basis]
        A_v = transpose([trans_A[i] for i in aux_V])
        C_v = [[aux_goal[i]] for i in aux_V]

        # lamda 구하기
        lamda = matmul(inverse_mat(transpose(A_b)), C_b)
        print('lamda',lamda,C_b,aux_goal,'X_b',X_b,A_b)
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
        print('mu',mu_v)
        if idx == -1:
            break
        entering_idx = aux_V[idx]

        # leaving index 구하기
        A_q = [[i] for i in trans_A[entering_idx]]
        idx, epillon = find_leaving_index(X_b, A_b, A_q)
        leaving_idx = aux_basis[idx]
        print(f'{counter}th important info',mu_v,aux_basis,'entering',entering_idx,'leaving',leaving_idx,'c:',C_v,'temp:',temp)
        # basis업데이트
        aux_basis = set(aux_basis)
        aux_basis.discard(leaving_idx)
        aux_basis.add(entering_idx)
        #print('basis',aux_basis)
        #time.sleep(1)
    print('final aux_baiss',aux_basis)
    return aux_basis
def Simplex(goal,equations):
    '''simplex의 전략
    1. Initialization Phase
        초기 Basis를 찾는다.
    2. Optimization Phase
        Basis의 원소를 하나씩 교체해가면서 최적의 Basis를 찾는다'''
    A,X,B = equations
    basis = set(simplex_find_initial(goal,equations))
    #basis = set([1,2])
    B = [[i] for i in B]
    total_set = set(list(range(len(A[0]))))
    while True:
        print('basis',basis)
        # find X_b
        V = total_set.difference(basis)
        V = sorted(V)
        basis = sorted(basis)
        trans_A = transpose(A)
        A_b = transpose([trans_A[i] for i in basis])
        X_b = matmul(inverse_mat(A_b),B)
        C_b = [[goal[i]] for i in basis]
        A_v = transpose([trans_A[i]for i in V])
        C_v = [[goal[i]] for i in V]

        # lamda 구하기
        lamda = matmul(inverse_mat(A_b),C_b)
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
        print('mu_v entering list',idx,basis,C_v,goal,mu_v)
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
        print('basis',basis)
    ans_X = [0] * len(goal)
    for i in range(len(basis)):
        ans_X[basis[i]] = X_b[i][0]
    sol = 0
    print(ans_X,X_b)
    for i in range(len(goal)):
        sol += goal[i]*ans_X[i]
    return sol


goal = [1,2,3]
A = [[5,-1,1],[5,1,-3]]
B = [1,-2]
print(Simplex(goal,(A,[],B)))

