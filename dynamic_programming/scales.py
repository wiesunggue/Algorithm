# https://www.acmicpc.net/problem/2629
# 백준 2629번 양팔저울 문제
import copy
#MAX_WEIGHT = 30 * 500 + 1
MAX_WEIGHT = 20
N = int(input())
arr = list(map(int,input().split()))

M = int(input())
marbles = list(map(int,input().split()))

dpleft = [[0] * MAX_WEIGHT for i in range(N + 1)]
dpright = [[0] * MAX_WEIGHT for i in range(N + 1)]
dpleft[0][0] = 1
dpright[-1][0] = 1
for i in range(N):
    for m in range(MAX_WEIGHT):
        if m+arr[i]<MAX_WEIGHT and dpleft[i][m]:
            dpleft[i+1][m+arr[i]] = dpleft[i][m]
            dpleft[i+1][m] = dpleft[i][m]
        if m+arr[N-i-1]<MAX_WEIGHT and dpright[N-i][m]:
            dpright[N-i-1][m+arr[N-i-1]] = dpright[N-i][m]
            dpright[N-i-1][m] = dpright[N-i][m]


print(*dpleft, sep='\n')
print('*'*50)
print(*dpright, sep='\n')

def check_weight(marble):
    for i in range(N+1):
        print(i,N-i)
        for m in range(MAX_WEIGHT):
            if m+marble<MAX_WEIGHT and dpleft[i][m+marble] and dpright[N-i][m]:
                return "Y"
            if m+marble<MAX_WEIGHT and dpleft[i][m] and dpright[N-i][m+marble]:
                return "Y"
    return "N"

ans = []
for i in range(M):
    ans.append(check_weight(marbles[i]))

print(' '.join(ans))