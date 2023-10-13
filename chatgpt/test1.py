# Read the input
n = int(input())
a = [int(input()) for i in range(n)]

# Read the queries
queries = []
for _ in range(int(input())):
    x, y, k = map(int, input().split())
    queries.append((x - 1, y - 1, k))

# Precompute prefix sums
for i in range(1, n):
    a[i] += a[i - 1]

# Answer the queries
for x, y, k in queries:
    # Check if the indices are within the bounds of the array
    if x < 0 or y >= n:
        print(0)
        continue
    
    # If the indices are within bounds, compute the sum using the prefix sums
    print((a[y] - a[x - 1]) // k)