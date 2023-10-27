# https://www.acmicpc.net/problem/27809
from collections import defaultdict, Counter
import sys
import random
input = sys.stdin.readline
T=99
def solution():
    U = 2
    map_dict = {'0':'E','1':'F','2':'G','3':'H','4':'I','5':'J','6':'K','7':'L','8':'N','9':'M'}
    #data = [input().split() for i in range(10000)]
    data = [0]*10000
    for i in range(10000):
        M = random.randint(1,10**16)
        data[i]= str(-1),''.join(list(map(lambda x:map_dict[x],str(random.randint(1,M)))))
    all_dict=defaultdict(lambda: 10)
    support_dict = defaultdict(int)
    cnt_dict = Counter()
    for num, s in data:
        cnt_dict.update(Counter(list(s)))
        cnt_dict[s[0]]+=10
        support_dict[s[0]]=1
        if num=='-1':
            for i in list(s):
                all_dict[i]=min(9,all_dict[i])
            continue
        # 길이가 1이 아니면 첫 문자는 처
        else:
            for i in range(len(s)):
                if i==0 and len(num)==len(s):
                    all_dict[s[i]] = min(int(num[i]), all_dict[s[i]])
                else:
                    all_dict[s[i]]=min(9,all_dict[s[i]])

    ans = [-1]*10
    reversed_dict = defaultdict(list)
    for key,value in all_dict.items():
        if support_dict[key]==0:
            ans[0]=key
            continue
        reversed_dict[value].append(key)
    #print(reversed_dict)
    for key in sorted(reversed_dict):
        value_list = reversed_dict[key]
        value_list = sorted(value_list, key=lambda x: -cnt_dict[x])

        if len(value_list)==1:
            ans[key]=value_list[0]
        else:
            idx=0
            for j in range(1,key+1):
                if ans[j]==-1:
                    ans[j]=value_list[idx]
                    idx+=1
    if num=='-1':
        ans = ans[:1] + sorted(reversed_dict[9], key=lambda x: -cnt_dict[x])
    return ans

for test in range(T):
    print(f"Case #{test+1}: ",*solution(),sep='')
