#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
df=pd.read_csv('/content/SeoulBikeData.csv',encoding='ISO-8859-1')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df.head()

df.tail()

df=df.fillna(0)

df.describe

x1=df['Hour']
x2=df['Humidity(%)']
x3=df['Rainfall(mm)']
x4=df['Dew point temperature(°C)']
x5=df['Snowfall (cm)']
x6=df['Solar Radiation (MJ/m2)']
x7=df['Temperature(°C)']
x8=df['Wind speed (m/s)']
x9=df['Visibility (10m)']
y=df['Rented Bike Count']
size=x1.size
print(x1,x2,x3,x4,x5,x6,x7,x8,x9,y)

import random
x1_train=[]
x2_train=[]
x3_train=[]
x4_train=[]
x5_train=[]
x6_train=[]
x7_train=[]
x8_train=[]
x9_train=[]
y_train=[]

for j in range(0,1):
  for i in range(0,8760,2):
    x1_train.append(x1[i])
    x2_train.append(x2[i])
    x3_train.append(x3[i])
    x4_train.append(x4[i])
    x5_train.append(x5[i])
    x6_train.append(x6[i])
    x7_train.append(x7[i])
    x8_train.append(x8[i])
    x9_train.append(x8[i])
    y_train.append(y[i])

import random
x1_train=[]
x2_train=[]
x3_train=[]
x4_train=[]
x5_train=[]
x6_train=[]
x7_train=[]
x8_train=[]
x9_train=[]
y_train=[]

for j in range(1,300):
  for i in range(0,8760,2):
    x1_train.append(x1[i])
    x2_train.append(x2[i])
    x3_train.append(x3[i])
    x4_train.append(x4[i])
    x5_train.append(x5[i])
    x6_train.append(x6[i])
    x7_train.append(x7[i])
    x8_train.append(x8[i])
    x9_train.append(x8[i])
    y_train.append(y[i])

import random
x1_train=[]
x2_train=[]
x3_train=[]
x4_train=[]
x5_train=[]
x6_train=[]
x7_train=[]
x8_train=[]
x9_train=[]
y_train=[]

for j in range(300,600):
  for i in range(0,8760,2):
    x1_train.append(x1[i])
    x2_train.append(x2[i])
    x3_train.append(x3[i])
    x4_train.append(x4[i])
    x5_train.append(x5[i])
    x6_train.append(x6[i])
    x7_train.append(x7[i])
    x8_train.append(x8[i])
    x9_train.append(x8[i])
    y_train.append(y[i])

import random
x1_train=[]
x2_train=[]
x3_train=[]
x4_train=[]
x5_train=[]
x6_train=[]
x7_train=[]
x8_train=[]
x9_train=[]
y_train=[]

for j in range(600,1000):
  for i in range(0,8760,2):
    x1_train.append(x1[i])
    x2_train.append(x2[i])
    x3_train.append(x3[i])
    x4_train.append(x4[i])
    x5_train.append(x5[i])
    x6_train.append(x6[i])
    x7_train.append(x7[i])
    x8_train.append(x8[i])
    x9_train.append(x8[i])
    y_train.append(y[i])




#multiple linear regression

e=[]
ee=[]
def linear(m1,m2,m3,m4,m5,m6,m7,m8,m9,c):
  sum=0
  yp=[]
  for i in range(0,len(x8_train)):
    yp.append(m1*x1_train[i]+m2*x2_train[i]+m3*x3_train[i]+m4*x4_train[i]+m5*x5_train[i]+m6*x6_train[i]+m7*x7_train[i]+m8*x8_train[i]+m9*x9_train[i]+c)
    g=(y_train[i]-yp[i])**2
    sum=sum+g
  e.append(sum)
  ee.append(np.mod(sum,len(x1_train)))
  print(m1,m2,m3,m4,m5,m6,m7,m8,m9,c,np.mod(sum,len(x9_train)))
  sum=0

for i in range(1,100):
  linear(1+i,2+i,3+i,4+i,5+i,6+i,7+i,8+i,9+i,10+i,)



# In[ ]:




