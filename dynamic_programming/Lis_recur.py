# LIS를 재귀로도 풀 수 있다?!

N = int(input())
arr = list(map(int,input().split()))
cache = [-1] * (N+1)

def lis(start):
    '''재귀를 이용한 LIS'''
    if cache[start] != -1:
        return cache[start]
    ans = 1
    for i in range(start+1,N):
        if arr[start]<arr[i]:
            ans = max(ans,lis(i)+1)
    cache[start] = ans
    return ans

# 재귀 LIS에서는 start 지점을 반드시 지정해주어야 하기 때문에 가능한 최솟값보다 작은 0을 추가
# 0 10 20 10 30 20 50 -> 0 10 20 30 50(반드시 0이 포함되도록 하여 LIS의 길이에 1을 추가된다.)
arr = [0]+arr
N = len(arr)
print(lis(0)-1)