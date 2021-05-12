#10026 적록색약
#적록색약이 아닌 사람은 기존의 BFS와 동일하게 풀 수 있고, 적록색약인 사람은 R,G를 같은 블록을 취급해서 풀 수 있다

import sys
from collections import deque
input= sys.stdin.readline
n=int(input())
graph=list()
visited=[[False]*n for i in range(n)]
for i in range(n):
    graph.append(list(map(str, input().strip())))

def bfs(x,y,color):
    queue=deque()
    queue.append((x,y,color))
    visited[x][y]=True
    while queue:
        x,y,color= queue.popleft()
        for dx,dy in (1,0),(-1,0),(0,1),(0,-1):
            nx=x+dx
            ny=y+dy
            if 0<=nx<n and 0<=ny<n:
                if not visited[nx][ny] and graph[nx][ny]==color:
                    visited[nx][ny]=True
                    queue.append((nx,ny,color))

def color_bfs(x,y,color):
    queue=deque()
    # print(x,y,color)
    queue.append((x,y,color))
    color_visited[x][y]=True
    while queue:
        x,y,color= queue.popleft()
        for dx,dy in (1,0),(-1,0),(0,1),(0,-1):
            nx=x+dx
            ny=y+dy
            if 0<=nx<n and 0<=ny<n and not color_visited[nx][ny]:
                if color=="R":
                    if graph[nx][ny]==color or graph[nx][ny]=="G":
                        color_visited[nx][ny]=True
                        queue.append((nx,ny,color))
                elif color=="G":
                    if graph[nx][ny]==color or graph[nx][ny]=="R":
                        color_visited[nx][ny]=True
                        queue.append((nx,ny,color))
                else:
                    if graph[nx][ny]==color:
                        color_visited[nx][ny]=True
                        queue.append((nx,ny,color))
cnt=0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j,graph[i][j])
            cnt+=1


color_cnt=0
color_visited=[[False]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        if not color_visited[i][j]:
            color_bfs(i,j,graph[i][j])
            color_cnt+=1
print(cnt, color_cnt)