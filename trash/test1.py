import random
import numpy as np
import matplotlib.pyplot as plt

T=10**-5 # 두꼐가 10um
N=1*10**-3 # 프로브 간격이 1mm
copper = 0.3*10**-3 # 구리선 간격이 0.6mm
sigma = 1000 # 비저항이 1000 Ohm * m

size = 100000
data = np.array([0 for i in range(size)],dtype=np.float64)
for i in range(size):
    L1 = random.random()*6
    L2 = random.random()*6
    t1=L1*L2/(L1+L2)
    t2=(6-L1)*(6-L2)/((6-L1)+(6-L2))
    print(t1,t2)
    ans1 = t1*t2/(t1+t2)/(4) # copper저항
    ans2 = 1/(6) # glass 저항
    ans3 = ans1*ans2/(ans1+ans2)/4
    ans3 = ans3/4 # 4핀 접근
    print(ans1,ans2,ans3)
    data[i]= sigma/T*ans3# copper+glass저항

print("저항 최솟값: ",np.min(data))
print("저항 평균: ",np.mean(data))
plt.hist(data,bins=100)
plt.show()