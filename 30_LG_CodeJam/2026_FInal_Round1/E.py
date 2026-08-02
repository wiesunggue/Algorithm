N = int(input())
arr = list(map(int, input().split()))

MAX_SIZE = 998244353


ans1 = N # 항상 정답이므로 nC1
ans2 = N*(N-1)//2 # 항상 정답이므로 nC2
ans3 = 0
ans4 = 0

# 길이 3인 경우
for i in range(N):
    LL = 0
    for j in range(i):
        if arr[j]<arr[i]:
            LL += 1
    RL = (arr[i]-1)-LL
    LG = i-LL
    RG = N-i-1-RL
    ans3 += (LL*RL + LG*RG)%MAX_SIZE
    ans3 %= MAX_SIZE

# 길이 4인 경우 Ai<Ap,Aq<Aj or Aj<Ap,Aq<Ai 인 경우
# => Ai<Aj 이면 Ai<Ap,Aq<Aj 만 확인
# => Aj<Ai 이면 Aj<Ap,Aq<Ai 만 확인
# => low<Ap,Aq<high 이면 된다
# dp4[i][j] = L(i,j) * R(i,j)
# L은 i보다 작은 수 중에 low<Ap<high 인 수
# R은 j보다 큰 위치에서 low<Aq<high 인 수
idx_arr = [[0]*(N+2) for _ in range(N)]
for i in range(N+1): # i = high
    for j in range(N): # j = idx
        idx_arr[j][i] = idx_arr[j-1][i] + int(arr[j]<=i)

print(*idx_arr,sep='\n')

for i in range(1,N):
    for j in range(i + 1, N):
        low = min(arr[i], arr[j])
        high = max(arr[i], arr[j])
        ans4 += (idx_arr[i-1][high-1]-idx_arr[i-1][low]) * (high - low - 1 - (idx_arr[j][high-1]-idx_arr[j][low])) # L * R
        ans4 %= MAX_SIZE

print(ans1, ans2, ans3, ans4)
print((ans1 + ans2 + ans3 + ans4)%MAX_SIZE)


'''

6
1 3 5 6 2 4
ans 38

10
1 3 9 2 6 4 5 8 7 10

3
1 3 5
122
'''

