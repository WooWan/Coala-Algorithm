from collections import deque

q = deque()
dx = [-1,-1,-1,0,1,1,1,0]
dy = [-1,0,1,1,1,0,-1,-1]

def bfs(x,y):
    mutex[x][y] = True
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for i in range(8):
            ax = x + dx[i]
            by = y + dy[i]
            if 0<=ax<h and 0<=by<w and graph[ax][by]==1 and not mutex[ax][by]:
                mutex[ax][by]=True
                q.append((ax,by))


while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break
        exit()


    graph = [list(map(int, input().split())) for _ in range(h)]
    mutex = [[False] * w for _ in range(h)]
    result = 0
while 1:
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                if mutex[i][j] == False:
                    bfs(i, j)
                    result += 1
                else:
                    continue
    print(result)
