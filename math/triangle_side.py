# https://www.acmicpc.net/problem/5073
# 백준 5073번 삼각형과 세 변 문제

# 정삼각형/ 이등변/ 삼각형/ 삼각형 불가능
ans_list = ['Equilateral', 'Isosceles', 'Scalene', 'Invalid']

while True:
    a,b,c = sorted(list(map(int,input().split())))
    if a==b==c==0:
        break

    if a+b<=c:
        print(ans_list[3])
    elif a==b==c:
        print(ans_list[0])
    elif a==b or b==c:
        print(ans_list[1])
    else:
        print(ans_list[2])
