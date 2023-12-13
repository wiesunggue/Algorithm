# https://www.acmicpc.net/problem/13164
# 백준 13164 행복 유치원 문제

N,K = map(int,input().split())
arr = list(map(int,input().split()))

diff = [0]*(N-1)
for i in range(1,N):
    diff[i-1] = arr[i]-arr[i-1]
diff.sort()
print(sum(diff[:N-K]))