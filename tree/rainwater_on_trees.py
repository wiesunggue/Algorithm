# https://www.acmicpc.net/problem/17073
# 백준 17073번 나무 위의 빗물

# 모든 빗발울은 항상 종단 노드로 가게 되고
# 그것의 각 노드에 기대되는 평균을 계산하고 평균이 0 이상인 노드의 평균을 계산하면
# 1. 종단 노드가 아니면 평균이 0이다.
# 2. 종단 노드의 빗물 총 합은 초기 빗물과 같다.
# 3. 평균이 0 이상인 노드의 평균은 초기 빗물/종단 노드의 수가 된다

# 데이터 입력받기
import sys
input = sys.stdin.readline
N,W = map(int,input().split())
arr = [0]*(N+1)
visit = [0]*(N+1)
for i in range(N-1):
    x,y = map(int,input().split())
    arr[x]+=1
    arr[y]+=1

print(W/arr[2:].count(1)) # 종단 노드는 1개의 간선만 존재한다