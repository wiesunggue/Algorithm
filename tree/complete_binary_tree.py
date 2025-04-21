N = int(input())
data = list(map(int,input().split()))
node = [0]*(len(data)+1)
nextSerial = 0
def recur(n):
    global nextSerial
    if n>len(data):
        return
    recur(n*2)
    node[n] = data[idx]
    idx += 1
    recur(n*2+1)

recur(1)
for i in range(N):
    for j in range(2**i):
        print(node[2**i+j],end=' ')
    print()

