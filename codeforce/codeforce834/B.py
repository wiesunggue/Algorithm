def overlap_checker(lis:list) -> bool: # 중복되면 false 아니면 참
    return len(set(lis))==len(lis)

    
def shortage(lis:list) -> int: # 필요한 최소 값
    m=max(lis)
    return (m*(m+1)//2)-sum(lis)

def solution():
    T = int(input())
    for test in range(T):
        m,s = map(int,input().split())
        arr=list(map(int,input().split()))
        short=s-shortage(arr)
        M = max(arr)+1
        if overlap_checker(arr)==False or short<0:
            print("NO")
        else:
            stop=False
            while short>=0:
                if short==0:
                    stop=True
                    break
                short-=M
                M+=1

            print("YES" if stop==True else "NO")

solution()