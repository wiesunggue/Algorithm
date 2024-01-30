# https://www.acmicpc.net/problem/10994
# 백준 10994번 별 찍기 19

N = int(input())
arr = [[' ']*(4*N-3) for i in range(4*N-3)]
mid = 2*N-1

def recur(x):
    if x==N+1:
        return
    for i in range(4*x-3):
        arr[mid-2*x+1][mid-2*x+1+i]='*'
        arr[mid+2*x-3][mid-2*x+1+i]='*'
        arr[mid-2*x+1+i][mid-2*x+1]='*'
        arr[mid-2*x+1+i][mid+2*x-3]='*'
    recur(x+1)

recur(1)

for i in range(4*N-3):
    print(''.join(arr[i]))