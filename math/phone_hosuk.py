# https://www.acmicpc.net/problem/21275
# 백준 21275번 폰 호석만 문제

s,t = input().split()
#print(int(s,12),12*10+10)
def find_min_base(s):
    t = max(list(s))
    if 'a'<=t<='z':
        t = ord(t)-ord('a')+10
    else:
        t = ord(t)-ord('0')
    t = max(t,1)
    return t

cnt = 0
for i in range(find_min_base(s)+1,37):
    for j in range(find_min_base(t)+1,37):
        if int(s,i)==int(t,j) and i != j:
            cnt += 1
            X = int(s,i)
            A = i
            B = j
            if X>=2**63:
                cnt -= 1
#print(int(s,3), int(t,9),int('22',3))
if cnt == 0:
    print('Impossible')
elif cnt == 1:
    print(X,A,B)
else:
    print('Multiple')
