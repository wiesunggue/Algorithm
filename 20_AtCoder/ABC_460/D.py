N, M = map(int, input().split())
arr = [list(input().strip()) for i in range(N)]
g = 10
generation = [[["" for k in range(M)] for j in  range(N)] for i in range(g)]
generation[0] = arr[:]
move_x = [-1,-1,-1,0,0,1,1,1]
move_y = [-1,0,1,-1,1,-1,0,1]
print(*generation[0],sep='\n')
for t in range(1,g):
    for i in range(N):
        for j in range(M):
            if generation[t-1][i][j] == "#":
                generation[t][i][j] = "."
            else:
                for k in range(8):
                    if 0<=i+move_x[k]<N and 0<=j+move_y[k] <M and generation[t-1][i+move_x[k]][j+move_y[k]] == "#":
                        generation[t][i][j] = "#"
                        break


def state(t1,t2):
    if generation[t1] == generation[t2]:
        return True
    else:
        return False

for i in range(1,g):
    print(f"generation {i}---------------------------")
    print(*generation[i],sep='\n')