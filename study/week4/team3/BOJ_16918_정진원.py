import sys
from collections import deque

r, c, n = map(int, sys.stdin.readline().split())

graph = []
visited = [[False] * c for _ in range(r)]

for i in range(r):
    graph.append(list(sys.stdin.readline().strip()))

def bfs(x, y, graph, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:        
        x, y = queue.popleft()
        graph[x][y] = '.'
        for dx, dy in (1,0), (-1,0), (0,1), (0,-1):
            nx = x + dx
            ny = y + dy
            if 0<= nx < r and 0<= ny < c :
                if not visited[nx][ny] and graph[nx][ny] == 'O':
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                elif not visited[nx][ny] and graph[nx][ny] == '.':
                    visited[nx][ny] = True
                    graph[nx][ny] = '.'
                elif visited[nx][ny]:
                    graph[nx][ny] = '.'
        

if n % 2 == 1 and n % 4 == 1:
    for i in range(r):
        for j in range(c):
            print(graph[i][j], end='')
        print('')
elif n % 2 == 0:
    for i in range(r):
        for j in range(c):
            graph[i][j] = "O"
            print(graph[i][j], end='')
        print('')
elif n % 2 == 1 and n % 4 6 == 3:
    for i in range(r):
        for j in range(c):
            if not visited[i][j] and graph[i][j] == 'O':
                bfs(i, j, graph, visited)
            elif not visited[i][j] and graph[i][j] == '.':
                visited[i][j] = True
                graph[i][j] = 'O'

    for i in range(r):
        for j in range(c):
            print(graph[i][j], end='')
        print('')