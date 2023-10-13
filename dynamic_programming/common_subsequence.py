str1 = input()
str2 = input()
arr = [[0 for _ in range(4000)]for _ in range(4000)]
for i in range(len(str1)):
    for j in range(len(str2)):
        if str1[i]==str2[j]:
            if i==0 or j==0:
                arr[i][j]=1
            else:
                arr[i][j]+=arr[i-1][j-1]+1

print(max(map(max,arr)))