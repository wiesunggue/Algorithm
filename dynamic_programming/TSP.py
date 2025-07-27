# https://www.acmicpc.net/problem/2098
# 백준 외판원 순회 문제

# N개의 도시르 모두 거쳐서 원래 도시로 최소비용으로 돌아오는 방법(중복 방문 금지)
# A->B의 비용과 B->A의 비용이 다름
# 1. 조기 종료
# 2. 탐색 순서 변화(그리디한 탐색)
# 3. 간단한 휴리스틱(낙관적인 탐색- 가장 먼곳까지 더했을 때 최적해보다 크다면 조기종료)
# 4. 지나온 경로에 대한 가지치기(인접한 두 경로를 바꾸기)
# 5. 마지막 단계 메모이제이션 하기(일부 결과 저장)

N = int(input())
CostMatrix = [list(map(int,input().split())) for i in range(N)]
Dp = []
Visit = 0
Cost = 10**10

minCost = 10**10
for i in range(N):
    for j in range(N):
        if CostMatrix[i][j] != 0:
            minCost = min(minCost,CostMatrix[i][j])
        else:
            CostMatrix[i][j] = 10**10

def Search(before,node,c,count,s,visit):
    global Cost, Dp
    # 시작 도시 선택
    if node == -1:
        for start in range(N):
            Search(-1,start,0,1,start, visit | 1<<start)

    # 알려진 최소 비용보다 커지는 경우 탐색 중지
    if Cost <= c:
        return

    # 비용의 최솟값을 남은 거리에 곱해서 알려진 최솟값보다 크다면 탐색 종료
    if Cost <= c + (N-visit.bit_count()+1)*minCost:
        return

    # 모든 노드에 방문 완료한 경우
    if count == N:
        print(count,Cost)
        if CostMatrix[node][s] != 10**10: # 시작노드로 방문 가능한 경우만 값 업데이트
            Cost = min(Cost,c+CostMatrix[node][s])
        return
    
    # 재귀 탐색
    for i in range(N):
        if not (visit & 1 << i)  and CostMatrix[node][i] != 10**10:

            # 휴리스틱 방문 노드 변경하기
            # 현재 노드 node 다음 노드 i
            # i 방문 후 node 방문할 때 cost가 더 감소하면 탐색하지 않는다

            convertCost = c - CostMatrix[before][node]
            convertCost += CostMatrix[before][i] + CostMatrix[i][node]
            if before != -1 and convertCost < c+CostMatrix[node][i]:
                return

            Search(before,i,c+CostMatrix[node][i],count+1,s,visit | 1<<i)

Search(-1,-1,0,0,0,0)
print(Cost)