from collections import deque
N = int(input())
M = int(input())
arr = [[0 for i in range(N)] for j in range(N)]
for i in range(M):
    i,j = map(int,input().split())
    arr[j-1][i-1] = 1

direction = [(-1,0),(1,0),(0,-1),(0,1)]
rotation = [[3,2],[2,3],[0,1],[1,0]]
L = int(input())
moveDict = {}
for i in range(L):
    a,b = input().split()
    moveDict[int(a)] = b
dq = deque()
dq.append((0,0,1))
def rotate(d,command):
    if command=='L':
        return rotation[d][0]
    else:
        return rotation[d][1]
stop = False
for t in range(10111):
    print(t,dq)
    if moveDict.get(t) == None:
        i,j,d = dq[-1]
    else:
        com = moveDict[t]
        d = rotate(d,com)

    x, y = direction[d]
    i += x
    j += y
    if i<0 or i>=N or j<0 or j>=N:
        stop=True
    for a,b,_ in dq:
        if a==i and b==j:
            stop=True
            break
    if stop:
        break
    dq.append((i, j, d))
    if arr[i][j] == 0:
        dq.popleft()
    else:
        arr[i][j] = 0
print(t+1)