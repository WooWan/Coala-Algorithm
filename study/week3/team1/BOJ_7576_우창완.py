import sys
from collections import deque

m,n= map(int, sys.stdin.readline().split())
ground=list()

for i in range(n):
    ground.append(list(map(int, sys.stdin.readline().split())))
queue=deque()

def bfs():
    while queue:
        x, y, cnt = queue.popleft()
        for dx, dy in (1,0), (-1,0), (0,1), (0,-1):
            nx= x+dx
            ny= y+dy
            if 0<=nx<n and 0<=ny<m:
                if ground[nx][ny]==0:
                    ground[nx][ny]=1
                    queue.append((nx,ny, cnt+1))
    return cnt

for i in range(n):
    for j in range(m):
        if ground[i][j]==1:
            queue.append((i,j,0))
answer=bfs()
isTomato=True
for i in range(n):
    if 0 in ground[i]:
        isTomato=False
print(answer if isTomato else -1)

