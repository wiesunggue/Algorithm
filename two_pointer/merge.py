# https://www.acmicpc.net/problem/11728
# 백준 11728번 배열 합치기
import sys
input = sys.stdin.readline

def array_mergy():
    N, M = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    idx1,idx2 = 0,0
    merged_arr = [0]*(N+M)
    while idx1!=N and idx2!=M:
        if arr1[idx1]<arr2[idx2]:
            merged_arr[idx1+idx2] = arr1[idx1]
            idx1+=1
        else:
            merged_arr[idx1+idx2] = arr2[idx2]
            idx2+=1
    while idx1!=N:
        merged_arr[idx1+idx2] = arr1[idx1]
        idx1+=1
    while idx2!=M:
        merged_arr[idx1+idx2] = arr2[idx2]
        idx2+=1
    print(*merged_arr)

array_mergy()