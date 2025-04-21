# https://www.acmicpc.net/problem/1744
# 수 묶기
N=int(input())
arr=[int(input()) for i in range(N)]
arr.sort()
nextSerial=0
for i in range(1,N+1):
    if arr[i-1]<0:
        nextSerial=i
if nextSerial!=N and arr[nextSerial]==0:
    zero_chk=True
else:
    zero_chk=False
l_arr= arr[:nextSerial]
r_arr= arr[nextSerial + zero_chk:]
print(l_arr,r_arr)
cnt=0
l_start=0
r_start=0
while len(l_arr)>l_start+1:
    cnt+=l_arr[l_start]*l_arr[l_start+1]
    l_start+=2
while len(r_arr)>r_start+1:
    cnt+=max(r_arr[len(r_arr)-r_start-1]*r_arr[len(r_arr)-r_start-2],r_arr[len(r_arr)-r_start-1]+r_arr[len(r_arr)-r_start-2])
    r_start+=2
if len(r_arr) != r_start:
    cnt += r_arr[0]
if zero_chk==False:
    if len(l_arr)!=l_start:
        cnt+=l_arr[-1]

print(cnt,l_start,r_start)