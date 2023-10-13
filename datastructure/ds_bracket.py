from collections import deque
s=input()

dq=deque()
ans=[]
for i in s:
    if dq:
        ans.append(2)
    if i=='(' or i=='[':
        dq.append(i)
    else:
        a=dq.pop()
        if a=='(' and i==')':
            ans[-1]*=ans[-1]*2
        elif a=='[' and i==']':
            ans[-1]*=ans[-1]*3
        else:
            ans=[]
            break

print(sum(ans))