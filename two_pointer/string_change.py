# https://www.acmicpc.net/problem/1522
# 백준 1522번 문자열 교환 문제

def solution():
    s = input()
    ans = len(s)
    start,end = -s.count('a'),-1
    exchange = s[start:].count('b')
    print(start,end,exchange)
    while end<len(s)-1:
        exchange -= s[start] == 'b'
        start += 1
        end += 1
        exchange += s[end]=='b'
        ans = min(ans,exchange)
        print(start,end,exchange)
    print(ans if s.count(a)!=0 else 0)

if __name__ == '__main__':
    solution()