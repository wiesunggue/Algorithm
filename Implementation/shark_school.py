# https://www.acmicpc.net/problem/21608
# 백준 21608번 상어 초등학교 문제
import sys
input = sys.stdin.readline
posx = [-1,1,0,0]
posy = [0,0,-1,1]

def student_score():
    '''calculate student score'''
    score = 0
    score_list = [0,1,10,100,1000]
    for i in range(N):
        for j in range(N):
            like = 0
            for k in range(4):
                x,y = i+posx[k],j+posy[k]
                student = student_pos[i][j]
                if 0<=x<N and 0<=y<N:
                    if student_pos[x][y] in student_info[student]:
                        like+=1
            score+=score_list[like]

    return score

def set_position(student,like):
    max_position = []
    max_like = 0
    # 1번 연산하기
    for i in range(N):
        for j in range(N):
            if student_pos[i][j] == -1: # 사용 가능한 자리
                cnt = 0
                for k in range(4):
                    x,y = i+posx[k],j+posy[k]
                    if 0<=x<N and 0<=y<N and student_pos[x][y] in like:
                        cnt += 1

                if max_like<cnt:
                    max_like = cnt
                    max_position = []
                    max_position.append((i,j))
                elif max_like==cnt:
                    max_position.append((i,j))
    if len(max_position) == 1:
        return max_position[0]
    # 2번 연산하기
    black_list = [0]*len(max_position)
    for idx,(i,j) in enumerate(max_position):
        for k in range(4):
            x,y = i+posx[k],j+posy[k]
            if 0<=x<N and 0<=y<N and student_pos[x][y] == -1:
                black_list[idx]+=1
    if black_list.count(max(black_list)) == 1:
        pos = black_list.index(max(black_list))
        return max_position[pos]
    # 3번 연산하기
    goal = max(black_list)
    for i in range(len(black_list)):
        if black_list[i] == goal:
            pos = i
            break
    return max_position[pos]

N = int(input())
student_info = {}
student_pos = [[-1]*N for i in range(N)]
for query in range(N**2):
    student,*like = map(int,input().split())
    student_info[student]=like
    x,y = set_position(student,like)
    student_pos[x][y] = student

print(student_score())