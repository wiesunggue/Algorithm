# https://www.acmicpc.net/problem/1889
# 백준 1889번 선물 교환 문제

from collections import deque
def solutions():
    N = int(input())
    send = [[] for i in range(N+1)]
    receive = [[]for i in range(N+1)]
    table = [0] * (N+1)
    for i in range(1,N+1):
        a,b = map(int,input().split())
        send[i].append(b)
        send[i].append(a)
        receive[a].append(i)
        receive[b].append(i)
        table[a] += 1
        table[b] += 1
    dq = deque()
    for i in range(1,N+1):
        if table[i]==0:
            dq.append(i)
        elif table[i]==1:
            dq.append(receive[i][0])
    print(table)
    while dq:
        idx = dq.popleft()
        pop_idx = []
        for i in send[idx]:
            table[i] -= 1
            if table[i] == 0:
                dq.append(i)
#            elif table[i] == 1:
#                dq.append(receive[i][0])
    ans = []
    for i in range(1,N+1):
        if table[i] == 2:
            ans.append(str(i))
    print(table)
    print(len(ans))
    if len(ans)!= 0:
        print(' '.join(ans))
if __name__ == '__main__':
    solutions()