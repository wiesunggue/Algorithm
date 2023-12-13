# https://www.acmicpc.net/problem/21314
# 백준 21314번 민겸 수 문제

s = input()
M,m,c=[],[],0
for i in s:
    if i=='K':
        M.append('5'+'0'*c)
        m.append('1'*(c!=0)+'0'*(c-1)+'5')
        c=0
    else:
        c+=1
M.append('1'*c)
m.append('1'*(c!=0)+'0'*(c-1))
print(''.join(M),''.join(m))