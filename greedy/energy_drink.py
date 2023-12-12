# https://www.acmicpc.net/problem/20115
# 백준 20115번 에너지 드링크 문제
import sys

N = int(input())
arr = list(map(int,sys.stdin.readline().split()))

M = max(arr)
print(M/2+sum(arr)/2)