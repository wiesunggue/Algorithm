from collections import defaultdict

N = int(input())
arr = defaultdict(int)
for i in range(N):
    arr[input()] += 1

for i in range(N-1):
    arr[input()] -= 1

for i in arr:
    if arr[i]==1:
        print(i)