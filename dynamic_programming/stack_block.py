# https://www.acmicpc.net/problem/18427
# 백준 18427번 함께 블록 쌓기 문제
import sys
input = sys.stdin.readline

N,M,H = map(int,input().split())
students = [sorted(map(int,input().split())) for i in range(N)]


dp_array = [[1 if i==0 else 0 for i in range(H+1)] for j in range(N+1)]
for i in range(1,N+1):
    dp_array[i] = dp_array[i-1].copy()
    for value in students[i-1]:
        for k in range(value,H+1):
            dp_array[i][k] += dp_array[i-1][k-value]
            dp_array[i][k] %= 10007

print(dp_array[N][H]%10007)