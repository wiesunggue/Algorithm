# https://www.acmicpc.net/problem/5373
# 큐빙
import copy
revert = {'L': 'R', 'R': 'L', 'F': 'B', 'B': 'F', 'U': 'U', 'D': 'D'}

dice = {'U':[0,1,2,3,4,5],
        'D':[5,1,4,3,2,0],
        'F':[3,0,2,5,4,1],
        'B':[1,5,2,0,4,3],
        'L':[4,1,0,3,5,2],
        'R':[2,1,5,3,0,4]}
def rotate(cub):
    new_cube = [[cub[0][2], cub[0][5], cub[0][8], cub[0][1], cub[0][4], cub[0][7], cub[0][0], cub[0][3], cub[0][6]],
                [cub[1][0], cub[1][1], cub[1][2], cub[1][3], cub[1][4], cub[1][5], cub[2][0], cub[2][3], cub[2][6]],
                [cub[3][2], cub[2][1], cub[2][2], cub[3][1], cub[2][4], cub[2][5], cub[3][0], cub[2][7], cub[2][8]],
                [cub[4][2], cub[4][5], cub[4][8], cub[3][3], cub[3][4], cub[3][5], cub[3][6], cub[3][7], cub[3][8]],
                [cub[4][0], cub[4][1], cub[1][8], cub[4][3], cub[4][4], cub[1][7], cub[4][6], cub[4][7], cub[1][6]],
                [cub[5][0], cub[5][1], cub[5][2], cub[5][3], cub[5][4], cub[5][5], cub[5][6], cub[5][7], cub[5][8]]]
    return new_cube

def rotateclockwise(cub):
    A1 = rotate(cub)
    A2 = rotate(A1)
    A3 = rotate(A2)
    return A3

def rotatecounterclockwise(cub):
    return rotate(cub)

def dice_rotate(cub,d):
    new_dice = []
    for i in dice[d]:
        new_dice.append(cub[i])
    return new_dice

def cubing(cub, d):
    a,b = list(d)
    ra = revert[a]
    print(a,b,cub)
    cub = dice_rotate(cub, a)
    print(a,b,cub)
    if b == '+':
        cub = rotateclockwise(cub)
    else:
        cub = rotatecounterclockwise(cub)
    print(a,b,cub)
    cub = dice_rotate(cub, ra)

    return cub

T = int(input())
for i in range(T):
    N = int(input())
    command = input().split()

    #cube = [['w']*9,['o']*9,['b']*9,['r']*9,['g']*9, ['y']*9]
    cube = [['w', 'w', 'w', 'w', 'w', 'w', 'g', 'g', 'g'], ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'], ['w', 'b', 'b', 'w', 'b', 'b', 'w', 'b', 'b'], ['r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r'], ['g', 'g', 'y', 'g', 'g', 'y', 'g', 'g', 'y'], ['b', 'b', 'b', 'y', 'y', 'y', 'y', 'y', 'y']]
    for c in command:
        cube = cubing(cube,c)
        print(c,cube)

    print(''.join(cube[0][0:3]))
    print(''.join(cube[0][3:6]))
    print(''.join(cube[0][6:9]))
    print()

#cube = [['w', 'w', 'w', 'w', 'w', 'w', 'g', 'g', 'g'], ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
#        ['w', 'b', 'b', 'w', 'b', 'b', 'w', 'b', 'b'], ['r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r'],
#        ['g', 'g', 'y', 'g', 'g', 'y', 'g', 'g', 'y'], ['b', 'b', 'b', 'y', 'y', 'y', 'y', 'y', 'y']]
cube = [['w']*9,['o']*9,['b']*9,['r']*9,['g']*9, ['y']*9]
cube = dice_rotate(cube,"F")
print(cube)
cube = rotate(cube)
print(cube)
cube = dice_rotate(cube,'B')
print(cube)
cube = dice_rotate(cube,"B")
print(cube)
cube = rotate(cube)
print(cube)
cube = dice_rotate(cube,"F")
print(cube)