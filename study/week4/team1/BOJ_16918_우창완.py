#16918 봄버맨 S1
#체감상 S1보다 난이도가 높고(G5?), 문제를 보고 패턴이 바로 보이지가 않아 1초, 2초,3초일 때 상황을 그렸고,
# second가 짝수일 때 폭탄이 설치되고 홀수일 때 터지는 것을 찾을 수 있었습니다.
# 처음에 폭탄이 터지는 timing을 queue에 넣고 queue에 있는 폭탄의 i,j 좌표를 터뜨렸지만 예외상황을 처리하며 시간초과가 발생하게 되었고
# grid에 터지는 시간을 저장한뒤 해당하는 시간이 되면 체크해서 터지도록 만들었습니다
import sys

r,c,n = map(int, sys.stdin.readline().split())
if n%2==0:
    for i in range(r):
        print('O'*c)
    exit()
elif n == 1:
    for _ in range(r):
        print(input())
else:
    graph=list()
    for i in range(r):
        graph.append(list(map(str, sys.stdin.readline().strip())))
    graph=[list(input()) for i in range(r)]
    # grid = [list(input()) for i in range(r)]
    bomb= [[-1]*c for i in range(r)]
    for i in range(r):
        for j in range(c):
            if graph[i][j]=="O":
                bomb[i][j]=3

    second=1
    def bfs(bomb,graph,second):
        isbomb=deque()
        for i in range(r):
            for j in range(c):
                if bomb[i][j]==second: isbomb.append((i,j))

        while isbomb:
            x,y=isbomb.popleft()
            graph[x][y]="."
            for dx, dy in (1,0),(-1,0),(0,1),(0,-1):
                nx=dx+x
                ny=dy+y
                if 0<=nx<r and 0<=ny<c:
                    # print(nx,ny)
                    bomb[nx][ny]=-1
                    graph[nx][ny]="."

    while second<n:
        second+=1
        if second%2==0:
            for i in range(r):
                for j in range(c):
                    if graph[i][j]==".":
                        graph[i][j] ="O"
                        bomb[i][j]=second+3
        if second%2==1:
            bfs(bomb,graph,second)


    for i in range(r):
        for j in range(c):
            print(graph[i][j], end='')
        print()
