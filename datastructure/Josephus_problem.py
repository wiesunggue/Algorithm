# https://www.acmicpc.net/problem/1158
# 데이터 구조 기본 문제
# 요세푸스 문제
from collections import deque

import sys
input = sys.stdin.readline
N,K = map(int,input().split())
dq = deque()
ans = deque()
# N명 추가
for i in range(N):
    dq.append(str(i+1))


for i in range(N):
    # K번째 사람 제거하기
    for j in range(K-1):
        dq.append(dq.popleft())
    ans.append(dq.popleft()) # 마지막은 아예 삭제해버린다.

print('<'+', '.join(ans)+'>')