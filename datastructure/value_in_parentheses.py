# https://www.acmicpc.net/problem/2504
# 백준 2504번 괄호의 값

from collections import deque

s = input()
ans = deque()
dq = deque(['']*40) # 버퍼 용량 확보하기(저장되지 않은 상태에서 삭제 시도 방지)
def calculation(s):
    # 판단해야 하는 경우 4가지
    # ')'를 만나는 경우 -> '('를 만나서 2를 만든다(A) or '('를 만나기 전에 많은 숫자가 들어있어서 더하고 2를 곱한다.(B)
    # ']'를 만나는 경우 -> '['를 만나서 3을 만든다(C) or '['를 만나기 전에 많은 숫자가 들어있어서 더하고 3을 곱한다.(D)
    ans = deque(s[0])
    for i in range(1,len(s)):
        if s[i]==')':
            if s[i-1]=='(': # case: A
                ans.pop()
                ans.append(2)
            else: # case: B
                cnt=0
                while ans[-1]!='(':
                    cnt+=ans.pop()
                ans.pop()
                ans.append(cnt*2)
        elif s[i]==']':
            if s[i-1]=='[': # case: C
                ans.pop()
                ans.append(3)
            else: # case: D
                cnt=0
                while ans[-1]!='[':
                    cnt+=ans.pop()
                ans.pop()
                ans.append(cnt*3)
        else:
            ans.append(s[i])
    return sum(ans)

# 옳은 문제인지 판단하기
for i in range(len(s)):
    if s[i]==')' and dq[-1] =='(':
        dq.pop()
    elif s[i]==']' and dq[-1] == '[':
        dq.pop()
    else:
        dq.append(s[i])

if len(dq)==40:
    print(calculation(s))
else:
    print(0)