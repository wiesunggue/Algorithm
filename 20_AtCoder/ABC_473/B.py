from collections import Counter
N = int(input())
arr = list(map(int, input().split()))

c = Counter(arr)
ans = 0
for i in c.keys():
    if c[i] % 2 == 1:
        ans += i

print(ans)
