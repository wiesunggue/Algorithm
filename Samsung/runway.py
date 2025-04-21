# https://www.acmicpc.net/problem/14890
# 경사로

N,L = map(int,input().split())
arr = [list(map(int,input().split())) for i in range(N)]
visit = [[0]*N for i in range(N)]
ans = 0
for i in range(N):
    cnt = 0
    able = True

    # 불가능한 경우
    before = arr[i][0]
    for j in range(N):
        if abs(before-arr[i][j])>=2:
            able = False
            break
        before = arr[i][j]
    if able == False:
        continue
    before = arr[i][0]

    # 증가하는 방향으로 차이가 1 나는 경우
    for j in range(N):
        if before == arr[i][j]:
            cnt += 1
        elif before+1 == arr[i][j]:
            before +=1
            if cnt>=L:
                cnt = L
                while cnt!=0:
                    visit[i][j-cnt] = 1
                    cnt -= 1
                cnt = 1
            else:
                able = False
                break
        else:
            before = arr[i][j]
            cnt = 1

    # 감소하는 방향으로 차이가 1 나는 경우
    cnt = 0
    before = arr[i][-1]
    for j in range(N-1,-1,-1):
        if not able:
            break
        if before == arr[i][j]:
            cnt += 1
        elif before+1 == arr[i][j]:
            before = arr[i][j]
            if cnt>=L:
                cnt = L
                while cnt!=0:
                    if visit[i][j+cnt] == 0:
                        visit[i][j+cnt] = 1
                        cnt -= 1
                    else:
                        able = False
                        break
                cnt = 1
            else:
                able = False
                break
        else:
            before = arr[i][j]
            cnt = 1

    if able == True:
        print('i',i)
        ans += 1
print(ans)
print(*visit,sep='\n')
print()
visit = [[0]*N for i in range(N)]

for j in range(N):
    cnt = 0
    able = True

    # 불가능한 경우
    before = arr[0][j]
    for i in range(N):
        if abs(before - arr[i][j]) >= 2:
            able = False
            break
        before = arr[i][j]
    if able == False:
        continue
    before = arr[0][j]

    # 증가하는 방향으로 차이가 1 나는 경우
    for i in range(N):
        if before == arr[i][j]:
            cnt += 1
        elif before + 1 == arr[i][j]:
            before += 1
            if cnt >= L:
                cnt = L
                while cnt != 0:
                    visit[i-cnt][j] = 1
                    cnt -= 1
                cnt = 1
            else:
                able = False
                break
        else:
            before = arr[i][j]
            cnt = 1
    if j==4:
        print(*visit,sep='\n')
    # 감소하는 방향으로 차이가 1 나는 경우
    cnt = 0
    before = arr[-1][j]
    for i in range(N - 1, -1, -1):
        if not able:
            break
        if j==0:
            print("****",before,arr[i][j], i,j,cnt,)
        if before == arr[i][j]:
            cnt += 1
        elif before + 1 == arr[i][j]:
            before = arr[i][j]
            if cnt >= L:
                cnt = L
                while cnt != 0:
                    if visit[i+cnt][j] == 0:
                        visit[i+cnt][j] = 1
                        cnt -= 1
                    else:
                        able = False
                        break
                cnt = 1
            else:
                able = False
                break
        else:
            before = arr[i][j]
            cnt = 1

    if able == True:
        print('j',j)
        ans += 1

print(ans)
print(*visit,sep='\n')