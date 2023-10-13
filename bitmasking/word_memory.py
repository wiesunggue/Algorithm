# 단어 암기
# https://www.acmicpc.net/problem/18119
import sys
input = sys.stdin.readline
word_memory=(1<<26)-1
def word_count():
    cnt=0
    for i in range(N):
        ans=(word_memory&optimized_arr[i])==optimized_arr[i]
        cnt+=ans
    return cnt
N,M=map(int,input().split())
arr=[input().rstrip() for i in range(N)]
optimized_arr=[0]*N
for i in range(N):
    for j in range(len(arr[i])):
        optimized_arr[i] |= (1<<(ord(arr[i][j])-97))
for i in range(M):
    a,b = input().split()
    if a=='1': # 까먹는다.
        word_memory &= ~(1<<(ord(b)-97))
    else: #기억해 낸다.
        word_memory |= (1<<(ord(b)-97))
    print(word_count())

arr_X=[1,2,3,4,5,6,7,8,9,5]
def increasing(idx):
    while arr_X[idx]<arr_X[idx+1]:
        idx+=1
def decreasing(idx):
    while arr_X[idx]>arr_X[idx+1]:
        idx+=1

def split_state():
    idx=0
    while idx<len(arr_X):
        increasing(idx)
        decreasing(idx)
        print(idx)
