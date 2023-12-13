# https://www.acmicpc.net/problem/21758
# 백준 21758번 꿀 따기 문제

# 전략
# 1. 왼쪽에 벌 2마리 배치(한마리는 끝에,한마리는 중간에 배치할 수도 있음) -> 오른쪽 끝에 벌통 배치
# 2. 오른쪽에 벌 2마리 배치(한마리는 끝에,한마리는 중간에 배치할 수도 있음) -> 왼쪽 끝에 벌통 배치
# 3. 왼1 오1 배치(두마리 다 양쪽 끝에 배치) -> 중간에 벌통 배치

# 1,2,3의 결과 중 최댓값을 출력한다.
import sys
N = int(input())
arr = list(map(int,sys.stdin.readline().split()))

psumLeft = [arr[0]] * N
psumRight = [arr[-1]] * N
for i in range(1,N):
    psumLeft[i] = psumLeft[i - 1] + arr[i]
    psumRight[N-i-1] = psumRight[N-i] + arr[N-i-1]
ans=0
for i in range(1,N-1):
    ans = max(ans, psumLeft[i]-psumLeft[0]+psumRight[i]-psumRight[-1])# 2. 양쪽 탐색
    #print(psumLeft[i]-psumLeft[0],psumRight[i]-psumRight[-1])
psumRight.reverse()
for i in range(1,N):
    ans = max(ans, psumLeft[-1] - psumLeft[0] + psumLeft[-1] - psumLeft[i] - arr[i]) # 1.왼쪽 탐색
    print('left',psumLeft[-1] - psumLeft[0] - arr[i],psumLeft[-1] - psumLeft[i])
    ans = max(ans, psumRight[-1]-psumRight[0] + psumRight[-1] - psumRight[i] - arr[N-i-1]) # 3.오른쪽 탐색
    print('right',i,psumRight[-1]-psumRight[0] - arr[N-i-1], psumRight[-1] - psumRight[i])
print(ans)