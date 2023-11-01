# https://www.acmicpc.net/problem/21939
# 백준 21939번 문제 추천 시스템 Version 1

# heapq는 최소힙
import heapq
from collections import defaultdict

# solved 연산이 있다면 기록만 해두고 만나면 무시하도록 한다
# update는 현재 상태와 다르다면 무시하도록 한다.
sol_dict = defaultdict(int)
update_dict = defaultdict(int)
# add와 recommand는 단순하게 우선순위 큐에 저장
# 쉬운 문제는 min에 저장 어려운 문제는 max에 저장 -> 하나가 삭제되면 sol_dict에 추가해서 무시
pq_max = []
pq_min = []
N = int(input())

# 문제 리스트 저장
for i in range(N):
    prob, score = map(int, input().split())
    update_dict[prob] = score
    heapq.heappush(pq_max,(-score,-prob)) # score은 -를 곱해서 max힙이 되도록 하였고, prob는 항상 큰 번호의 문제를 출력할 수 있도록 하기 위해서 -를 붙임
    heapq.heappush(pq_min,(score,prob))

# 문제 해결하기
M = int(input())
for i in range(M):
    s = input().split()
    if s[0][0] == 'a': # add 명령어(시간 때문에 전체 문자열 확인하지 않음)
        prob, score = map(int,s[1:])
        sol_dict[prob] = 0
        update_dict[prob] = score
        heapq.heappush(pq_max,(-score,-prob))
        heapq.heappush(pq_min,(score,prob))
    elif s[0][0] == 'r': # recommend 명령어 (시간 때문에 전체 문자열 확인하지 않음)
        if s[1] == '1': # 어려운 문제 추천 명령을 받으면 pq_max에서 체크가 되지 않은 문제를 찾을 때까지 탐색을 반복하고 찾은 문제를 출력
            while True:
                score,prob = heapq.heappop(pq_max)
                if sol_dict[-prob] != 1 and update_dict[-prob] == -score:
                    break
            # 안 푼 문제는 추천 후 다시 넣어줌.
            heapq.heappush(pq_max,(score,prob))
            print(-prob)
        if s[1] == '-1': # 쉬운 문제 추천 명령을 받으면 pq_min에서 체크가 되지 않은 문제를 찾을 때까지 탐색을 반복하고 찾은 문제를 출력
            while True:
                score,prob = heapq.heappop(pq_min)
                if sol_dict[prob] != 1 and update_dict[prob] == score:
                    break
            # 안 푼 문제는 추천 후 다시 넣어줌.
            heapq.heappush(pq_min,(score,prob))
            print(prob)

    elif s[0][0] == 's': # solved 명령어(시간 때문에 전체 문자열 확인하지 않음)
        sol_dict[int(s[1])] = 1
