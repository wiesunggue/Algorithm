import sys
input = sys.stdin.readline


# i번째 경기 = 2i-1와 2i가 가 치룸
# i번째 선수는 이미 A_i번 승리
# 모든 경기가 끝난 뒤 가장 많은 승수를 가진 선수 중 챔피언을 랜덤 추출

MAX = 998244353
DIV = 259959467

N = int(input())
arr = []
for i in range(N):
    A,B = map(int, input().split())
    arr.append(A)
    arr.append(B)

m = max(arr)

# 경우는 2가지
# 1. arr 최댓값 + 1이 우승하는 경우
# 2. arr의 최댓값이 우승하는 경우
