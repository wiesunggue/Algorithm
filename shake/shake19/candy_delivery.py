# https://www.acmicpc.net/problem/17305
# 캔디 배달하기
from collections import deque
N,W = map(int,input().split())
three=deque()
five=deque()
for i in range(N):
    a,b=map(int,input().split())
    if a==3:
        three.append(b)
    else:
        five.append(b)

three=[0]+sorted(list(three),reverse=True)
pthree=[0]*len(three)
pthree[0]=three[0]
five=[0]+sorted(list(five),reverse=True)
pfive=[0]*len(five)
pfive[0]=five[0]
for i in range(1,len(three)):
    pthree[i]=pthree[i-1]+three[i]
for i in range(1,len(five)):
    pfive[i]=pfive[i-1]+five[i]

# x는 3의 개수 y는 5의 개수

m=0
for i in range(W):
    x=i
    y=(W-x*3)//5
    print('xy',x,y)
    if x*3>W or y<0 or x>=len(pthree)-1 or y>=len(pfive)-1 or y*5>W:
        print('*****')
        continue
    m=max(pthree[x]+pfive[y],m)

print(m)