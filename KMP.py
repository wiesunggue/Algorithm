def getPartialMatchNaive(N):
    m = len(N)
    pi = [0]*m
    
    for begin in range(1,m):
        for i in range(m-begin):
            if N[begin+i] !=N[i]:
                break
            pi[begin+i] = max(pi[begin+i],i+1)
            
    return pi

def getPartialMatch(N):
    m = len(N)
    pi = [0]*m
    
    begin,matched = 1,0
    while (begin+matched) <m:
        print(begin, matched, begin+matched-1)
        if N[begin+matched] == N[matched]:
            matched+=1
            pi[begin+matched-1] = matched
        else:
            if matched==0:
                begin+=1
            else:
                begin +=matched - pi[matched-1]
                matched = pi[matched-1]
    
    return pi
print(list("ababbaba"))
print(getPartialMatchNaive('ababbaba'))
print(getPartialMatch('ababbaba'))