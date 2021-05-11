#!/usr/bin/env python
# coding: utf-8

# In[26]:


from collections import deque

# 기본 세팅 (box, bfs용 큐, 방향벡터)
box = []
queue = deque()
dx = [1,-1,0,0]
dy = [0,0,1,-1]

# 입력
m,n = map(int, input().split())
for i in range(n):
    box.append(list(map(int,input().split())))    

# bfs 
for i in range(n):
    for j in range(m):
        if(box[i][j] == 1):
            queue.append([i,j])

while queue:
    a,b = queue.popleft()
    for i in range(4):
        x = a + dx[i] # x축으로 <-  or  ->
        y = b + dy[i] # y축으로 위로 또는 밑으로
        # 인덱스 초과하지 않는 경우 + 그 인접값이 0이면 1로 바꿔주고 큐에 추가하기(bfs)
        # 주의! x 랑 y가 원래 생각하는 가로 세로가 아님!
        if 0 <= x < n and 0 <= y < m and box[x][y] == 0:
            box[x][y] = box[a][b] + 1
            queue.append([x,y])

            
day = 0
for i in range(n):
    for j in range(m):
        # 익지 않은 토마토가 있는 경우
        if(box[i][j] == 0):
            print(-1)
            exit()
        if(day < box[i][j]):
            day = box[i][j]
            
print(day-1)

