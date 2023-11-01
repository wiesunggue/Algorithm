# https://www.acmicpc.net/problem/4358
# 백준 4358번 생태학
from collections import Counter
eco_dict = Counter()
s = '1'
while True:
    try:
        s = input()
        eco_dict[s] += 1
    except:
        break
total = sum(eco_dict.values())
print(eco_dict)
for key in sorted(eco_dict):
    print(key,f'{eco_dict[key]/total*100:.4f}')
