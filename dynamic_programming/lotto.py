# https://www.acmicpc.net/problem/2758
# 백준 2758번 로또 문제
def solution():
    N, M = map(int, input().split())

    # 절대로 로또를 구매하지 못하는 경우
    if 2**(N-1)>M:
        return 0

    dp = [[0]*N for i in range(M)] #dp[N][M]
    dp

T = int(input())

for test in range(T):
    print(solution())