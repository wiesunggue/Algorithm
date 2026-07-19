import sys
from collections import Counter
input = sys.stdin.readline

S = Counter(list(input().rstrip()))
print(S)
if S['E'] > S["W"]:
    print("East")
else:
    print("West")