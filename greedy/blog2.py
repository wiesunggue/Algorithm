# https://www.acmicpc.net/problem/20365
# 백준 20365번 블로그2

N = int(input())
s = input()
cnt1,cnt2 = 0, 0
for i in range(1,N):
    if s[i]=='R' and s[i-1]=='B':
        cnt1 += 1
    if s[i]=='B' and s[i-1]=='R':
        cnt2 += 1
if s[0]=='R':
    cnt1 += 1
else:
    cnt2 += 1
print(min(cnt1,cnt2)+1)