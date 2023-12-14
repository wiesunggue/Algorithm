# https://www.acmicpc.net/problem/2812
# 백준 2812번 크게 만들기 문제
from collections import deque

N,K = map(int,input().split())

# 아이디어 앞에서 부터 지우면서 감소수열을 만들어야 한다
arr = input()
st = ['a'] # 감소수열을 만들기 위한 10 0~9보다 더 큰수가 들어간다
idx = 0
while K and idx<N:
    while st[-1]<arr[idx] and K:
        st.pop()
        K -= 1
    st.append(arr[idx])
    idx += 1

# 삭제가 끝났지만 남은 자료가 존재하는 경우
while idx<N:
    st.append(arr[idx])
    idx +=1

# 삭제가 다 안끝난 경우 필요한 만큼 마지막 자리를 삭제
while K:
    st.pop()
    K -= 1

# 초기값 a 빼고 출력
print(''.join(st[1:]))