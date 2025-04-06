# abs() 절댓값 반환
print(abs(-1),abs(1))

# all() 모든 bool값이 True면 True반환 []->True
print(all([]),all([True, True,1,2,3]),all([True,True,False]))

# any() 어떤 bool값이 True면 True반환 []->False
print(any([]),any([True,True,False]),any([0,0,0,1]),any([0,0,0,False]))

# bin() 이진수로 변환
print(bin(10))

# int('num', base) n진수 -> 10진수로 변환
print(int('101',3), int(bin(10),2))

# chr() 아스키코드를 문자로 변환
print(chr(97), chr(65))

# 문자를 아스키코드로 변환
print(ord('a'),ord('A'))

# enumerate() index, arr[index]을 하나씩 반환
print(list(enumerate(['a','b','c'])))

# filter(function, iterable) 조건에 맞는 배열만 generator로 반환
print(list(filter(lambda x: x>50, [10,20,30,40,50,60,70,80,90,100])))

# map(function, iterable) 각 arr의 원소에 function(arr원소)을 적용하여 generator로 반환
print(list(map(lambda x:x**2,[1,2,3,4])))

# eval()문자열로 들어온 연산 식 처리하기
print(eval('1+2'), eval('[1,2]'))
from functools import reduce
# reduce(function, iterable)
print(reduce(lambda x,y:x+y,[1,2,3,4,5,6]))


# zip() 압축& 압축해제하기
# 압축하기
zipped = list(zip([1,2,3],(5,6,7)))
print('zipped',zipped)

# 압축 해제하기 -> x만의 좌표나 y만의 좌표나 뽑아낼 수 있음
A,B = zip(*zipped)
print(A)
print(B)

from functools import cmp_to_key
# cmp_to_key 정렬의 비교 기준함수
# 반드시 1과 -1이 있어야 한다(True, False가 기준이 아니다)
print(sorted([-6,-1,5,3,-2],key=cmp_to_key(lambda x,y:1 if x**2>y**2 else -1)))


# 최대 재귀 횟수 설정
import sys
sys.setrecursionlimit(10**5)

# 빠른 입출력
import sys
input = sys.stdin.readline
#print = sys.stdout.write # 대부분의 경우 ' '.join()을 쓰는 것이 더 빠르다

# itertools 몇가지 함수들

# prodcut() iterable타입의 카데시안 프로덕트
from itertools import product
for i in product([1,2,3,4],'he'):
    print(i)

#permutations(iterable,int) -> int개로 가능한 모든 순열 출력(순서 미고려)
from itertools import permutations
print('permuatations')
for i in permutations([1,2,3,4],2):
    print(i)
#combinations(iterable,int) -> int개로 가능한 모든 조합(순서 고려)
from itertools import combinations
print('combinations')
for i in combinations([1,2,3,4],2):
    print(i)

# combinations_with_replacemnet(iterable, int) int개로 가능한 중복 조합
from itertools import combinations_with_replacement
print('combinations_with_replacement')
for i in combinations_with_replacement([1,2,3,4],2):
    print(i)

# 리스트 탐색
arr = list(range(10))
print(arr[::-1]) # 3

# copy
# copy() deepcopy()
from copy import copy, deepcopy
arr = [[1,2,3,],[4,5,6]]
brr = copy(arr)
crr = deepcopy(arr)
arr[0][2]=1
print(brr) # 1차원 배열에서만 사용할 수 있다.(list까지만 복사, list속 list는 주소만 불러옴)
print(crr) # 2차원 배열에서도 사용할 수 있다.(list속의 list도 값 복사)

# 최소 힙 사용하기
import heapq
priority_queue = []
heapq.heappush(priority_queue,2)
heapq.heappush(priority_queue,-1)
heapq.heappush(priority_queue,3)
heapq.heappush(priority_queue,5)
heapq.heappush(priority_queue,-10)
print(heapq.heappop(priority_queue)) # 항상 최솟 값부터 반환한다


# collections 유용한 기능
# deque 사용하기
from collections import deque
dq = deque([1,2,3,])
dq.append(4)
dq.appendleft(0)
dq.pop()
dq.popleft()
print(dq)

# Counter 개수를 세는 딕셔너리
from collections import Counter
print(Counter('hello world'))
print(Counter([1,2,3,4,1,2,3,1,2,1]))

# defaultdict 디폴트 값이 있는 딕셔너리 if dict.get(a)==None; dict[a]= [] 와 같은 식으로 사용 가능
from collections import defaultdict
d = defaultdict(int)
d[1] += 1
d[2] += 2
print(d)

# OrderedDict 순서가 있는 딕셔너리(삽입된 순서대로 저장)
from collections import OrderedDict
od = OrderedDict()
od[1] = 2
od[2] = 5
od[0] = 1
print('od',od)

# queue 활용하기
# PriorityQueue().put((우선순위,값)) 으로 사용, 최소 힙
from queue import Queue,PriorityQueue
qu = Queue()
qu.put(1)
qu.put(2)
qu.put(0)
pq = PriorityQueue()
pq.put((1,'a'))
pq.put((2,'b'))
pq.put((0,'c'))
print(qu.qsize(),pq.qsize())
while qu.empty()==False:
    print(qu.get())
while pq.empty()==False:
    print(pq.get())


# bisect 이분 탐색하기
import bisect
lst = [1,3,5,6,6,8]
print(bisect.bisect_left(lst,4))
print(bisect.bisect_left(lst,6))
print(bisect.bisect_right(lst,6))


