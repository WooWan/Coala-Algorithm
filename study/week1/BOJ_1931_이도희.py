#!/usr/bin/env python
# coding: utf-8

# In[38]:


trial = int(input())

meeting = list()
for i in range(trial):
    start, end = map(int,input().split(" "))
    meeting.append([start,end])
meeting.sort() # 시작순 시간 정렬
temp = sorted(meeting, key = lambda meeting:meeting[1]) # 이후 끝나는 시간대로 정렬 
#>> 결론적으로 끝나는거 기준 -> 시작 기준 으로 정렬됨

first = temp[0][1] #첫 번째 시간
result = 1 # 첫 번째 거 확정

for i in range(1, trial):
    if(first <= temp[i][0]): 
        first = temp[i][1] # 끝시간이 제일 짧은 시간과 시작이 겹치거나 더 큰 것을 다시 기준으로!
        result += 1 # 회의 하나 더 확정된거니 count 증가
print(result)            

