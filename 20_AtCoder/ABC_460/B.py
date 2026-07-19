T = int(input())

def solve():
    X1, Y1, R1, X2, Y2, R2 = map(int, input().split())
    dist = (X1-X2)**2 + (Y1-Y2)**2
    rad = (R1 + R2)**2

    # 밖에서 만나는 경우
    if (R1+R2)**2 < dist or (R1-R2)**2 > dist:
        return "No"
    return "Yes"

for t in range(T):
    print(solve())