'''
Mo's 알고리즘
대표 예제
구간에서 서로 다른 수의 개수
구간에서 같은 값 쌍의 개수
구간 최빈값 계열
구간에서 음이 아닌 가장 작은 정수는?(Mo's + sqrt decomposition 활용)
'''

import sys
from math import sqrt

input = sys.stdin.readline

def solve():
    N = int(input())
    arr = list(map(int, input().split()))

    values = sorted(set(arr))
    comp = {v: i for i, v in enumerate(values)}

    M = int(input())
    queries = []
    for idx in range(M):
        l, r = map(int, input().split())
        l -= 1
        r -= 1
        queries.append((l, r, idx))
    
    block = int(sqrt(N)) + 1

    queries.sort(key = lambda x: (x[0]//block, x[1] if (x[0]//block) %2==0 else -x[1]))

    freq = [0] * len(values)
    ans = [0] * M

    distinct = 0

    def add(x):
        nonlocal distinct
        if freq[x] == 0:
            distinct += 1
        freq[x] += 1
    
    def remove(x):
        nonlocal distinct
        freq[x] -= 1
        if freq[x] == 0:
            distinct -= 1
    cur_l = 0
    cur_r = -1

    for l, r, idx in queries:
        while cur_l > l:
            cur_l -= 1
            add(arr[cur_l])
        
        while cur_r < r:
            cur_r += 1
            add(arr[cur_r])
        
        while cur_l < l:
            remove(arr[cur_l])
            cur_l += 1
        
        while cur_r > r:
            remove(arr[cur_r])
            cur_r -= 1
        
        ans[idx] = distinct

    print('\n'.join(map(str, ans)))
