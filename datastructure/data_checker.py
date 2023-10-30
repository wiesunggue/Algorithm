N = int(input())
arr = [list(map(int,input().split())) for i in range(N)]

arr.sort(key = lambda x: sum(x))
print(arr)