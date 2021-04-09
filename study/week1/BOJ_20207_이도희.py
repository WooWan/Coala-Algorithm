#!/usr/bin/env python
# coding: utf-8

# In[9]:


trial = int(input())
#인덱스는 0부터시작, but 우리는 입력을 1부터 받아 -> 365만들기 위해 배열 1칸더필요
schedule = [0]*367
scheduleend = 0
for i in range(trial):
    start, end = map(int,input().split(" "))
    scheduleend = max(scheduleend, end)
    for i in range(start,end+1):
        schedule[i]+=1         
width = 0
height = 0
result = 0
for i in range(1,scheduleend+2):
    if(schedule[i] != 0): 
        width += 1
        height = max(height, schedule[i])
    else: #중간이 비어서 다른 사각형이 되는 경우 or 365까지 간 경우(그래서 맨 끝칸 빈칸으로 하나 만들기 -> 배열 1칸 더 필요)
        result += width*height
        width = 0 #새로운 사각형 시작해야하니 초기화
        height = 0
        
print(result)

