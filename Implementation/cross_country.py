# https://www.acmicpc.net/problem/9017
# 백준 9017번 크로스 컨트리 문제

import sys
from collections import defaultdict
input =  sys.stdin.readline
def compare(teamA, teamB):
    # 비교 연산에 대한 정의
    print(sum(teamA[:4]),sum(teamB[:4]))
    if sum(teamA[:4])==sum(teamB[:4]):
        return teamA[4:]>teamB[4:]
    return sum(teamA[:4])>sum(teamB[:4])

def solve():
    counter_dict = defaultdict(int)
    score_dict = defaultdict(list)
    N = int(input())
    arr = list(map(int,input().split()))

    # 팀원이 6명인 팀을 체크
    for i in arr:
        counter_dict[i] +=1
    score = 1

    # 스코어 산정
    for i in arr:
        if counter_dict[i]==6:
            score_dict[i].append(score)
            score += 1
            min_team = i
    print(score_dict,min_team)

    # 우승 팀 계산
    for key in score_dict.keys():
        print(compare(score_dict[min_team],score_dict[key]))
        if compare(score_dict[min_team],score_dict[key]):
            min_team = key
            print('**',min_team)

    return min_team

T = int(input())
for test in range(T):
    print(solve())