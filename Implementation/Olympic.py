# https://www.acmicpc.net/problem/8979
# 백준 8979번 올림픽 문제

N,idx = map(int,input().split())
country_dict = {}
for i in range(N):
    a,*b = map(int,input().split())
    country_dict[a] = b
cnt = 1
for key in country_dict.keys():
    cnt += country_dict[key]>country_dict[idx]
print(cnt)