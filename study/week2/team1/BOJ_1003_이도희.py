#!/usr/bin/env python
# coding: utf-8

# In[84]:


trial = int(input())
temp = [0]*10000

result = [0,0]
temp[0] = [1,0]
temp[1] = [0,1]
temp[2] = [1,1]
for i in range(trial):
    fibonum = int(input())
    if(fibonum == 0):
        result = temp[0]
    elif(fibonum == 1):
        result = temp[1]
    elif(fibonum == 2):
        result = temp[2]
    elif(fibonum > 2):
        for j in range(3,fibonum+1):
            temp[j] = [temp[j-1][0]+temp[j-2][0], temp[j-1][1]+temp[j-2][1]]
        result = temp[fibonum]
    print("%d %d"%(result[0],result[1]))

