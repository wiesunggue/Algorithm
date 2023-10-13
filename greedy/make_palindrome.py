# https://www.acmicpc.net/problem/1213
# 팰린드룸 만들기 문제

from collections import Counter,deque
d=Counter(input())

cnt=0
odd=0
for i in d.keys():
    if d[i]%2==1:
        cnt+=1
        odd=i
ans=[]
ans2=deque()
if cnt>1:
    print("I'm Sorry Hansoo")

else:
    for i in sorted(d.keys()):
        c=d[i]
        a=c//2
        while a:
            a-=1
            ans.append(i)
        a=c//2
        while a:
            a-=1
            ans2.append(i)
        if odd==i:
            mid=i
    if odd!=0:
        ans.append(mid)
    while ans2:
        ans.append(ans2.pop())
    print(*ans,sep='')

