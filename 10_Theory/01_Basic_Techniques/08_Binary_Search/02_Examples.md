# 이분 탐색 대표 유형과 예제

`check(X)`의 결과가 한 방향으로만 바뀌는지를 먼저 확인한 뒤, 정답이 될 수 있는 값의 범위를 이분 탐색한다.

난이도는 [solved.ac](https://solved.ac/) 기준이다. (확인일: 2026-08-17)

| 번호 | 대표 유형 | 핵심 `check(X)` | Basic (대표형) | Application (응용형) | Advanced (고난도 확장) |
| ---: | --- | --- | --- | --- | --- |
| [03](03_Production_Cutting.py) | 생산량 / 절단량 | 크기 `X`로 만들었을 때 목표 개수 이상을 만들 수 있는가? | BOJ 1654 랜선 자르기<br>**Silver II** | BOJ 1114 통나무 자르기<br>**Platinum V** | BOJ 5530 JOIOI 탑<br>**Platinum I** |
| [04](04_Interval_Min_Max.py) | 구간 Min-Max 분할 | 각 구간의 비용을 `X` 이하로 제한해 분할할 수 있는가? | BOJ 2343 기타 레슨<br>**Gold V** | BOJ 13397 구간 나누기 2<br>**Gold IV** | BOJ 14421 The Kingdom of JOIOI<br>**Platinum II** |
| [05](05_Distance_Max_Min.py) | 거리 Max-Min / 배치 | 최소 간격을 `X` 이상으로 유지하며 배치할 수 있는가? | BOJ 2110 공유기 설치<br>**Gold IV** | BOJ 6209 제자리 멀리뛰기<br>**Gold II** | BOJ 17976 Thread Knots<br>**Gold III** |
| [06](06_Time_Throughput.py) | 시간 / 처리량 | 시간 `X` 안에 필요한 작업량을 처리할 수 있는가? | BOJ 3079 입국심사<br>**Gold V** | BOJ 1561 놀이 공원<br>**Gold I** | BOJ 1348 주차장<br>**Platinum II** |
| [07](07_Count_Kth_Value.py) | Count / K번째 값 | `X` 이하인 값의 개수가 `K` 이상인가? | BOJ 1300 K번째 수<br>**Gold I** | BOJ 1637 날카로운 눈<br>**Platinum IV** | BOJ 12921 제한된 메모리<br>**Platinum I** |
| [08](08_Value_Range_Optimization.py) | 값 범위 `[L, R]` 최적화 | 특정 값 범위만 사용해 조건을 만족할 수 있는가? | BOJ 1981 배열에서 이동<br>**Platinum V** | BOJ 2842 집배원 한상덕<br>**Platinum IV** | BOJ 10227 삶의 질<br>**Platinum III** |
| [09](09_Graph_Threshold.py) | Graph Threshold | 비용 또는 가중치가 `X`를 넘는 간선을 제한했을 때 도달할 수 있는가? | BOJ 1800 인터넷 설치<br>**Gold I** | BOJ 2842 집배원 한상덕<br>**Platinum IV** | BOJ 1348 주차장<br>**Platinum II** |
| [10](10_Matching_Parametric.py) | Matching + Parametric | `X` 이하의 관계만 남겼을 때 완전 매칭이 가능한가? | BOJ 1348 주차장<br>**Platinum II** | BOJ 13166 범죄 파티<br>**Platinum II** | BOJ 2365 숫자판 만들기¹<br>**Platinum II** |
| [11](11_Flow_Parametric.py) | Flow + Parametric | 각 간선의 용량을 `X`로 제한해 필요한 유량을 보낼 수 있는가? | BOJ 2365 숫자판 만들기<br>**Platinum II** | Flow + 추가 제약 문제<br>**—** | 복합 Flow 결정 문제<br>**—** |
| [12](12_Parallel_Binary_Search.py) | Parallel Binary Search | 여러 `check(X)`를 한꺼번에 처리할 수 있는가? | BOJ 12921 제한된 메모리<br>**Platinum I** | BOJ 1396 크루스칼의 공<br>**Platinum I** | BOJ 8217 유성<br>**Diamond IV** |

> ¹ BOJ 2365는 매칭 관점으로 확장해 볼 수 있지만, 일반적으로는 유량 기반 풀이가 더 직접적이다.
