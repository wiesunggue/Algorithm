"""
Knapsack DP(배낭 문제)
=====================

무게 제한이 있는 배낭에 물건을 골라 담아 가치의 합을 최대화하는
동적 계획법이다.

각 물건은 다음 두 값을 가진다.

    weight: 물건의 무게
    value : 물건의 가치

가장 기본적인 형태는 각 물건을 최대 한 번만 선택할 수 있는
0/1 Knapsack이다.


1. 상태와 점화식
----------------
N개의 물건과 최대 용량 W가 있을 때:

    dp[i][capacity]
    = 앞에서 i개 물건을 고려하고 capacity 이하를 사용했을 때 최대 가치

i번째 물건의 무게를 weight, 가치를 value라고 하면:

물건을 담지 않는 경우:
    dp[i][capacity] = dp[i - 1][capacity]

물건을 담는 경우(weight <= capacity):
    dp[i][capacity]
    = dp[i - 1][capacity - weight] + value

두 경우 중 큰 값을 선택한다.

    dp[i][capacity]
    = max(
        dp[i - 1][capacity],
        dp[i - 1][capacity - weight] + value
      )

시간 복잡도: O(NW)
공간 복잡도: O(NW)

W가 N에 비례하면 O(N^2) 수준이지만, 복잡도는 실제로 물건 수 N과
용량 W의 곱에 의해 결정된다. 값의 크기가 입력 비트 수에 비례하지 않고
용량 자체에 비례하므로 의사 다항 시간(pseudo-polynomial)이라고 한다.


2. 1차원 공간 최적화
--------------------
현재 행은 바로 이전 행만 참조하므로 dp 배열 하나만 사용할 수 있다.

    dp[capacity]
    = capacity 이하를 사용했을 때 얻을 수 있는 최대 가치

0/1 냅색에서는 capacity를 W부터 weight까지 역순으로 순회해야 한다.
정방향으로 순회하면 같은 물건으로 갱신한 값을 다시 사용하여 한 물건을
여러 번 선택하게 된다.

시간 복잡도: O(NW)
공간 복잡도: O(W)


3. 0/1 냅색과 무한 냅색의 차이
------------------------------
0/1 Knapsack:
    각 물건을 최대 한 번 사용
    capacity를 큰 값부터 작은 값으로 역순 순회

Unbounded Knapsack:
    각 물건을 여러 번 사용 가능
    capacity를 작은 값부터 큰 값으로 정방향 순회

반복문의 방향만 달라져도 문제의 의미가 완전히 달라지므로 주의한다.


4. 정확한 무게와 최대 무게
--------------------------
아래 기본 구현에서 dp[capacity]는 "capacity 이하"를 사용한 최대 가치다.
초기값을 모두 0으로 두므로 아무 물건도 고르지 않는 선택이 허용된다.

정확히 capacity만큼 채워야 하는 문제라면 도달 불가능 상태를 음의
무한대로 초기화한다.

    dp = [-INF] * (W + 1)
    dp[0] = 0

그 뒤 도달 가능한 상태에서만 전이해야 한다.


5. 가치 기준 DP
---------------
W가 매우 크지만 모든 가치의 합이 작다면 상태를 반대로 정의할 수 있다.

    dp[value] = 정확히 value의 가치를 만들기 위한 최소 무게

가치 합을 V라고 할 때:

    시간 복잡도: O(NV)
    공간 복잡도: O(V)

마지막에 dp[value] <= W인 가장 큰 value를 찾는다.


6. 자주 나오는 변형
-------------------
- 각 물건을 한 번만 사용: 0/1 Knapsack
- 각 물건을 무제한 사용: Unbounded Knapsack
- 각 물건의 사용 개수가 제한됨: Bounded Knapsack
- 정확히 용량을 채우기
- 최대 가치가 아니라 경우의 수 계산
- 두 개 이상의 제한 조건을 갖는 다차원 냅색
- 선택한 물건 목록 복원


7. 실수하기 쉬운 점
-------------------
- 0/1 냅색은 용량을 역순으로 순회한다.
- 무한 냅색은 용량을 정방향으로 순회한다.
- 무게와 가치의 입력 순서를 확인한다.
- 정확히 채우는 문제인지 용량 이하를 허용하는 문제인지 확인한다.
- 가치 합이 int 범위를 넘을 수 있으면 long long을 사용한다.
- N과 W가 모두 크면 O(NW)는 사용할 수 없다.
"""


def knapsack_2d(items, capacity_limit):
    """
    2차원 DP로 0/1 냅색의 최대 가치를 구한다.

    items: (weight, value) 쌍의 리스트
    시간 복잡도: O(NW)
    공간 복잡도: O(NW)
    """
    item_count = len(items)
    dp = [
        [0] * (capacity_limit + 1)
        for _ in range(item_count + 1)
    ]

    for item_index in range(1, item_count + 1):
        weight, value = items[item_index - 1]

        for capacity in range(capacity_limit + 1):
            # 현재 물건을 선택하지 않는 경우
            dp[item_index][capacity] = dp[item_index - 1][capacity]

            # 현재 물건을 선택하는 경우
            if weight <= capacity:
                dp[item_index][capacity] = max(
                    dp[item_index][capacity],
                    dp[item_index - 1][capacity - weight] + value,
                )

    return dp[item_count][capacity_limit]


def knapsack_1d(items, capacity_limit):
    """
    1차원 DP로 0/1 냅색의 최대 가치를 구한다.

    같은 물건을 중복 사용하지 않도록 용량을 역순으로 순회한다.
    시간 복잡도: O(NW)
    공간 복잡도: O(W)
    """
    dp = [0] * (capacity_limit + 1)

    for weight, value in items:
        for capacity in range(capacity_limit, weight - 1, -1):
            dp[capacity] = max(
                dp[capacity],
                dp[capacity - weight] + value,
            )

    return dp[capacity_limit]


def unbounded_knapsack(items, capacity_limit):
    """
    각 물건을 여러 번 선택할 수 있는 무한 냅색의 최대 가치를 구한다.

    같은 물건을 다시 사용할 수 있도록 용량을 정방향으로 순회한다.
    """
    dp = [0] * (capacity_limit + 1)

    for weight, value in items:
        for capacity in range(weight, capacity_limit + 1):
            dp[capacity] = max(
                dp[capacity],
                dp[capacity - weight] + value,
            )

    return dp[capacity_limit]


def exact_weight_knapsack(items, capacity_limit):
    """
    무게를 정확히 capacity_limit만큼 채우는 0/1 냅색의 최대 가치를 구한다.
    정확히 채울 수 없으면 None을 반환한다.
    """
    negative_infinity = float("-inf")
    dp = [negative_infinity] * (capacity_limit + 1)
    dp[0] = 0

    for weight, value in items:
        for capacity in range(capacity_limit, weight - 1, -1):
            if dp[capacity - weight] != negative_infinity:
                dp[capacity] = max(
                    dp[capacity],
                    dp[capacity - weight] + value,
                )

    if dp[capacity_limit] == negative_infinity:
        return None

    return dp[capacity_limit]
