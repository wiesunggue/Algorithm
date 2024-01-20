# https://www.acmicpc.net/problem/15961
# 백준 15961번 회전초밥 문제

import sys
input = sys.stdin.readline

N,d,k,c = map(int,input().split())
arr = [int(input()) for i in range(N)]
state_table = [0]*(d+1)
state_table[c] = -10*10
idx = k
cases = 0
ans = 0
for i in range(k):
    state_table[arr[i%N]]+=1
    cases += (state_table[arr[i%N]] == 1)
ans = cases
print(ans)
while idx<=N+k:
    print(state_table)
    before1, before2 = state_table[arr[idx%N]], state_table[arr[(idx-k)%N]]
    state_table[arr[idx%N]] += 1
    state_table[arr[(idx-k)%N]] -= 1
    cases += (before1==0 and state_table[arr[idx%N]]==1)-(before2==1 and state_table[arr[(idx-k)%N]]==0)
    print(cases)
    ans = max(ans,cases)
    idx += 1

print(ans+1)