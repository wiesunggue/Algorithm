# https://algospot.com/judge/problem/read/POLY
# 알고스팟 폴리오미노 문제

#정사각형들의 변들을 서로 완전하게 붙여 만든 도형들을 폴리오미노(Polyomino)라고 부릅니다.
# n개의 정사각형으로 구성된 폴리오미노들을 만들려고하는데,
# 이 중 세로로 단조(monotone)인 폴리오미노의 수가 몇 개나 되는지 세고 싶습니다.
# 세로로 단조라는 말은 어떤 가로줄도 폴리오미노를 두 번 이상 교차하지 않는다는 뜻입니다.

# N각형으로 이루어진 폴리오미노의 개수를 구하라(N은 100이하)
# 10000000이상인 경우 10000000으로 나눈 나머지를 출력하라

MOD = 10000000
N = 92
dp = [[-1]*101 for i in range(101)]
def poly(n,first):
    if n==first: return 1
    if dp[n][first]!= -1:
        return dp[n][first]
    ret = 0
    for second in range(1,n-first+1):
        if first == 0:
            ret += poly(n-first,second)
        else:
            ret += poly(n-first,second)*(first+second-1)%MOD
        ret %= MOD
    dp[n][first] = ret
    return ret

print(poly(N,0))
