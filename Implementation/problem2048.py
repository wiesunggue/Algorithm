import sys
from copy import deepcopy

input = sys.stdin.readline
def change(x,y):
    global arr
    temp = arr[x[0]][x[1]]
    arr[x[0]][x[1]] = arr[y[0]][y[1]]
    arr[y[0]][y[1]] = temp
def left():
    # 값이 있는 배열의 인덱스 찾기
    idx_arr = [[]for i in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j]!=0:
                idx_arr[i].append(j)
    # 합치기
    for i in range(N):
        for j in range(1,len(idx_arr[i])):
            if arr[i][idx_arr[i][j]]==arr[i][idx_arr[i][j-1]]:
                arr[i][idx_arr[i][j-1]] *= 2
                arr[i][idx_arr[i][j]] = 0

    # 밀기
    for i in range(N):
        pos = 0
        for j in range(len(idx_arr[i])):
            idx = idx_arr[i][j]
            if arr[i][idx] != 0:
                arr[i][pos] = arr[i][idx]
                pos += 1
        for j in range(pos,N):
            arr[i][j] = 0


def right():
    # 값이 있는 배열의 인덱스 찾기
    idx_arr = [[]for i in range(N)]
    for i in range(N):
        for j in range(N-1,-1,-1):
            if arr[i][j]!=0:
                idx_arr[i].append(j)

    # 합치기
    for i in range(N):
        for j in range(1,len(idx_arr[i])):
            if arr[i][idx_arr[i][j-1]]==arr[i][idx_arr[i][j]]:
                arr[i][idx_arr[i][j-1]] *= 2
                arr[i][idx_arr[i][j]] = 0

    # 밀기
    for i in range(N):
        pos = N-1
        for j in range(len(idx_arr[i])):
            idx = idx_arr[i][j]
            if arr[i][idx] != 0:
                arr[i][pos] = arr[i][idx]
                pos -= 1
        for j in range(pos,-1,-1):
            arr[i][j] = 0

def up():
    # 값이 있는 배열의 인덱스 찾기
    idx_arr = [[] for i in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[j][i]!=0:
                idx_arr[i].append(j)
    # 합치기
    for i in range(N):
        for j in range(1,len(idx_arr[i])):
            if arr[idx_arr[i][j]][i]==arr[idx_arr[i][j-1]][i]:
                arr[idx_arr[i][j-1]][i] *= 2
                arr[idx_arr[i][j]][i] = 0
    # 밀기
    for i in range(N):
        pos = 0
        for j in range(len(idx_arr[i])):
            if arr[idx_arr[i][j]][i] != 0:
                arr[pos][i] = arr[idx_arr[i][j]][i]
                pos += 1
        for j in range(pos,N):
            arr[j][i] = 0

def down():
    # 값이 있는 배열의 인덱스 찾기
    idx_arr = [[] for i in range(N)]
    for i in range(N):
        for j in range(N-1,-1,-1):
            if arr[j][i]!=0:
                idx_arr[i].append(j)
    # 합치기
    for i in range(N):
        for j in range(1,len(idx_arr[i])):
            if arr[idx_arr[i][j]][i]==arr[idx_arr[i][j-1]][i]:
                arr[idx_arr[i][j-1]][i] *= 2
                arr[idx_arr[i][j]][i] = 0
    # 밀기
    for i in range(N):
        pos = N-1
        for j in range(len(idx_arr[i])):
            if arr[idx_arr[i][j]][i] != 0:
                arr[pos][i] = arr[idx_arr[i][j]][i]
                pos -= 1
        for j in range(pos,-1,-1):
            arr[j][i] = 0

def move(query):
    if query==0:
        left()
    elif query==1:
        right()
    elif query==2:
        up()
    elif query==3:
        down()

ans = 0
def backtracking(cnt):
    global ans,arr
    if cnt==5:
        ans = max(ans, max(map(max,arr)))
        return
    for i in range(4):
        temp = deepcopy(arr)
        move(i)
        backtracking(cnt+1)
        arr = deepcopy(temp)
N = int(input())
arr = [list(map(int,input().split())) for i in range(N)]
backtracking(0)
print(ans)
