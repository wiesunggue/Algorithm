from math import log2
a,b,c=map(int,input().split())
if c==0:
    print(min(b,int(log2(a+0.9))))
else:
    print(min(int(log2(c + 0.1)) + b, int(log2(a + 0.9))))

import os
print(os.path.basename('E:\graduate\Korea_MIUD'))
print(*[file for file in os.path.basename('E:\graduate\Korea_MIUD') if file.endswith('.inc')],sep='\n')
