from collections import  defaultdict
import sys
input = sys.stdin.readline


N, M = map(int, input().split())

bird = [list(map(int, input().split())) for i in range(N)]

bird.sort(key= lambda x : x[1])
count = defaultdict(int)
start = 0
for i in range(N):
    if bird[i][1] != 1:
        count[bird[i][0]] += 1
    else:
        count[bird[i][2]] += 1
for i in range(N):
    if bird[i][1] == 1:
        start = i+1

print(count)
for i in range(1,M + 1):
    while start < N:
        if bird[start][1] == i:
            count[bird[start][0]] -= 1
            if count[bird[start][0]] == 0:
                count.pop(bird[start][0])
            count[bird[start][2]] += 1
            start += 1
        else:
            break
    print(len(count))
