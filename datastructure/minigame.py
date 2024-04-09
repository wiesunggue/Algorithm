# https://www.acmicpc.net/problem/25757
# 백준 25757번 임스와 함께하는 미니게임 문제
import sys
input = sys.stdin.readline

name_dict = {}
game_dict = {'Y':2,'F':3,'O':4}

N,game = input().split()
for i in range(int(N)):
    name_dict[input()] = True
print(len(name_dict)//(game_dict[game]-1))