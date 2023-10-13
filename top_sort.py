import sys
sys.setrecursionlimit(10**6)
rinput = sys.stdin.readline


def find_dp(target):
    if ans.get(target)!=None:
        return ans[target]
    if len(rnode[target]) == 0:
        ans[target] = build_time[target-1]
        return build_time[target - 1]
    m = 0
    for i in rnode[target]:
        m = max(m, find_dp(i) + build_time[target - 1])
    ans[target]=m
    return ans[target]


T = 1
for t in range(T):
    N, K = map(int, rinput().split())
    build_time = [int(input()) for i in range(N)]
    node = [[] for i in range(N+1)]
    rnode = [[] for i in range(N + 1)]
    visit = [0] * (N + 1)
    for i in range(K):
        a, b = map(int, rinput().split())
        rnode[b].append(a)
        node[a].append(b)
    2
    ans = {}
    m=0
    for i in range(1,N+1):
        m = max(m,find_dp(i))
    print(m)