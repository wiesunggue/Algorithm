# https://www.acmicpc.net/problem/17435
# 백준 17435번 합성함수와 쿼리 문제

import sys
import math
input = sys.stdin.readline
print = sys.stdout.write
def make_sparse_mat():
    '''희소 행렬을 구성하는 함수'''
    N = len(arr)-1
    for i in range(22):
        for j in range(0,N+1):
            if i ==0:
                sparse[j][i] = j
            elif i ==1:
                sparse[j][i] = arr[j]
            else:
                sparse[j][i] = sparse[sparse[j][i-1]][i-1]
# 0은 x(자기자신)
# 1은 f1(x)
# 2은 f2(x)
# 3은 f4(x)로 정의한다

def query(n,x):
    '''쿼리를 처리하는 코드
    ex) 10, 1을 입력받으면 10은 이진수로 1010이므로 f2(1)을 먼저 계산하고 해당 계산 결과를 f8(f2(1))로 바꾸어 계산한다'''
    while n:
        t = n & (-n) # 최소 원소 찾기
        n &= (n-1) # 최소 원소 지우기
        x= sparse[x][t.bit_length()] # 최소 비트를 찾아서 합성곱을 진행한다.
    return x

N = int(input())
arr = [0]+list(map(int,input().split()))
sparse = [[0]*22 for i in range(N+1)]

make_sparse_mat() # 희소 행렬을 만든다.
M = int(input())
for i in range(M):
    n,x = map(int,input().split())
    print(f'{query(n,x)}\n')

