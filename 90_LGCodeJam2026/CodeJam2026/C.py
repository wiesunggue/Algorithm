N = int(input())
position = []
for i in range(N):
    a, b, w = map(int, input().split())
    position.append((a, b, w))
date = list(map(int, input().split()))

# N = 10만
# A, B, C가 주어질 때
## W * (|A - C| + |B - C|)
## 비용이 최소가 되도록 A와 C를 모두 연결할 때
# 가장 비싼 연결은?
