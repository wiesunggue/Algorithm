# https://www.acmicpc.net/problem/14891
# 백준 14891번 톱니바퀴 문제

from collections import deque

def update(idx,direction):
    link1 = gear_list[0][2]!=gear_list[1][6]
    link2 = gear_list[1][2]!=gear_list[2][6]
    link3 = gear_list[2][2]!=gear_list[3][6]
    link = [link1,link2,link3]
    if idx == 0:
        if link[0] == 0:
            gear_list[0].rotate(direction)
        elif link[1] == 0:
            gear_list[0].rotate(direction)
            gear_list[1].rotate(-direction)
        elif link[2] == 0:
            gear_list[0].rotate(direction)
            gear_list[1].rotate(-direction)
            gear_list[2].rotate(direction)
        else:
            gear_list[0].rotate(direction)
            gear_list[1].rotate(-direction)
            gear_list[2].rotate(direction)
            gear_list[3].rotate(-direction)

    if idx == 1:
        gear_list[1].rotate(direction)
        if link[0] != 0:
            gear_list[0].rotate(-direction)
        if link[1] != 0:
            gear_list[2].rotate(-direction)
            if link[2] != 0:
                gear_list[3].rotate(direction)

    if idx == 2:
        gear_list[2].rotate(direction)
        if link[1] != 0:
            gear_list[1].rotate(-direction)
            if link[0] != 0:
                gear_list[0].rotate(direction)
        if link[2] != 0:
            gear_list[3].rotate(-direction)
    if idx == 3:
        if link[2] == 0:
            gear_list[3].rotate(direction)
            return
        elif link[1] == 0:
            gear_list[3].rotate(direction)
            gear_list[2].rotate(-direction)
        elif link[0] == 0:
            gear_list[3].rotate(direction)
            gear_list[2].rotate(-direction)
            gear_list[1].rotate(direction)
        else:
            gear_list[3].rotate(direction)
            gear_list[2].rotate(-direction)
            gear_list[1].rotate(direction)
            gear_list[0].rotate(-direction)

def score():
    ans = 0
    for i in range(4):
        ans += gear_list[i][0]*2**i
    return ans
gear_list = [deque(list(map(int,input()))) for i in range(4)]


N = int(input())
for i in range(N):
    nextSerial,direction = map(int, input().split())
    update(nextSerial - 1, direction)
print(score())