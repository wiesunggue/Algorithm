"""
스위핑 / 라인 스위핑(Line Sweeping)
==================================

좌표나 시간을 한 방향으로 훑으면서 현재 지점에서 필요한 정보만 유지하는
기법이다. 모든 쌍을 비교하는 O(N^2) 풀이를 정렬 후 O(N log N) 또는
O(N)으로 줄이는 경우가 많다.

기본 절차:
    1) 사건(event)을 좌표 기준으로 정렬한다.
    2) 왼쪽에서 오른쪽으로 사건을 처리한다.
    3) 현재 활성 상태만 자료구조에 유지한다.

1. 구간 합치기
--------------
구간을 시작점 기준으로 정렬한다. 다음 구간의 시작점이 현재 끝점 이하라면
겹치므로 끝점을 확장하고, 아니면 현재 구간을 확정한다.

2. 이벤트 스위핑
----------------
[start, end) 구간마다 (start, +1), (end, -1)을 만들고 정렬하면 특정
시점의 활성 구간 수를 구할 수 있다.

같은 좌표의 이벤트 처리 순서는 구간 정의에 따라 달라진다.
- [start, end): 종료(-1)를 시작(+1)보다 먼저 처리
- [start, end]: 시작(+1)을 종료(-1)보다 먼저 처리

3. 활성 집합
------------
선분 교차, 가장 가까운 점 등에서는 현재 x좌표와 관련 있는 객체만 균형
트리, 힙, 세그먼트 트리 등에 유지한다. 무엇을 제거하고 어떤 기준으로
조회할지가 문제의 핵심이다.

복잡도:
    정렬 O(N log N) + 각 이벤트 처리 비용

주의:
- 닫힌 구간과 반열린 구간의 경계를 명확히 한다.
- 같은 좌표의 tie-breaking을 먼저 정한다.
- 좌표가 크면 좌표 압축을 고려한다.
- 현재 상태에서 더 이상 필요 없는 원소를 즉시 제거한다.
"""


def merge_intervals(intervals):
    """겹치거나 맞닿은 닫힌 구간들을 합친다."""
    if not intervals:
        return []

    intervals = sorted(intervals)
    merged = [list(intervals[0])]

    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])

    return [tuple(interval) for interval in merged]


def union_length(intervals):
    """반열린 구간 [start, end)의 합집합 길이를 구한다."""
    return sum(end - start for start, end in merge_intervals(intervals))


def maximum_overlap(intervals):
    """반열린 구간 [start, end)의 최대 동시 활성 개수를 구한다."""
    events = []

    for start, end in intervals:
        events.append((start, 1))
        events.append((end, -1))

    # 같은 좌표에서는 -1이 +1보다 먼저 와서 [start, end)를 표현한다.
    events.sort()
    active = 0
    answer = 0

    for _, delta in events:
        active += delta
        answer = max(answer, active)

    return answer
