#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#백준 - 토마토 7576

from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

m, n = map(int, input().split())

farm = []
for i in range(n):
            farm.append(list(map(int, input().split())))
        
  
queue = deque()

for i in range(n):
    for j in range(m):
        if farm[i][j] == 1:
            queue.append([i, j])
        
        
def bfs():
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if farm[nx][ny] == 0:
                    farm[nx][ny] = farm[x][y] + 1
                    queue.append([nx, ny])
                    
bfs()

check = 1
result = -1

for i in farm:
    for j in i:
        if j == 0:
            check = 0
            
        result = max(result, j)

        
if check == 0:
    print(-1)
elif result == 1:
    print(0)
else:
    print(result-1)

# https://it-garden.tistory.com/174


# In[ ]:




