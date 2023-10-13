# https://www.acmicpc.net/problem/20667
# 크롬
import random
import time
N,M,K = 100,100,10000
arr={'(0,0)':0}
ans=10**9
data = [[random.randint(1,30), random.randint(1,1000),random.randint(1,5)] for i in range(N)]
start=time.time()
for i in range(N):
    tmp={}
    for j in arr.keys():
        if arr[j]>ans:
            continue
        cpu, memory =eval(j)
        if cpu >= M and memory >= K:
            ans = min(ans, arr[j])
            continue
        c,m,p=data[i]
        s=str((cpu+c,memory+m))
        if arr.get(s)==None:
            tmp[s]=p+arr[j]
        else:
            tmp[s]=min(p+arr[j],arr[s])
    arr.update(tmp)
print(arr)
print(ans)
print(time.time()-start)