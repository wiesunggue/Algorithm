# https://www.acmicpc.net/problem/8980
# 백준 8980번 택배 문제

import sys
input = sys.stdin.readline

N,C = map(int,input().split())
M = int(input())
arr = [list(map(int,input().split())) for i in range(M)]
arr.sort(key=lambda x:(x[1],x[0]))
cnt = 0
visit = [0] * (N)
for c in range(C):
    idx = 0
    # 보낼 택배가 있는 마을 중에 끝나는 점이 가장 작은 택배를 찾는다
    while idx<M:
        if arr[idx][2] != 0:
            break
        idx += 1

    # 모든 택배를 다 보낸 경우 탐색 종료
    if idx == M:
        break

    # 택배 보내는 마을은 택배 1감소
    last = arr[idx][1]
    arr[idx][2] -= 1
    cnt +=1
    for i in range(arr[idx][0],arr[idx][1]):
        visit[i] +=1
    # 탐색하기
    for i in range(idx,M):
        if last <= arr[i][0] and arr[i][2]:
            last = arr[i][1]
            cnt+=1
            arr[i][2] -= 1
            for t in range(arr[i][0],arr[i][1]):
                visit[t] +=1

print(cnt)
print(visit)
print(arr)