
# 1. 아직 풀지 않은 데이터 구조 문제들(데이터 구조1, 2)
# TODO https://www.acmicpc.net/problem/22942 데이터 체커 문제
# TODO https://www.acmicpc.net/problem/1918 후위 표기식
# TODO https://www.acmicpc.net/problem/21944 문제 추천 시스템 Version 2


# https://github.com/tony9402/baekjoon
# 문제집에서 다루는 주제
# 0. 데이터 구조 1
# 1. 데이터 구조 2
# 2. 트리 # TODO 현재 진행중
# 3. 수학
# 4. 그리디
# 5. DP
# 6. DP2
# 7. 투포인터
# 8. 구현
# 9. 그래프 탐색
# 10. 완전 탐색
# 11. 시뮬레이션
# 12. 이분 탐색
# 13. 백트래킹
# 14. 분할정복
# 15. 누적 합
# 16. 문자열
# 17. 최단거리
# 18. 위상정렬
# 19. 분리집합
# 20. 최소스패닝트리
# 21. 트라이
# 22. 트리디피

# 제출 논문, 발표자료, 학회 캡처자료
# 숙소,  -> 오늘 하자
# KTX, -> 3명 시간 보고 정하기
# 출장 등록

# 모든 결제는 영수증과 매출 전표가 있어야 함(무엇을 결제했는지 알 수 있어야 함)
# 영수증만 있으면 증빙으로 안됨
# 영수증과 거래명세서 혹은 매출전표(무엇을 얼마나 결제했는지에 대한 확인이 필요함)
# 객실은 오늘 등록하자
# 논문 파일과 포스터 파일, 발표자 명단, 프로그램 시간표

# https://www.acmicpc.net/problem/11438
# https://www.acmicpc.net/problem/17435

n, m, h = map(int, input().split())
dp = [[1]+[0]*h for i in range(n+1)]
for i in range(1, n+1):
    dp[i] = dp[i-1].copy()
    blocks = list(map(int, input().split()))
    for b in blocks:
        for j in range(b, h+1):
            dp[i][j]+=dp[i-1][j-b]
print(*dp,sep='\n')