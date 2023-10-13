#https://www.acmicpc.net/problem/9657
# 돌 게임3
cache=[0,1,2,1,1,3,3,4]+[-1]*1001
N=int(input())
for i in range(5,1005):
    if cache[i-1]%2==0:
        cache[i]=cache[i-1]+1
    elif cache[i-3]%2==0:
        cache[i]=cache[i-3]+1
    elif cache[i-4]%2==0:
        cache[i]=cache[i-4]+1
    else:
        cache[i]=min(cache[i-1],cache[i-3],cache[i-4])+1

print('CY' if cache[N]%2==0 else 'SK')