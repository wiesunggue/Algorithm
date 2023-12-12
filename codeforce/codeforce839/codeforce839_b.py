def beautiful(mat):
    A= mat[0][0]<mat[0][1] and mat[0][0]<mat[1][0] and mat[1][0]<mat[1][1] and mat[0][1]<mat[1][1]
    return A

def rotation(mat):
    mat[0][0], mat[0][1], mat[1][1], mat[1][0] = mat[1][0], mat[0][0], mat[0][1],mat[1][1]

    return mat

T=int(input())
for test in range(T):
    arr=[list(map(int,input().split())) for _ in range(2)]
    ans=0
    for i in range(4):
        arr=rotation(arr)
        if beautiful(arr)==True:
            ans=1
            break
    print("YES" if ans else "NO")
    