N = int(input())
p_arr = list(map(int,input().split()))
K = int(input())

def p_th_sum(p):
    max_num=K
    ans=0
    while max_num!=0:
        max_num=max_num//p
        ans+=max_num

    return ans
ans=0
for i in p_arr:
    ans+=p_th_sum(i)

print(ans)