# https://www.acmicpc.net/problem/19583
# 백준 19583 싸이버 개강총회
from collections import defaultdict
def conv(x):
    a,b = map(int,x.split(":"))
    return a*60+b

bef, start, end = map(conv,input().split())
ans = defaultdict(int)
while True:
    s = input()
    if s=='':
        break
    time, name = s.split()
    time = conv(time)
    if time<=bef:
        ans[name] = 1

    if start<=time<=end and ans[name] == 1:
        ans[name] = 2

cnt = 0
for k in ans:
    if ans[k] == 2:
        cnt += 1
print(cnt)