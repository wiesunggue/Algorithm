# https://www.acmicpc.net/problem/17825
# 주사위 윳놀이


k = {21:(-1,0),22:(23,13),23:(24,16),24:(25,19),25:(26,25),26:(27,30),27:(20,35),28:(29,22),29:(25,24),30:(31,28),31:(32,27),32:(25,26)}
graph = {i: (i+1,i*2) for i in range(21)}
link = {5:22,10:28,15:30}
graph.update(k)
dices = list(map(int,input().split()))
visited = [0]*40
horse = [0]*4
max_score = 0
def move(idx,cnt):
    if cnt == 0:
        return idx
    if idx == -1:
        return idx
    i,s = graph[idx]
    return move(i,cnt -1)
def backtracking(cnt,score):
    global max_score
    print(horse)
    if cnt == 10:
        max_score = max(max_score,score)
        print(horse,score)
        return
    for i in range(4):
        h = horse[i]
        if h== -1:
            continue
        if h == 5 or h==10 or h==15:
            next_pos = move(link[h],dices[cnt]-1)
        else:
            next_pos = move(h,dices[cnt])
        if next_pos == -1:
            horse[i] = -1
            visited[h] = 0
            backtracking(cnt+1,score)
            horse[i] = h
            visited[h] = 1
            continue
        n,s = graph[next_pos]
        if visited[next_pos] == 0:
            horse[i] = next_pos
            visited[h] = 0
            visited[next_pos] = 1
            backtracking(cnt+1,score+s)
            visited[h] = 1
            visited[next_pos] = 0
            horse[i] = h

backtracking(0,0)
print(max_score)