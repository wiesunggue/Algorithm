# https://www.acmicpc.net/problem/21941
# 백준 21941번 문자열 제거 문제

s = input()
N = int(input())
score = [input().split() for i in range(N)]
state = [0]*N
state_ring = [0]*N
dp = [0]*(len(s)+1)

for i in range(len(s)):
    for j in range(N):
        # state는 j번째 인덱스 기록 배열
        # score은 j번째 문자와 점수를 기록하는 배열
        print(i,j, state[j],state_ring[j])
        if score[j][0][state[j]] == s[i]:
            if score[j][0][state_ring[j]] == s[i] and state[j]!=0:
                state_ring[j] += 1
            else:
                state_ring[j] = 0
            state[j] += 1
        else:
            state[j] = 0
            state_ring[j] = 0
        if state[j] == len(score[j][0]): # 점수 문자열의 최대 길이에 도달하는 경우 업데이트
            dp[i] = max(dp[i],dp[i-state[j]]+int(score[j][1]))
            state[j] = state_ring[j]
            state_ring[j] = 0
#            state = [0]*N
    print(state)

    # 특별한 점수 문자열을 만들지 않고 1만 추가하는 경우
    dp[i] = max(dp[i],dp[i-1]+1)
print(dp[len(s)-1])

