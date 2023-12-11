# https://www.acmicpc.net/problem/1747
# 백준 1747번 소수&팰린드룸 문제

# 팰린드룸 2가지
# 중앙 1개 나머지 대칭
# 중앙 0개 나머지 대칭

#큰 팰린드룸을 만들어서 sqrt(N) 방식으로 소수인지 판별하자
arr = ['0','1','2','3','4','5','6','7','8','9']
def is_prime(p):
    if p<2:
        return False
    if p==2:
        return True
    i = 1
    while i*i<=p:
        i+=1
        if p%i == 0:
            return False
    return True
def is_palindrome(p):
    p = str(p)
    for i in range(len(p)):
        if p[i]!=p[-i-1]:
            return False
    return True

for k in range(int(input()),10000000):
    if is_palindrome(k):
        if is_prime(k):
            print(k)
            break

