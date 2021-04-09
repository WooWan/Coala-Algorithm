#!/usr/bin/env python
# coding: utf-8

# In[34]:


trial = int(input())

grapejuice = list()
grapejuice.append(0)
for i in range(trial):
    juice = int(input())
    grapejuice.append(juice)
grapejuice.append(0) # 1 입력시 index error 방지 (grapejuice index 2가 없는 상태가 되어서 error)
temp = [0]*(trial+2)
 # 시도가 2회 이하(1회,2회)는 다 마시기 가능
temp[1] = grapejuice[1]
temp[2] = grapejuice[1] + grapejuice[2]
if trial<3:
    result = temp[2]
    
for i in range(3,trial+1):
    temp[i] = max(grapejuice[i]+grapejuice[i-1]+temp[i-3],grapejuice[i]+temp[i-2],temp[i-1])

print(temp[trial])

