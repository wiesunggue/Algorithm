from itertools import combinations
while 1:
    try:
        for i in combinations(sorted(input().split()[1:]),6):
            print(*i)
        print()
    except EOFError:
        break