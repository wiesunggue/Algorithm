# https://www.acmicpc.net/problem/20125
# 백준 20125번 쿠키의 신체 측정 문제

import sys
input = sys.stdin.readline

N = int(input())
str_arr = [input() for i in range(N)]
left_leg = 0
right_leg = 0

# 심장 찾기
for i in range(N):
    if str_arr[i].find('*')!=-1:
        heart = i+1,str_arr[i].find('*')
        break

# 허리 찾기
for i in range(heart[0]+1,N):
    if str_arr[i].count('*')==2:
        middle = i-heart[0]-1
        middle_pos = i
        break

print(middle_pos)
# 다리 찾기
for i in range(middle_pos,N):
    left_leg+= str_arr[i][:heart[1]].count('*')
    right_leg += str_arr[i][heart[1]:].count('*')
left_arm = str_arr[heart[0]][:heart[1]].count('*')
right_arm = str_arr[heart[0]][heart[1]+1:].count('*')

print(heart[0]+1,heart[1]+1)
print(left_arm,right_arm,middle,left_leg,right_leg)