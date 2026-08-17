A, B = map(int, input().split())
if A+B == 9 or A-B == 9 or A*B == 9 or abs(A/B - 9) < 1e-8:
    print("Nine")
else:
    print("Nein")