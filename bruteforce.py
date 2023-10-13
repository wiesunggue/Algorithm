import sys
rprint = sys.stdout.write
def recur(size,x,y):
    print(size,x,y)
    if size==1:
        return
    for i in range(size):
        for j in range(size-1):
            if (i+j)<size-1:
                arr[x+i][y+j]=1
        for j in range(size,size*2-1):
            if (j-i)>=size:
                arr[x+i][y+j]=1
        if x+i>size//2-1 and size>3:
            arr[x+i][y+size-1]=1
    if size==3:
        arr[x+1][y+2]=1
        arr[x][y+2]=0
        arr[x+2][y+2]=0

    recur(size//2,x,y+size//2)
    recur(size//2,x+size//2,y+size)
    recur(size//2,x+size//2,y)


def solve():
    size = int(input())
    global arr
    arr = [[0 for i in range(size*2-1)]for j in range(size)]
    #print(*arr,sep='\n')
    recur(size,0,0)
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            rprint("*" if arr[i][j]==0 else " ")
        print()
solve()