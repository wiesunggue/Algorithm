N=int(input())
ans = 'Yes'*100
for i in range(N):
    s=input()
    print("YES" if ans.find(s)!=-1 else "NO")
    