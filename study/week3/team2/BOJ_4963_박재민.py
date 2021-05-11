from collections import deque
import numpy as np

dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]


def bfs():
    result = 0
    while que:
        x, y = que.popleft()
        if(arr[x][y] == -1): continue
        else: arr[x][y] = -1 # flag for visited
        result += 1
        island_queue = deque()
        while 1:
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1:
                    arr[nx][ny] = -1
                    island_queue.append([nx,ny])
            if not(island_queue): break
            x, y = island_queue.popleft()
    return result

while 1:
    m, n = map(int, input().split())
    if(m == 0 and n == 0): break
    que = deque()
    arr = np.zeros([n, m])

    for i in range(n):
        row = list(map(int, input().split()))
        for j in range(m):
            arr[i][j] = row[j]
            if row[j] == 1:
                que.append([i, j])
    print(bfs())
