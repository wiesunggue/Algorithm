# 알고스팟 문제
# https://www.algospot.com/judge/problem/read/QUANTIZE
# Quantization 문제
MAX_VALUE = 2**31
# N개로 이루어진 배열을 K개의 정보를 통해 양자화한다고 할 때 손실이 최소가 되는 제곱합을 구하는 문제
# test 1
#N,K = 10,3
#arr = [3,3,3,1,2,3,2,2,2,1]

# test 2
N,K = 9,3
arr = [1,744,755,4,897,902,890,6,777]
# 이 문제는 정렬하여 어떻게 수열을 나눌지를 찾는 문제로 볼 수 있다.
# 이것을 재귀로 구현하자
arr.sort()
def error(start,to):
    if start==to:
        return 0
    data = int(sum(arr[start:to])/(to-start)+0.5)
    total = 0
    for i in range(start, to):
        total += (data-arr[i])**2
    return total

def quantize(start, parts):
    print(start, parts)
    if start == N:
        return 0
    if parts == 0:
        return MAX_VALUE
    ret = MAX_VALUE
    for to in range(1,N-start+1):
        ret = min(ret, error(start,start+to)+quantize(start+to,parts-1))

    return ret

print(quantize(0,K))

# 현재 코드에는 2가지 문제점이 있다
# 1. PSUM을 활용한 연산 최적화
# 2. 반복을 기록하여 반복연산 삭제하기(메모이제이션)
