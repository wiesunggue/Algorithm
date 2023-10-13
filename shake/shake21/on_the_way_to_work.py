# https://www.acmicpc.net/problem/24229
# 모두싸인 출근길 문제
import sys
input = sys.stdin.readline
from collections import deque
# 많이 가는게 정답
# 하지만 적게 점프하는 것이 정답이 될 수가 있음
# 그렇다면 점프해서 밟을 수 있는 발판에 대해서 모두 탐색해야 함
# 하지만 "가능한" 발판에는 같은 발판에서 시작하는 것을 의미하는 것이 아니라 발판의 시작점으로 가는 것을 의미

N = int(input())
arr = [list(map(int,input().split()))+[0] for i in range(N)]
arr.sort()

# 발판 합치기
# 시작점 <= 이전의 끝점이라면 합칠 수 있다. => 근데 합치는 것 보다 누적시키는 것이 더 이득이다.(새 배열 형성하는데 많은 시간복잡도)
idx=arr[0][1]
before=arr[0][0]
arr[0][2]=1
ans=idx
sarr = []
dq = deque()
for i in range(N):
    if idx>=arr[i][0]:
        idx = max(idx,arr[i][1])
    else:
        sarr.append([before,idx])
        idx=arr[i][1]
        before=arr[i][0]
sarr.append([before,idx])
visit = [0]*len(sarr)
print(sarr)
sans=0
dq.append(0)
while dq:
    print(dq)
    idx = dq.popleft()
    if visit[idx]==1:
        continue
    visit[idx]=1
    jump = sarr[idx][1]-sarr[idx][0]
    for i in range(idx+1,len(sarr)):
        if jump>=sarr[i][0]-sarr[idx][1]:
            print('idx',i)
            dq.append(i)
            sans = max(sans,sarr[i][1])
        else:
            break
print(sans)
print("*"*50)
idx=arr[0][1]
before=arr[0][0]
arr[0][2]=1
ans=idx
for i in range(N):
    print('iteration *',i)
    if idx>=arr[i][0]:
        idx = max(idx,arr[i][1])
        arr[i][2]=1
        ans = idx
    else:
        jump = idx-before
        print('jump',jump)
        j=i
        while j<N:
            if jump<(arr[j][0]-arr[i-1][1]):
                break
            print('j',j,arr[j][0],arr[i-1][1])
            ans = max(arr[j - 1][1], ans)
            arr[j][2]=1
            j+=1
        idx=arr[i][1]
        before=arr[i][0]
    if arr[i][2]==0:
        break
    ans = max(arr[i][1],ans)

if arr[0][0] != 0:
    print(0)
else:
    print(ans)