# https://www.acmicpc.net/problem/23971
# 백준 23971 ZOCA4 문제

H,W,N,M = map(int,input().split())
x,y = (H+N)//(N+1),(W+M)//(M+1)
print(x*y,x,y)