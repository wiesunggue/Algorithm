# https://www.acmicpc.net/problem/9372
# 백준 9372번 상근이의 여행

# 비행기의 종류는 항상 노드의 개수 - 1과 같다
import sys
input = sys.stdin.readline
T = int(input())
for test in range(T):
    N,M = map(int,input().split())
    for i in range(M):
        input()
    print(N-1)