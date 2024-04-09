# https://www.acmicpc.net/problem/4659
# 백준 4659번 비밀번호 말하기 문제

type = ['a','e','i','o','u']
def check1(s):##
    for idx in range(len(s)):
        if s[idx] in type:
            return True
    return False
def check2(s):
    cnt1 = 0
    cnt2 = 0
    for idx in range(len(s)):
        if s[idx] in type:
            cnt1 += 1
            cnt2 = 0
        else:
            cnt1 = 0
            cnt2 += 1
        if cnt1==3 or cnt2==3:
            return False
    return True

def check3(s):
    for idx in range(1,len(s)):
        if s[idx]==s[idx-1] and s[idx] not in ['e','o']:
            return False
    return True

while True:
    s = input()
    if s=='end':
        break
    if check1(s)*check2(s)*check3(s):
        print(f'<{s}> is acceptable.')
    else:
        print(f'<{s}> is not acceptable.')
