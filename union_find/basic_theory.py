# 유니온 파인드
# 개념 : 집합을 합치기 a와 b가 같은 집합이고 b와 c가 같은 집합이면 a b c모두 같은 집합이 된다
# 응용 예제 : 집합 연산하기, 사이클 검사하기

# 유니온 파인드 클래스 정의하기
# 유니온 파인드 기본
import random
class NaiveDisjointSet():
    def __init__(self,size):
        self.parent=[i for i in range(size)]
        self.N = size

    def find(self,u):
        if u==self.parent[u]:
            return u
        return self.find(self.parent[u])

    def merge(self, u, v):
        u,v = self.find(u),self.find(v)
        if u==v:
            return
        self.parent[u]=v

# 최적화된 유니온 파인드
class OptimizedDisjointSet():
    def __init__(self,size):
        self.parent = [i for i in range(size)]
        self.rank = [1 for i in range(size)]
        self.N = size

    def find(self,u):
        if u==self.parent[u]:
            return u
        return self.find(self.parent[u])

    def merge(self,u,v):
        u,v = self.find(u),self.find(v)
        if u==v:
            return
        if self.rank[u]>self.rank[v]:
            u,v = v,u

        self.parent[u]=v
        if self.rank[u]==self.rank[v]:
            self.rank[v]+=1



# 나중에 체크해보자
# 이기면 배팅금액의 2배 받고, 100원 배팅
# 지면 배팅금액을 잃고 2배 배팅(돈이 부족하면 남은 돈 만큼 배팅)
def solution(money, expected, actual):
    N = len(expected)
    win = [expected[i]==actual[i] for i in range(N)] # 승패 기록을 저장한 리스트
    m = 100 # 배팅 금액
    res = money
    for i in range(N):
        # 배팅하기
        if res < m: # 돈이 부족한 경우
            m  = res
            res = 0
        else: # 돈이 충분한 경우
            res -= m

        # 결과 보기
        if win[i]==True:
            res += m*2 # 2배의 돈을 번다
            m = 100 # 배팅금액 초기화
        else:
            m *= 2 # 배팅 금액 2배 증가

    answer = res
    return answer

