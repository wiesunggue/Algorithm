N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = [B[A[i]-1] for i in range(N)]
result = "Yes"
for i in range(N):
    if ans[i] != i+1:
        result = "No"
        break
print(result)