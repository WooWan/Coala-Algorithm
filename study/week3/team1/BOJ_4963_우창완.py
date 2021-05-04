from collections import deque
import sys


def bfs(x,y,visited):
    queue=deque()
    queue.append((x,y))
    while queue:
        x,y= queue.popleft()
        for dx,dy in (1,0),(0,1),(0,-1),(-1,0),(1,1),(-1,-1), (1,-1), (-1,1):
            nx=x+dx
            ny=y+dy
            if 0<=nx<n and 0<= ny<m:
                if not visited[nx][ny] and land[nx][ny]==1:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
    # print(visited)

while True:
    m,n= map(int, sys.stdin.readline().split())
    cnt=0
    if n==0 and m==0: break
    visited = [[False]*m for _ in range(n)]
    land=list()
    for i in range(n):
        land.append(list(map(int, sys.stdin.readline().split())))

    for i in range(n):
        for j in range(m):
            if land[i][j]==1 and not visited[i][j]:
                cnt+=1
                visited[i][j]=True
                bfs(i,j,visited)
    print(cnt)

