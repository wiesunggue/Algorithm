"""
약수의 개수와 약수의 합
=======================

양의 정수 n의 양의 약수 개수를 tau(n), 양의 약수의 합을 sigma(n)이라고
한다.

예시:
    12의 약수 = 1, 2, 3, 4, 6, 12
    tau(12) = 6
    sigma(12) = 28


1. 소인수분해를 이용한 약수의 개수
----------------------------------
n을 다음과 같이 소인수분해했다고 하자.

    n = p1^a1 * p2^a2 * ... * pk^ak

n의 약수는 각 소인수 pi의 지수를 0부터 ai까지 선택해서 만든다.
각 지수 선택은 서로 독립이므로 곱의 법칙에 따라:

    tau(n) = (a1 + 1)(a2 + 1)...(ak + 1)

예시:
    12 = 2^2 * 3^1
    tau(12) = (2 + 1)(1 + 1) = 6


2. 소인수분해를 이용한 약수의 합
--------------------------------
각 소인수에서 선택할 수 있는 거듭제곱의 합을 모두 곱한다.

    sigma(n)
    = (1 + p1 + p1^2 + ... + p1^a1)
      * ...
      * (1 + pk + pk^2 + ... + pk^ak)

등비수열의 합 공식을 사용하면:

    sigma(n) = product((pi^(ai + 1) - 1) / (pi - 1))

정수 연산에서는 나눗셈 오차를 피하기 위해 거듭제곱을 직접 더하거나
분자가 정확히 나누어지는 것을 이용해 정수 나눗셈을 사용한다.

예시:
    12 = 2^2 * 3
    sigma(12) = (1 + 2 + 4)(1 + 3) = 7 * 4 = 28


3. O(sqrt(n)) 약수 쌍 탐색
--------------------------
d가 n의 약수이면 n // d도 약수이다. 따라서 1부터 sqrt(n)까지만 확인해
약수 쌍 (d, n // d)을 한 번에 처리할 수 있다.

n이 완전제곱수이면 sqrt(n)가 자기 자신과 짝을 이루므로 한 번만 세어야
한다.

소인수분해 없이 한 수의 약수 개수와 합만 필요할 때 간단한 방법이다.

시간 복잡도: O(sqrt(n))
공간 복잡도: O(1)


4. 진약수와 완전수
------------------
진약수는 자기 자신을 제외한 양의 약수이다.

    진약수의 합 = sigma(n) - n

완전수:
    진약수의 합이 자기 자신과 같은 수
    sigma(n) - n = n, 즉 sigma(n) = 2n

예시:
    6의 진약수는 1, 2, 3이고 합은 6이므로 6은 완전수이다.


5. 1부터 N까지 모든 약수 합의 누적
-----------------------------------
다음 값을 구한다고 하자.

    sigma(1) + sigma(2) + ... + sigma(N)

약수 d는 d, 2d, 3d, ..., floor(N / d)d에 총 floor(N / d)번 등장한다.
따라서 각 약수의 기여도를 더하면:

    sum(sigma(k), 1 <= k <= N)
    = sum(d * floor(N / d), 1 <= d <= N)

이 공식은 O(N)에 계산할 수 있다.

여러 N에 대한 질의가 있고 최댓값이 충분히 작다면:
    1) 배수 순회로 모든 sigma(n)을 전처리한다.
    2) sigma의 누적 합을 만든다.
    3) 각 질의에 O(1)로 답한다.

전처리 시간 복잡도: O(N log N)
공간 복잡도: O(N)


6. 특수한 값과 주의점
---------------------
- 1의 양의 약수는 1 하나이므로 tau(1) = 1, sigma(1) = 1이다.
- 약수 문제에서 보통 양의 약수만 다룬다.
- 완전제곱수의 제곱근을 두 번 세지 않는다.
- 진약수 합에서는 자기 자신 n을 제외한다.
- sigma(n)과 1부터 n까지 sigma의 누적 합을 혼동하지 않는다.
- 값이 매우 커질 수 있으므로 다른 언어에서는 64비트 정수를 확인한다.
"""

from math import isqrt


def divisor_count_and_sum(n):
    """
    소인수분해를 이용해 n의 양의 약수 개수와 합을 반환한다.

    시간 복잡도: O(sqrt(n))
    """
    if n <= 0:
        raise ValueError("n은 양의 정수여야 합니다.")

    remaining = n
    divisor_count = 1
    divisor_sum = 1
    prime = 2

    while prime * prime <= remaining:
        if remaining % prime != 0:
            prime += 1
            continue

        exponent = 0
        power = 1
        power_sum = 1

        while remaining % prime == 0:
            remaining //= prime
            exponent += 1
            power *= prime
            power_sum += power

        divisor_count *= exponent + 1
        divisor_sum *= power_sum
        prime += 1

    # sqrt(n)보다 큰 소인수가 하나 남은 경우 지수는 1이다.
    if remaining > 1:
        divisor_count *= 2
        divisor_sum *= 1 + remaining

    return divisor_count, divisor_sum


def divisor_count_and_sum_by_pairs(n):
    """약수 쌍을 직접 확인해 n의 약수 개수와 합을 반환한다."""
    if n <= 0:
        raise ValueError("n은 양의 정수여야 합니다.")

    divisor_count = 0
    divisor_sum = 0

    for divisor in range(1, isqrt(n) + 1):
        if n % divisor != 0:
            continue

        paired = n // divisor
        divisor_count += 1
        divisor_sum += divisor

        if paired != divisor:
            divisor_count += 1
            divisor_sum += paired

    return divisor_count, divisor_sum


def proper_divisor_sum(n):
    """n의 진약수 합을 반환한다."""
    return divisor_count_and_sum(n)[1] - n


def is_perfect_number(n):
    """n이 완전수인지 반환한다."""
    return n > 1 and proper_divisor_sum(n) == n


def cumulative_divisor_sum(n):
    """sigma(1) + sigma(2) + ... + sigma(n)을 O(n)에 계산한다."""
    if n < 0:
        raise ValueError("n은 음수가 될 수 없습니다.")

    return sum(divisor * (n // divisor) for divisor in range(1, n + 1))


def divisor_sum_sieve(limit):
    """0부터 limit까지 각 수의 약수 합 sigma(n)을 전처리한다."""
    if limit < 0:
        raise ValueError("limit은 음수가 될 수 없습니다.")

    sigma = [0] * (limit + 1)

    for divisor in range(1, limit + 1):
        for multiple in range(divisor, limit + 1, divisor):
            sigma[multiple] += divisor

    return sigma


def cumulative_divisor_sum_table(limit):
    """여러 질의를 위해 sigma의 누적 합 테이블을 만든다."""
    sigma = divisor_sum_sieve(limit)
    prefix_sum = [0] * (limit + 1)

    for number in range(1, limit + 1):
        prefix_sum[number] = prefix_sum[number - 1] + sigma[number]

    return prefix_sum
