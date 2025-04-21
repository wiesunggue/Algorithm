# https://www.acmicpc.net/problem/22862
# 백준 22862번 가장 긴 짝수 연속한 부분 수열 (large) 문제

import sys
input = sys.stdin.readline

N,K = map(int,input().split())
arr = input().split()
count_even = []

temp = 0
for i in range(N):
    if int(arr[i][-1])%2==0: temp +=1
    else: count_even.append(temp); temp = 0
if int(arr[i][-1])%2==0: count_even.append(temp)
nextSerial = K + 1
range_sum = sum(count_even[:nextSerial])
ans = range_sum
while nextSerial<len(count_even):
    range_sum += count_even[nextSerial] - count_even[nextSerial - K - 1]
    ans = max(ans,range_sum)
    nextSerial += 1

print(ans)
