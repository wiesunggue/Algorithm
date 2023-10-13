def solution(cacheSize, cities):
    dq = []
    answer = 0
    for city in cities:
        city = city.upper()
        if city in dq:
            answer += 1
            for idx in range(len(dq)):
                if dq[idx].find(city) != -1:
                    chk = idx
            
            dq.pop(chk)
            dq.append(city)
        
        else:
            answer += 5
            if len(dq) < cacheSize:
                dq.append(city)
            else:
                dq.append(city)
                dq.pop(0)
    print(dq)
    return answer

print(solution(30,['a','b','a','d','a']))
from collections import Counter
A=Counter('abcd')
B=Counter('cdef')
for key in A:
    B[key]=3
print(B)