
N = 8
arr = [[1,2],[3,4],[5,6],[7,8],[],[],[],[]]
while True:
    if arr[0] != []:
        break
    arr.pop(0)
    arr.append([])

# 7. 어항 올리기(2단)
for i in range(N//4):
    arr[N//2- i-1].extend(reversed(arr[i]))
    arr[i] = []
# 밀기
while True:
    if arr[0] != []:
        break
    arr.pop(0)
    arr.append([])
print(arr)
