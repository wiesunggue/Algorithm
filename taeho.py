# print
# list
# dictionry
# stack, queue, pq
# heapq
# map, filter, set, lambda, sort
import random
from collections import defaultdict, Counter, OrderedDict,deque

# input()
#input().split('abcd')
#print("1abcd2abcd3".split("ab"))
#arr = ['1','2','3']
# map
#arr = [1,2,3,4,5,]
[].sort()
[1,2,3,4,5].insert(10,50)
[].append()
len([1,2,3,4])
[1,2,3,4,5].index(4)
['1','2','3','abc'].index('abc')

arr = list(map(int,input().split()))
arr = []
for i in range(N):
    arr.append(int(input()))

N = int(input())
arr = [int(input()) for i in range(N)]
#dictionary
d = {}
#d['aaa'] = 3

#d['aaa']
s = ()
t = (1,2)

#s = set()
#s[1] = 1
d.get(1)

arr = [3,1,2]
arr.sort()
arr2 = sorted(arr)

arr = [0] * 1000
arr = [0 for i in range(1000)]

df = defaultdict(int)
print(df[10])

c = Counter("aabbccdddabab")
print(c)

od = OrderedDict()
od[3]=1
od[2] =2
od[1]=3

print(od)

#dq = deque()
#dq.appendleft()
#dq.popleft()

import heapq
pq = []
for i in range(10):
    heapq.heappush(pq,random.random())

while pq:
    print(heapq.heappop(pq))

arr = [1,2,3,4,5]
print(list(filter(lambda x:x%2,arr)))

arr = {}
for i in range(10):
    arr[input()]

print(arr)
[1,2,3,4,5]
print(*arr)
#1 2 3 4 5

print(*arr,end=' ')

arr = [[1,2,3],[4,5,6],[7,8,9]]
print(arr)