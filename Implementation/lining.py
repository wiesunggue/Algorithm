# https://www.acmicpc.net/problem/10431
# 백준 10431번 줄세우기 문제
def solution():
    case, *arr = list(map(int,input().split()))
    cnt = 0
    i = 0
    for idx in range(1,len(arr)):
        data = arr[idx]
        for i in range(idx+1):
            if data<arr[i]:
                break
        for j in range(idx,i,-1):
            arr[j]=arr[j-1]
            cnt+=1
        if i!=idx:
            arr[i]=data

    print(case,cnt)



T = int(input())
for test in range(T):
    solution()