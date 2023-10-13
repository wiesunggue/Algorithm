from scipy.stats import norm
import numpy as np
from math import sqrt
p = norm.cdf(-28)
print(p)
print(np.random.binomial(5000,0.5))
m=2500
var=1250
Z = (3500-m)/sqrt(var)
print(Z)
a=0.25/sqrt(0.1)
print(norm.cdf(a))
def f(a,b):
    return a^b
print('start')
def find_ans(k):
    ans = 0
    for i in range(k):
        for j in range(k):
#            print(f(i,j),' ',end='')
            ans+=f(i,j)
#        print()
    return ans
for i in range(2,20):
    print(i,find_ans(i),find_ans(i)/i**2)