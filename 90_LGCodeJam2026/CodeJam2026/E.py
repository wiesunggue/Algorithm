N = int(input())
arr = list(map(int, input().split()))

MAX_SIZE = 998244353

dp = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    dp[i][arr[i]] = 1
    for j in range(N):
        dp[i]



print(dp)
print(sum(dp))

# 모든 1<=i<j<k<=X 에 대해서 Xj>max(Xi,Xk) or Xj<max(Xi,Xk)를 만족하는 부분 수열을 좋은 수열이라고 할 때 좋은 수열의 개수를 구하기
# N = 5000, 1 <= Ai <= 5000

'''
6
1 3 5 6 2 4
ans 38

10
1 3 9 2 6 4 5 8 7 10

3
1 3 5
122
'''

