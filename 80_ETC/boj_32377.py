N,x,y,z = map(int, input().split())
def pop_ballons(time):
    ans = time//x + time//y + time//z
    return ans

start, mid, end = 0, 0, 10**20

while start < end:
    mid = (start + end) // 2
    cnt = pop_ballons(mid)
    if cnt < N:
        start = mid + 1
    else:
        end = mid

result = pop_ballons(start)
remain_x = start%x
remain_y = start%y
remain_z = start%z
m = min(remain_x, remain_y, remain_z)
if remain_z == m:
    if N == result:
        print("C win")
    else:
        result -= 1
if remain_y == m:
    if N == result:
        print("B win")
    else:
        result -= 1
if remain_x == m:
    if N == result:
        print("A win")
    else:
        result -= 1
