from collections import Counter
N = int(input())
C = Counter(map(int, input().split()))

print(N-max(C.values()))