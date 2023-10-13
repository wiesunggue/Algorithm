arr = [list(map(int,list(input())))for i in range(9)]
zero=[]
stop=False
for i in range(9):
    for j in range(9):
        if arr[i][j]==0:
            zero.append((i,j))
def chk(x,y,s):
    for i in range(9):
        if arr[x][i]==s:
            return False
        if arr[i][y]==s:
            return False
    a,b=x//3*3,y//3*3
    for i in range(a,a+3):
        for j in range(b,b+3):
            if arr[i][j]==s:
                return False
    return True

def back2(x,y,k):
    x,y,k
    global stop
    if stop==True:
        return
    for i in range(1,10):
        if chk(x,y,i):
            arr[x][y]=i
            if k==len(zero):
                stop=True
                return

            back2(*zero[k],k+1)
            if stop!=True:
                arr[x][y]=0
back2(*zero[0],1)
for i in range(9):
    print(*arr[i],sep='')
