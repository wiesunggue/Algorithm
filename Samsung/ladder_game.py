# https://www.acmicpc.net/problem/15684
# 사다리 게임
import sys
input = sys.stdin.readline

N,M,H = map(int,input().split())
arr = [[0]*(N+2) for i in range(H+2)]
ans = 4
for i in range(M):
    a,b = map(int,input().split())
    arr[a][b] = 1

def backtracking(cnt):
    global ans
    wrong = ladderstart()
    if wrong == 0:
        ans = min(ans,cnt)
    if cnt >= ans or cnt>=3:
        return

    # 가지치기 주의해야 함
    if wrong > (3-cnt)*2:
        return
    for i in range(1,H+1):
        for j in range(1,N):
            if arr[i][j] == 1 or arr[i][j+1] == 1 or arr[i][j-1] == 1:
                continue
            arr[i][j] = 1
            backtracking(cnt+1)
            arr[i][j] = 0

def ladderstart():
    ladder = [i for i in range(N+1)]
    for i in range(1,H+1):
        for j in range(1,N):
            if arr[i][j] == 1:
                ladder[j],ladder[j+1] = ladder[j+1],ladder[j]
    wrong = 0
    for i in range(N+1):
        if ladder[i] != i:
            wrong += 1
    return wrong

backtracking(0)
if ans > 3:
    print(-1)
else:
    print(ans)