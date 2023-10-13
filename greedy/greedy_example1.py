MAX_N=10000
e=[0]*MAX_N
m=[0]*MAX_N
N=3
e=[1,2,3] # 먹는 시간
m=[1,2,1] # 데우는 시간
def heat():
    order=[(0,0)]*N
    for i in range(N):
        order[i]=(-e[i],i)
    order.sort()
    ret, beginEat= 0,0
    for i in range(N):
        box=order[i][1]
        beginEat+=m[box]
        print(box)
        ret = max(ret, beginEat+e[box])
    
    return ret

print(heat())