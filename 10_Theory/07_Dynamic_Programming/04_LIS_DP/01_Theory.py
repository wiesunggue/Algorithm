"""
LIS(Longest Increasing Subsequence, 최장 증가 부분 수열)
=====================================================

1. 정의
-------
수열에서 일부 원소를 원래 순서대로 골랐을 때, 값이 엄격하게 증가하는
부분 수열 중 가장 긴 것을 LIS라고 한다.

예시:
    수열: [10, 20, 10, 30, 20, 50]
    LIS : [10, 20, 30, 50]
    길이: 4

부분 수열(subsequence)은 원소가 연속할 필요는 없지만 원래 순서는
바꿀 수 없다. 부분 배열(subarray)과 혼동하지 않아야 한다.


2. O(N^2) DP
------------
상태:
    dp[i] = i번째 원소를 마지막 원소로 사용하는 LIS의 길이

점화식:
    dp[i] = 1 + max(dp[j])
            단, 0 <= j < i 이고 arr[j] < arr[i]

앞에 연결할 수 있는 원소가 없다면 dp[i] = 1이다.
전체 LIS 길이는 max(dp)이다.

시간 복잡도: O(N^2)
공간 복잡도: O(N)

이 방법은 상태와 점화식이 명확하고, 이전 인덱스를 기록하면 실제 LIS도
쉽게 복원할 수 있다. N이 작을 때 가장 직관적인 풀이이다.


3. O(N log N) 이분 탐색
-----------------------
tails[k]를 "길이가 k + 1인 증가 부분 수열이 가질 수 있는 가장 작은
마지막 값"으로 관리한다.

각 값 x에 대해:
    1) tails에서 x 이상인 첫 위치(lower_bound)를 찾는다.
    2) 그런 위치가 있으면 그 값을 x로 교체한다.
    3) 없다면 x를 tails 끝에 추가한다.

마지막 값을 가능한 작게 유지하면 뒤의 값이 연결될 가능성이 커진다.
따라서 모든 원소를 처리한 뒤 tails의 길이가 LIS의 길이가 된다.

주의:
    tails 자체가 원래 수열의 LIS인 것은 아니다.
    tails는 LIS의 길이를 구하기 위한 최소 꼬리값 정보이다.
    실제 수열을 구하려면 각 원소의 이전 인덱스를 별도로 기록해야 한다.

시간 복잡도: O(N log N)
공간 복잡도: O(N)


4. 중복 원소 처리
-----------------
엄격한 증가 LIS:
    arr[j] < arr[i]
    bisect_left 사용 (x 이상인 첫 위치)

비감소 부분 수열 LNDS(Longest Non-Decreasing Subsequence):
    arr[j] <= arr[i]
    bisect_right 사용 (x보다 큰 첫 위치)

문제에서 "증가", "오름차순", "감소하지 않는"의 의미를 정확히 확인해야
한다. 같은 값의 허용 여부에 따라 이분 탐색 함수가 달라진다.


5. 자주 나오는 변형
-------------------
- 실제 LIS 출력:
  parent 배열과 각 길이의 마지막 원소 인덱스를 기록하여 역추적한다.

- 최장 감소 부분 수열:
  모든 값에 음수를 취한 뒤 LIS를 구하거나 비교 방향을 반대로 바꾼다.

- 가장 긴 바이토닉 부분 수열:
  왼쪽에서 증가 LIS와 오른쪽에서 증가 LIS를 각각 구해 결합한다.

- 2차원 조건:
  한 기준으로 정렬한 뒤 다른 기준에 LIS를 적용한다.
  첫 기준이 같을 때의 정렬 순서가 중복 선택을 막도록 설계되어야 한다.

- 최소 제거 횟수:
  수열을 증가 상태로 만들기 위한 최소 제거 개수는 N - LIS 길이이다.


6. 실수하기 쉬운 점
-------------------
- LIS는 연속 부분 배열이 아니다.
- O(N log N) 방식에서 tails를 실제 LIS라고 생각하면 안 된다.
- 엄격한 증가인데 bisect_right를 사용하면 같은 값이 중복 포함된다.
- 빈 수열에서는 max(dp)를 호출할 수 없으므로 별도 처리한다.
- 실제 수열 복원 시 값이 아니라 원본 인덱스를 기록해야 한다.
"""

from bisect import bisect_left, bisect_right


def lis_length_quadratic(arr):
    """O(N^2) DP로 엄격한 LIS의 길이를 구한다."""
    n = len(arr)
    if n == 0:
        return 0

    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


def lis_length(arr):
    """O(N log N)으로 엄격한 LIS의 길이를 구한다."""
    tails = []

    for value in arr:
        position = bisect_left(tails, value)

        if position == len(tails):
            tails.append(value)
        else:
            tails[position] = value

    return len(tails)


def lis_sequence(arr):
    """O(N log N)으로 엄격한 LIS 하나를 복원한다."""
    n = len(arr)
    if n == 0:
        return []

    # tails_values[length - 1]:
    # 길이가 length인 증가 부분 수열의 최소 마지막 값
    tails_values = []

    # tails_indices[length - 1]:
    # 위 최소 마지막 값이 원본 수열에서 위치한 인덱스
    tails_indices = []

    # parent[i]:
    # 복원할 때 arr[i] 바로 앞에 오는 원소의 인덱스
    parent = [-1] * n

    for index, value in enumerate(arr):
        position = bisect_left(tails_values, value)

        if position > 0:
            parent[index] = tails_indices[position - 1]

        if position == len(tails_values):
            tails_values.append(value)
            tails_indices.append(index)
        else:
            tails_values[position] = value
            tails_indices[position] = index

    # 마지막 원소부터 parent를 따라가며 역순으로 복원한다.
    sequence = []
    current = tails_indices[-1]

    while current != -1:
        sequence.append(arr[current])
        current = parent[current]

    sequence.reverse()
    return sequence


def lnds_length(arr):
    """O(N log N)으로 최장 비감소 부분 수열의 길이를 구한다."""
    tails = []

    for value in arr:
        position = bisect_right(tails, value)

        if position == len(tails):
            tails.append(value)
        else:
            tails[position] = value

    return len(tails)
