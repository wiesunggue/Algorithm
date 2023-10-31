# https://www.acmicpc.net/problem/1863
# 백준 1863번 스카이라인 쉬운거

from collections import deque

def solution():
    # 같은값이 온다 -> 그대로 제거
    # 작은값이 온다 -> 같거나 작아질 때까지 여러개 제거하고 count
    # 큰값이 온다 -> append시켜줌
    N = int(input())
    arr = [list(map(int,input().split())) for i in range(N)]
    dq = deque()
    dq.append(-1)
    dq.append(arr[0][1])

    ans = 0
    for i in range(1,N):
        if dq[-1] == arr[i][1]:
            ans +=1
        elif dq[-1] < arr[i][1]:
            dq.append(arr[i][1])
        else:
            while dq[-1] > arr[i][1]:
                dq.pop()
                ans += 1
            if dq[-1] != arr[i][1]:
                dq.append(arr[i][1])

    while dq[-1]>0:
        dq.pop()
        ans += 1
    print(ans,dq)

solution()