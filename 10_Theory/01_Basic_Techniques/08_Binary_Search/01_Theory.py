"""
이분 탐색(Binary Search)
========================

정렬된 탐색 공간에서 중간값을 기준으로 후보를 절반씩 제거한다.
원소 검색뿐 아니라 정답의 범위가 단조성을 가질 때 최솟값/최댓값을
찾는 결정 문제에도 사용한다.

1. 원소 검색
------------
구간을 [left, right)로 관리하면 빈 구간이 left == right로 표현되어
경계 처리가 단순하다.

- arr[mid] < target: 정답은 mid 오른쪽에 있다.
- 그 외: mid도 후보이므로 right = mid

lower_bound:
    target 이상인 첫 위치

upper_bound:
    target보다 큰 첫 위치

target의 개수:
    upper_bound(target) - lower_bound(target)

시간 복잡도: O(log N)

2. 매개변수 탐색
----------------
정답 후보 x에 대한 판정 함수 possible(x)가 다음처럼 단조적일 때 쓴다.

    False False False True True True

이 경우 첫 True를 찾을 수 있다. 반대로 True ... False라면 마지막 True를
찾을 수 있다. 핵심은 최적화 문제를 O(1) 또는 O(N)의 결정 문제로 바꾸는
것이다.

3. 실수하기 쉬운 점
-------------------
- 데이터 정렬 여부를 확인한다.
- 닫힌 구간 [l, r]과 반열린 구간 [l, r)을 섞지 않는다.
- mid = (left + right) // 2로 계산한다.
- 갱신 때 탐색 구간이 반드시 줄어야 무한 반복하지 않는다.
- 실수 탐색은 반복 횟수 또는 오차 허용 범위를 종료 조건으로 사용한다.
"""


def lower_bound(arr, target):
    """정렬된 arr에서 target 이상인 첫 인덱스를 반환한다."""
    left, right = 0, len(arr)

    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left


def upper_bound(arr, target):
    """정렬된 arr에서 target보다 큰 첫 인덱스를 반환한다."""
    left, right = 0, len(arr)

    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid

    return left


def binary_search(arr, target):
    """target의 인덱스를 반환하고, 없으면 -1을 반환한다."""
    index = lower_bound(arr, target)
    return index if index < len(arr) and arr[index] == target else -1


def first_true(left, right, possible):
    """[left, right]에서 possible(x)가 처음 True가 되는 x를 찾는다."""
    answer = right + 1

    while left <= right:
        mid = (left + right) // 2
        if possible(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer
