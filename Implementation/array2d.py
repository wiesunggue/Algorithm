# https://www.acmicpc.net/problem/17140
# 백준 17140번 이차원 배열과 연산 문제
from collections import Counter

r,c,k = map(int,input().split())
r,c = r-1,c-1
arr = [list(map(int,input().split())) for i in range(3)]

def R_cal():
    max_len = 0
    for i in range(len(arr)):
        temp=Counter(arr[i])
        b = []
        for key,value in sorted(temp.items(),key=lambda x: (x[1],x[0])):
            if key==0:
                continue
            b.append(key)
            b.append(value)
        # 100개 넘어가는 경우
        if len(b)>100:
            arr[i] = b[:100]
        else:
            arr[i]= b
        max_len = max(max_len,len(b))

    # 빈 칸에 0채우기
    for i in range(len(arr)):
        arr[i] += [0]*(max_len-len(arr[i]))

def transpose():
    global arr
    temp = [[0]*len(arr) for i in range(len(arr[0]))]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            temp[j][i] = arr[i][j]
    arr = temp

def C_cal():
    transpose()
    R_cal()
    transpose()


def update_arr():
    R,C = len(arr),len(arr[0])
    if R>=C:
        R_cal()
    else:
        C_cal()

ans = -1
for t in range(101):
    if c<len(arr[0]) and r<len(arr):
        if arr[r][c]==k:
            ans = t
            break
    update_arr()

print(ans)