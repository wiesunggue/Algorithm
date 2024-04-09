# https://www.acmicpc.net/problem/20006
# 백준 20006번 랭킹전 대기열 문제
import sys
input = sys.stdin.readline

def gamestart(players):
    print('Started!' if len(players)==m else 'Waiting!')
    for id in sorted(players):
        print(name_info[id],id)
p,m = map(int,input().split())
room = []
name_info = {}
for i in range(p):
    lv,id = input().split()
    lv = int(lv)
    name_info[id] = lv

    added = False
    # 플레이어 넣기
    for idx in range(len(room)):
        room_id,players = room[idx]
        if abs(name_info[room_id]-lv)<=10 and len(players) != m:
            players += [id]
            print(players)
            added = True
            break

    # 없다면 방 생성
    if added==False:
        room.append([id,[id]])
print(name_info)
for _, players in room:
    gamestart(players)