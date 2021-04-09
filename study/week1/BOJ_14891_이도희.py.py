#!/usr/bin/env python
# coding: utf-8

# In[13]:


from collections import deque
         
gear = []
# 톱니바퀴 만들기
for i in range(4):
    gear.append(deque(list(input())))

trial = int(input())
for i in range(trial):
    gearnum, direction = map(int,input().split(" "))
    num = gearnum-1
    right = gear[num][2] # 새 시도마다 초기화해주기
    left = gear [num][6]
    gear[num].rotate(direction)
    origindirection = direction
    
    
#Right
    direction = origindirection
    for i in range(num,3,1):
        if right != gear[i+1][6]: # 오른쪽 톱니와 비교해서 다른 극이면 돌림
            right = gear[i+1][2]
            direction = -direction
            gear[i+1].rotate(direction)
        else:
            break
           
#Left
    direction = origindirection
    for i in range(num,0,-1):
        if left != gear[i-1][2]: # 왼쪽 톱니와 비교해서 다른 극이면 돌림
            left = gear[i-1][6]
            direction = -direction
            gear[i-1].rotate(direction) 
        else:
            break
    

result = 0
for i in range(4):
    if gear[i][0] == '1':
        result += 2**i
print(result)

