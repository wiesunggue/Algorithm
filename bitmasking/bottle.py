# https://www.acmicpc.net/problem/1052
# 물병 문제

def bit_count(x):
    if x==0:
        return 0
    return x%2+bit_count(x//2)
def min_bit(x):
    for i in range(100):
        if (1<<i)&x:
            return i
N,K = map(int,input().split())
N_before=N
while bit_count(N)>K:
    buy=min_bit(N)
    N+=1<<buy
print(N-N_before)
