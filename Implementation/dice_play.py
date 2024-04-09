# https://www.acmicpc.net/problem/14499
# 백주 14499번 주사위 굴리기

dice_state = {1:[6,3,4,2,5],2:[5,1,6,3,1],3:[4,6,1,2,5],4:[3,1,6,2,5],5:[2,3,4,1,6],6:[1,3,4,5,2]}
dice_data = [0,0,0,0,0,0,0]
move_x = [0,0,0,-1,1]
move_y = [0,1,-1,0,0]
N, M, x, y, K = map(int,input().split())
map_info = [list(map(int,input().split())) for i in range(N)]

move_query = list(map(int,input().split()))
state = 6
for i in range(K):
    query = move_query[i]
    new_x,new_y = move_x[query]+x,move_y[query]+y
    if new_x>=N or new_y>=M:
        continue
    x,y = new_x,new_y
    state = dice_state[state][query]
    if dice_data[state]==0:
        dice_data[state] = map_info[x][y]
    else:
        map_info[x][y]=dice_data[state]
        dice_data[state] = 0
    print(state,dice_data[dice_state[state][0]],dice_state[state][0],dice_data)
