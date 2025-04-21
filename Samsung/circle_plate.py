# https://www.acmicpc.net/problem/17822
# 원판 돌리기

N,M,T = map(int,input().split())
arr = [list(map(int,input().split())) for i in range(N)]

for i in range(T):
    x,d,k = map(int,input().split())
    multi = 1
    # 회전 시키기
    while multi*x<=N:
        nx = multi*x-1
        temp = []

        if d == 1: # 시계
            for j in range(M):
                temp.append(arr[nx][(k+j)%M])
        else: # 반시계
            temp = arr[nx][M-k:]+arr[nx][:M-k]
        multi += 1

        arr[nx] = temp
    print(i,"회전 직후")
    print(*arr,sep='\n')

    same = []
    # 큰 수 찾기
    isFind = False
    for t in range(N):
        for j in range(M):
            if arr[t][j] == -1:
                continue
            # 왼쪽
            if arr[t][(j-1)%M] == arr[t][j]:
                same.append((t,(j-1)%M))
                same.append((t,j))
                isFind = True
            # 오른쪽
            if arr[t][(j+1)%M] == arr[t][j]:
                same.append((t,(j+1)%M))
                same.append((t,j))
                isFind = True

            # 안쪽
            if t-1>=0 and arr[t-1][j] == arr[t][j]:
                same.append((t-1,j))
                same.append((t,j))
                isFind = True

            # 바깥쪽
            if t+1<N and arr[t+1][j] == arr[t][j]:
                same.append((t + 1, j))
                same.append((t, j))
                isFind = True
    print(same)
    # 지우기
    for a,b in same:
        arr[a][b] = -1

    if not isFind:
        s = 0
        c = N*M
        for j in range(N):
            s += sum(filter(lambda a:a>=0,arr[j]))
            c -= arr[j].count(-1)
        if c==0:
            continue
        m = s/c
        for t in range(N):
            for j in range(M):
                if arr[t][j] != -1:
                    if arr[t][j] > m:
                        arr[t][j] -= 1
                    elif arr[t][j] < m:
                        arr[t][j] += 1
    print(i,"삭제 직후")
    print(*arr,sep='\n')
ans = 0
for i in range(N):
    ans += sum(filter(lambda x:x>=0,arr[i]))

print(ans)