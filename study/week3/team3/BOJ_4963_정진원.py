import sys
from collections import deque

while(True):
    w, h = map(int, sys.stdin.readline().split())

    if(h == 0 & w == 0):
        break

    graph = []
    visited = [[False] * w for _ in range(h)]

    for i in range(h):
        maps = list(map(int, sys.stdin.readline().split()))
        graph.append(maps)

    def bfs(x, y, graph, visited):
        queue = deque()
        queue.append((x,y))
        visited[x][y] = True
        
        while queue:
            x, y = queue.popleft()
            for dx, dy in (1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1):
                nx = x + dx
                ny = y + dy
                if 0<= nx <h and 0<= ny <w:
                    if visited[nx][ny] == False and graph[nx][ny] == 1:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
        return
    
    cnt = 0

    for x in range(h):
        for y in range(w):
            if not visited[x][y] and graph[x][y] == 1:
                bfs(x, y, graph, visited)
                cnt += 1

    print(cnt)