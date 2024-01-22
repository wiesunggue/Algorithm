# https://www.acmicpc.net/problem/3151
# 백준 3151번 합이 0 문제

# 투 포인터 문제이지만 왜인지 해쉬만 잘 활용하면 풀려버리는 문제....?
# 문제 해결 전략
# Counter를 이용해서 각 값의 출현횟수를 기록한다
# Key를 기준으로 탐색한다. -> left key와 right키를 찾고 left+right+X = 0인 X=-left-right라고 할 수 있다.
# 이때의 X는 left<=X<=right이어야지만 반복 중 중복을 제거할 수 있다.
# 총 경우의 수는 Counter[left]*Counter[right]*Counter[-left-right]를 모두 더한 값이다.
# 하지만, 같은 수에 의해서 합이 0이 되는 경우가 존재한다. 2개가 같고 1개가 다른 경우와 3개 모두 같은 경우가 있다.
# left=X인 경우 -> (Counter[left]*(Counter[left]-1))/2*Counter[right] ( left의 개수 combination 2)*right의 개수
# right=X인 경우 -> (Counter[right]*(Counter[right]-1))/2*Counter[left] ( right의 개수 combination 2)*left의 개수
# left=right=X인 경우(전부 0) -> N combination 3와 같다.(N*(N-1)*(N-2)//6, N = Counter[0])
import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
abilities = Counter(map(int,input().split()))
abilities_key = sorted(abilities.keys())
key_size = len(abilities_key)
ans = abilities[0]*(abilities[0]-1)*(abilities[0]-2)//6

for i in range(key_size):
    for j in range(i+1,key_size):
        left_key = abilities_key[i]
        right_key = abilities_key[j]
        if left_key<-left_key-right_key<right_key and abilities[-left_key-right_key]!=0:
            ans += abilities[left_key]*abilities[right_key]*abilities[-left_key-right_key]
        elif left_key==-left_key-right_key:
            ans += (abilities[left_key]*(abilities[left_key]-1)//2)*abilities[right_key]
        elif right_key==-left_key-right_key:
            ans += (abilities[right_key]*(abilities[right_key]-1))//2*abilities[left_key]


print(ans)