#!/usr/bin/env python
# coding: utf-8

# In[4]:


from _collections import deque

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
        
    island = []
    queue = deque()
    # 8방향 (상하좌우 + 대각선)
    dx = [1,-1,0,0,1,-1,1,-1]
    dy = [0,0,1,-1,1,-1,-1,1]
    
    for i in range(h):
        island.append(list(map(int,input().split())))

    cnt = 0
    for i in range(h):
        for j in range(w):
            if island[i][j] == 1:
                queue.append([i, j])
                # 방문표시
                island[i][j] = 2

                while queue:
                    a, b = queue.popleft()
                    for k in range(8):
                        x = a + dx[k]
                        y = b + dy[k]
                        # 인덱스 초과하지 않는 경우 인접값이 1(땅)이면 2로 바꾸고(visit), 큐에 추가
                        if 0 <= x < h and 0 <= y < w:
                            if island[x][y] == 1:
                                queue.append([x, y])
                                island[x][y] = 2

                # 이어진 육지 다돌면 count += 1
                else:
                    cnt += 1

    print(cnt)

