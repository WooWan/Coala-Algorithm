from collections import deque
import numpy as np

move = [1, -1, 0, 0]


def bfs():
    result = 0
    while que:
        for _ in range(len(que)):
            x, y = que.popleft()
            for i in range(4):
                nx = x + move[i]
                ny = y + move[3-i]
                if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
                        arr[nx][ny] = 1
                        que.append([nx, ny])
        result+=1
    return result

m, n = map(int, input().split())
arr, que = [], deque()
arr = np.zeros([n,m])

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        arr[i][j] = row[j]
        if row[j] == 1:
            que.append([i, j])


result = bfs() - 1
if(np.count_nonzero(arr==0)!=0):
    print(-1)
    exit()
print(result)
