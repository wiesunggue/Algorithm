# https://www.acmicpc.net/problem/23291
# 어항 정리

N,K = map(int,input().split())
fish = list(map(int,input().split()))
arr = [[i]for i in range(N)]
direction = [(0,1),(0,-1),(1,0),(-1,0)]
print(fish)
generation = 0
while True:
    generation += 1
    # 1. 최소인 어항에 물고기 넣기
    min_fish = min(fish)
    for i in range(N):
        if min_fish==fish[i]:
            fish[i] += 1

    # 2. 가장 왼쪽의 어항을 오른쪽으로 쌓기
    arr[1].append(arr[0][0])
    arr[0].pop(0)
    while True:
        if arr[0] != []:
            break
        arr.pop(0)
        arr.append([])
    # 3. 2개 이상 쌓인 어항 회전하기
    fail = False
    while fail == False:
        next_arr = [[] for i in range(N)]
        before_arr = [[] for i in range(N)]

        for i in range(N):
            for j in range(len(arr[i])):
                before_arr[i].append(arr[i][j])

        for idx in range(N):
            if len(arr[idx]) <= 1:
                break
        for j in range(len(arr[0])):
            for i in range(idx - 1, -1, -1):
                next_arr[j].append(arr[i][j])
        for i in range(idx):
            arr[i] = []
        while True:
            if arr[0] != []:
                break
            arr.pop(0)
            arr.append([])
        for i in range(len(next_arr)):
            if next_arr[i] == []:
                break
            if arr[i] == []:
                fail = True
                break
            arr[i].extend(next_arr[i])
    arr = before_arr
    # 4. 물고기 조절하기
    regulate = [0] * N
    for i in range(N):
        for j in range(len(arr[i])):
            for d in range(4):
                x,y = i+direction[d][0],j+direction[d][1]
                if 0<=x<len(arr) and 0<=y<len(arr[x]):
                    if fish[arr[i][j]] > fish[arr[x][y]]:
                        regulate[arr[x][y]] += (fish[arr[i][j]]-fish[arr[x][y]])//K
                        regulate[arr[i][j]] -= (fish[arr[i][j]]-fish[arr[x][y]])//K
    for i in range(N):
        fish[i] += regulate[i]

    # 5. 일렬로 정리하기
    print('arr',arr)
    temp = [[] for i in range(N)]
    idx = 0
    for i in range(N):
        for j in arr[i]:
            temp[idx].append(j)
            idx += 1
    arr = temp

    # 6. 어항 올리기(1단)
    M = N // 2
    for i in range(M):
        for j in range(len(arr[i])):
            arr[N - i - 1].append(arr[i][j])
        arr[i] = []

    # 밀기
    while True:
        if arr[0] != []:
            break
        arr.pop(0)
        arr.append([])

    # 7. 어항 올리기(2단)
    for i in range(N // 4):
        arr[N // 2 - i - 1].extend(reversed(arr[i]))
        arr[i] = []
    # 밀기
    while True:
        if arr[0] != []:
            break
        arr.pop(0)
        arr.append([])

    # 8. 물고기 조절하기
    regulate = [0] * N
    for i in range(N):
        for j in range(len(arr[i])):
            for d in range(4):
                x,y = i+direction[d][0],j+direction[d][1]
                if 0<=x<len(arr) and 0<=y<len(arr[x]):
                    if fish[arr[i][j]] > fish[arr[x][y]]:
                        regulate[arr[x][y]] += (fish[arr[i][j]]-fish[arr[x][y]])//K
                        regulate[arr[i][j]] -= (fish[arr[i][j]]-fish[arr[x][y]])//K
    for i in range(N):
        fish[i] += regulate[i]

    # 9. 일렬로 정리하기
    temp = [[] for i in range(N)]
    idx = 0
    for i in range(N):
        for j in arr[i]:
            temp[idx].append(j)
            idx += 1

    arr = temp

    # 어항 정리 끝
    if max(fish)-min(fish)<=K:
        break

print(generation)

print(fish)
print(arr)

for i in range(N):
    print(fish[arr[i][0]],end=' ')