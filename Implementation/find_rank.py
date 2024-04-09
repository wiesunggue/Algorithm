# https://www.acmicpc.net/problem/1205
# 백준 1205번 등수 구하기 문제
import sys
input = sys.stdin.readline

N,new_score,P = map(int,input().split())
arr = list(map(int,input().split()))
cnt = 1
for i in range(N):
    cnt += arr[i]>new_score
print(cnt)
if cnt+arr.count(new_score)>P:
    print(-1)
else:
    print(cnt)