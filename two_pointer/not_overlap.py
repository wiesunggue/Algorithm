# https://www.acmicpc.net/problem/20922
# 백준 20922번 겹치는 건 싫어
import sys
from collections import Counter
input = sys.stdin.readline

N,K = map(int,input().split())
arr = list(map(int,input().split()))

state = [0] * 100001
before = 0
state[arr[before]] = 1
after = 1
ans = after-before+1
while after<N:
    print(before, after, state,arr[after])
    if state[arr[after]]<K:
        state[arr[after]] += 1
        ans = max(ans, after-before+1)
        after += 1
    else:
        state[arr[before]] -= 1
        before += 1

print(ans)