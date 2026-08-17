from collections import defaultdict
N = int(input())
d = defaultdict(int)
for i in range(N):
    d[input().lower()] += 1

print(max(d.values()))