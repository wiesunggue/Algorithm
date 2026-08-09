from collections import Counter
import sys
input = sys.stdin.readline
print = sys.stdout.write
N, Q = map(int, input().split())
A = [0] * N
C = Counter(A)
count = 0
def get_xor():
    ans = 0
    for k,v in C.items():
        if v % 2 == 1 and k-count >= 1:
            ans ^= k-count
    return ans
result = []
for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        C[A[query[1]-1]] -= 1
        if C[A[query[1]-1]] == 0:
            C.pop(A[query[1]-1])
        A[query[1]-1] += 1
        C[A[query[1]-1]] += 1
        result.append(str(get_xor()))
    elif query[0] == 2:
        count += 1
        result.append(str(get_xor()))

print('\n'.join(result))

