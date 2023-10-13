#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 라이브러리 불러오기
import numpy as np
import pandas as pd
import math
from math import e
ln = np.log  # assign the numpy log function to a new function called ln
from scipy.stats import norm

import warnings
warnings.filterwarnings('ignore')

import sys
import time
import datetime


# In[2]:


df = pd.read_csv("../baseball//computations//MLB datasets-2021-demeaned.csv")
L = 60; Time = 6
m = df[["m"]].values.flatten() # 순서대로 m을 가짐(선수 상관 x)
x1 = df[["x_1"]].values.flatten() #순서대로 x1을 가짐(선수 상관 x)
x2 = df[["x_2"]].values.flatten() #순서대로 x2를 가짐(선수 상관 x)

Z_demd = df.drop(['Team','Player','month','m','x_1','x_2'], axis=1)
Z_demd.head()


# ---

# In[3]:


z_p = Z_demd.loc[:,["Intercept","WPA", "Cent%",
                           "BABIP","BB/K", "LD%", "GB%", "Oppo%"]]
z_q = Z_demd.loc[:,["Intercept","WPA", "Cent%",
                           "FB%", "HR/FB", "Pull%"]]

####################################################
B_p = [-2.05,0.06,-0.64,3.37,0.14,-0.2,-0.16,0.50]
B_q = [-0.5,0.72,-0.64,0.60,0.90,1.83]
params = B_p + B_q
####################################################
d = len(params)

phi=100


# ---

# In[5]:


def fp(tta,bps,phi): # 함수의 목적은?
    bps[k] = tta
    Z_Bp = z_p.dot(np.diag(bps))
    logit_p = np.array(Z_Bp.sum(axis=1))
    ests = (tta * (z_p.iloc[:, [k]].to_numpy().flatten()) * x1 - m*ln(1+np.exp(logit_p))).sum()-(tta**2)/(2*(phi**2))
    return ests

def fq(tta,bqs,phi): # 함수의 목적은?
    bqs[k] = tta
    Z_Bq = z_q.dot(np.diag(bqs))
    logit_q = np.array(Z_Bq.sum(axis=1))
    ests = (tta * (z_q.iloc[:, [k]].to_numpy().flatten()) * x2 - x1*ln(1+np.exp(logit_q))).sum()-(tta**2)/(2*(phi**2))
    return(ests)


# In[6]:


d = len(params)
s = 2.4/math.sqrt(d)

np.random.seed(10)
eps = np.random.uniform(0,1,size=d)*0.05 # 0~1사이, 파라메터 개수 만큼 균등분포에서 랜덤값을 추출
Var_0  = np.random.uniform(5,20,size=d) # 5~20 사이의 랜덤값 추출
def EmpVar(nth):
    if i == 0:
        rslt = Var_0[nth]
    elif i == 1:
        rslt = s*eps[nth]
    else:
        rslt = s*np.var(u.iloc[0:(i-1),nth]) + s*eps[nth]
    return(rslt)


# ---

# In[7]:


itr = 6000
burn = 1000
thin = 1


# ---

# In[8]:


u_colnames = ["bp" + str(num1) for num1, in zip(range(len(B_p)))]+[
    "bq" + str(num1) for num1, in zip(range(len(B_q)))]

u = np.zeros((itr+1, d)) # 6001*14의 행렬 선언
u = pd.DataFrame(u, columns = u_colnames) #판다스로 형변환 + column 이름 붙이기
u.iloc[0,:] = params
print(u.head())