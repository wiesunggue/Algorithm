from collections import deque

N = int(input())
arr = list(map(int, input().split()))

ans = 1
cnt = 1
m = arr[0]
dq = deque([(m,0)])
print(cnt)

for i in range(1,N):
    cnt += 1
    while dq and dq[-1][0] <= arr[i]:
        data, idx = dq.pop()
        if data < arr[i]:
            cnt += idx - (dq[-1][1] if dq else -1)
        b_idx = idx


    dq.append((arr[i], i))
    print(dq)
    ans += cnt
    print(i,cnt)
print(ans)


'''
7
3 1 4 2 5 2 4
ans 

4
3 1 4 2
ans 14

3
2 2 1
ans 6

3
1 1 1
ans 6

5
1 2 3 4 5
ans 15

5
5 4 3 2 1
ans 15

5
1 2 3 2 1
'''