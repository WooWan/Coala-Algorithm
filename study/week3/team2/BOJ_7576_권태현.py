import sys
from collections import deque
r = sys.stdin.readline()

M,N = map(int,r.split())
tomato = []
q = deque()

for _ in range(N):
    tomato.append(list(map(int,input().split())))

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            q.append([i,j])

def bfs():
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    while q:
        a,b = q.popleft()

        for i in range(4):
            x = a+dx[i]
            y = b+dy[i]
            if 0<=x<N and 0<=y<M and tomato[x][y] ==0:
                tomato[x][y] = tomato[a][b]+1
                q.append([x,y])

bfs()

date = 0
for i in range(N):
    for j in range(M):
        if date < tomato[i][j]:
            date = tomato[i][j]
        if tomato[i][j]==0:
            print(-1)
        date = max(date,1)
print(date-1)
