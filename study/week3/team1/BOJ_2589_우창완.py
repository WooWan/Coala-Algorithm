import sys
from collections import deque

n,m = map(int, input().split())

ground=list()
for i in range(n):
    ground.append(list(map(str, sys.stdin.readline().strip())))


def bfs(visited, x,y):
    queue=deque()
    queue.append(x,y,0)
    visited[x][y]=True
    while queue:
        x,y,cnt= queue.popleft()
        for dx,dy in (1,0), (-1,0),(0,1), (0,-1):
            nx=x+dx
            ny=y+dy
            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny] and ground[nx][ny]=="L":
                    visited[nx][ny]=True
                    queue.append((nx,ny, cnt+1))
    return cnt
answer=0
for i in range(n):
    for j in range(m):
        if ground[i][j]=="L":
            visited=[[False]*m for _ in range(n)]
            answer= max(answer,bfs(visited, i,j))

print(answer)