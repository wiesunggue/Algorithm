import sys
import bisect
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    a,b = map(int, input().split())
    arr.append((min(a,b),max(a,b)))
# 비감소인 부분수열을 만드는 최소 분할의 개수를 구하는 문제
# => 엄격 감소의 최대길이 구하기 = LIS 구하기

# [10, 5, 7, 2] 이면
# 비감소 부분수열의 최대 분할 len([10], [5, 7], [2]) = 3
# 엄격 감소의 최대 길이 len([10, 5, 2]) = 3
arr.sort(key = lambda x: (x[0], x[1]))
print(*arr, sep ='\n')

def LIS():
    # tails[k] = 길이가 k+1인 증가 부분수열 중 최소 끝값
    tails =[]
    for i in range(N):
        idx = bisect.bisect_left(tails, -arr[i][1])

        if idx == len(tails):
            tails.append(-arr[i][1])
        else:
            tails[idx] = -arr[i][1]

    return tails

print(len(LIS()))