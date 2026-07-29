N, K = map(int, input().split())
arr = list(map(int, input().split()))

psum = [0] * (N+1)
p_sqaure_sum = [0] * (N+1)

for i in range(1, N+1):
    psum[i] = psum[i - 1] + arr[i-1]
    p_sqaure_sum[i] = p_sqaure_sum[i - 1] + arr[i-1] ** 2


def check(x):
    # P[j] = sigma(a^2-Xa) 라고 할 때
    # P[j] - min(P[i]), 0 <= i <= j - K 찾기
    prefix = 0
    for r in range(K, N + 1):
        left = r-K
        p_left = p_sqaure_sum[left] - x * psum[left]
        prefix = min(prefix, p_left)

        p_right = p_sqaure_sum[r] - x * psum[r]
        if p_right - prefix >= 0:
            return True

    return False

s, e = 1, 1000000
m = 0
for i in range(60):
    m = (s+e)/2
    if check(m):
        s = m
    else:
        e = m

print(m)