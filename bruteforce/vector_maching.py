from itertools import combinations
from math import sqrt
def dist(v1,v2):
    return sqrt((v1[0]-v2[0])**2+(v1[1]-v2[1])**2)
# 20C10 * 2**10
# = 20만 * 1024 => 2억번 연산
# 2개의 집합으로 나누고
# v와 -v를 고려해야 함
# 부호를 정하면 전부 더한 결과를 출력해야
# 20
N = int(input())
arr=[list(map(int,input().split()))for i in range(N)]
let = list(combinations(arr,N//2))
def chk_all(a,b):
    for i in range(2**len(a)):
        for j in range(len(a)):
            a[j]-b[j]
for i in let:
    print(i)