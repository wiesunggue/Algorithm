import time
start = time.time()
a=[]
for i in range(2000000):
    a.append(i)
end = time.time()
print(f'{end-start:.4f}')