# https://www.acmicpc.net/problem/24231
# 해석
s = '10'*3
MAX_NUM = 10**9+7
dp = [[-1 for i in range(len(s)+1)] for j in range(len(s)+1)]
def find_case(start,end):
    if dp[start][end]!=-1:
        return dp[start][end]
    #print("STARTend",start,end)
    #print(s)
    if (end-start)<=1:
        if s[start:end+1]=='01' or s[start:end+1]=='10':
            dp[start][end]=1
            return 1
        else:
            dp[start][end]=0
            return 0
    recur = 0
    for i in range(start+1,end):
        #print(i,start,end)
        if int(s[start])+int(s[i])==1:
            print(start,i,end)
            #print('spliter',s,s[start:i+1],'b',s[i+1:end+1])
            recur += find_case(start,i)*find_case(i+1,end)
    #print(start,end)
    if int(s[start])+int(s[end])==1:
        recur+= find_case(start+1,end-1)
    #recur -= find_case(start,start+1)*find_case(end-1,end)*find_case(start+2,end-2)
    #if int(s[0])+int(s[1])==1:
    #    parallel = find_case(s[2:])

    #print(s,recur)
    dp[start][end]=recur
    return recur % MAX_NUM

print('ans',find_case(0,len(s)-1))
print(dp)
print('01',find_case(0,1))
print('03',find_case(0,3))
print('25',find_case(2,5))
print('14',find_case(1,4))
print(find_case(0,1))
print(find_case(0,1))