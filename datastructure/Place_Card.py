# https://www.acmicpc.net/problem/18115
# 백준 18115 카드 놓기
from collections import deque

N = int(input())
dq = deque(list(range(1,N+1)))
ans = deque()
arr = list(reversed(list(map(int,input().split()))))

for com in arr:
    if com == 1:
        ans.appendleft(dq.popleft())
    elif com == 2:
        temp = ans.popleft()
        ans.appendleft(dq.popleft())
        ans.appendleft(temp)
    else:
        ans.append(dq.popleft())

print(*ans,sep=' ')

# 1번 연산 맨 위의 카드 삭제
# 2번 연산 맨 위의 2번째 카드 삭제
# 3번 맨 아래 카드 삭제
# 3가지 연산 다 맨 위에 추가됨 -> dq의 popleft만 사용할 것