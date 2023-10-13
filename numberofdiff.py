from collections import Counter
N=int(input())
maxarr=[2**i for i in range(N)]
minarr=[i for i in range(N)]
print(N*(N-1)//2)
print(*maxarr)
print(N-1)
print(*minarr)