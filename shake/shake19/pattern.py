from collections import Counter
position = {'1':(3,1),'2':(3,2),'3':(3,3),'4':(2,1),'5':(2,2),'6':(2,3),'7':(1,1),'8':(1,2),'9':(1,3)}
checker = {str(i):0 for i in range(10)}
reversed_position = {str(v):k for k,v in position.items()}
N = int(input())
pos = lambda x:position[x]
arr = list(map(pos,input().split()))
print(arr)
print(reversed_position)
bx,by=arr[0]
a=Counter(arr)
print(a)
ans='YES' if max(a.values())==1 else 'NO'
if len(arr)<3:
    ans="NO"
print(ans)
for x,y in arr:
    checker[reversed_position[str((x, y))]] = 1
    if x==bx and y==by:
        continue
    tx=(x+bx)
    ty=(y+by)
    print(tx,ty)
    if tx%2!=0 or ty%2!=0:
        print(reversed_position[str((tx//2,ty//2))])
        bx,by=x,y
        continue
    if checker[reversed_position[str((tx//2,ty//2))]]==1:
        continue
    print('************')
    print(checker[reversed_position[str((tx//2,ty//2))]])
    print("*********",x,y,tx,ty)
    ans='NO'
    break
print(ans)