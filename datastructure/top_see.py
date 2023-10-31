# https://www.acmicpc.net/problem/22866
# 백준 22866번 탑 보기
from collections import deque

N = int(input())
arr = list(map(int,input().split()))

ans = [0]*N
pos = [-10**10]*N
# 높은 것이 아니라 작은것을 보도록 한다.
# 낮아지는 것으로 역순으로 스택에 넣는다.
# 높은걸 만날 때까지 스택에서 제거하고 스택에 쌓인 개수를 추정
# 양쪽에서 볼 수 있어야 하므로 왼쪽에서 훑고 오른쪽에서 훑는다.

# 덱 생성 및 초기값 저장
dq = deque()
dq.append((10**10, -10**10))
dq.append((arr[0], 1))
cnt = 1
def posif(l,m,r):
    if abs(l-m)<=abs(r-m):
        return l
    else:
        return r
# 왼쪽에서 훑기
for i in range(1,N):
    if dq[-1][0] > arr[i]:
        ans[i] += cnt
        pos[i] = dq[-1][1]
        dq.append((arr[i],i+1))
        cnt += 1
    else:
        while dq[-1][0] <= arr[i]:
            dq.pop()
            cnt -= 1
        ans[i] += cnt
        pos[i] = dq[-1][1]
        dq.append((arr[i],i+1))
        cnt += 1

# 덱 초기화
dq = deque()
dq.append((10**10,-10**10))
dq.append((arr[-1],N))
cnt = 1

# 오른쪽에서 훑기
for i in range(N-2,-1,-1):
    if dq[-1][0] > arr[i]:
        ans[i] += cnt
        pos[i] = posif(pos[i],i+1,dq[-1][1])
        dq.append((arr[i],i+1))
        cnt += 1
    else:
        while dq[-1][0] <= arr[i]:
            dq.pop()
            cnt -= 1
        ans[i] += cnt
        pos[i] = posif(pos[i],i+1,dq[-1][1])
        dq.append((arr[i],i+1))
        cnt += 1

for i in range(N):
    print(ans[i],end='')
    if ans[i]!=0:
        print('',pos[i])
    else:
        print()