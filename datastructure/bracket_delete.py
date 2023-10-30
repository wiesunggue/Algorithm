# https://www.acmicpc.net/problem/2800
# 백준 2800번 괄호 제거
from collections import deque

print(200*1024) # 문자열의 최대 길이 200 * 가능한 총 경우의 수 1024 = 20만 -> 시간복잡도상 문제 없음

def solution():
    s = input()
    ans = set()  # 정답 저장 리스트
    st = deque()
    # 쌍이 되는 괄호를 찾아서 매칭 시켜두자
    mapping = {}
    for idx in range(len(s)):
        if s[idx]=='(':
            st.append(idx)
        if s[idx]==')':
            bef = st.pop()
            mapping[bef]=idx
    print(mapping)
    # convert연산 2400 * 1024번 연산 -> 250만번 연산으로 수행 가능
    for state in range(1, 2**len(mapping)):
        ans.add(convert(s,state,mapping))
    ans = sorted(list(ans))
    print(*ans,sep='\n')


def convert(s,state,mapping):
    # 최대 2400번의 연산(12번 update * 문자열의 길이 200)
    for idx, (key, value) in enumerate(mapping.items()):
        if state & (1<<idx):
            s = s[:key] + ' ' + s[key+1:]
            s = s[:value] + ' ' + s[value+1:]
    s = ''.join(s.split()) # 공백 제거하기
    return s
solution()

