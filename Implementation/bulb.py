# https://www.acmicpc.net/problem/21918
# 백준 21918번 전구 문제
import sys
input = sys.stdin.readline
print = sys.stdout.write
def f1(i,x):
    bulb[i-1]=str(x)
def f2(l,r):
    for i in range(l-1,r):
        bulb[i]= '1' if bulb[i]=='0' else '0'
def f3(l,r):
    bulb[l-1:r] = ['0']*(r-l+1)

def f4(l,r):
    bulb[l-1:r] = ['1']*(r-l+1)
d = {1:f1,2:f2,3:f3,4:f4}
N,M = map(int,input().split())

bulb = input().split()
for i in range(M):
    c,l,r = map(int,input().split())
    d[c](l,r)

for i in range(N):
    print(str(bulb[i])+" ")