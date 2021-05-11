#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#백준 - 4963 섬의 개수

from collections import deque

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def bfs(x, y):
    
    queue = deque()
    queue.append([x, y])
        
    while queue:    
        x, y = queue.popleft()
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    queue.append([nx, ny])
    

while True:
    w, h = map(int, input().split())
    
    if w == 0 and h == 0:
        break
    else:
        graph = []
        for i in range(h):
             graph.append(list(map(int, input().split())))
                
        n = 0
        
        for i in range(h):
            for j in range(w):
                if graph[i][j] == 1:
                    n = n + 1
                    bfs(i, j)


        print(n)
        
        

# https://it-garden.tistory.com/171


# ## 
