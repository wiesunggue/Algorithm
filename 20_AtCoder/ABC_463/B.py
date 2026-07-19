import sys

N, X = input().split()
N = int(N)
X = ord(X)-ord('A')
arr = [input() for i in range(N)]
ans = "No"
for i in range(N):
    if arr[i][X] == 'o':
        ans = "Yes"

print(ans)