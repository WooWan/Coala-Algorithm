#14226 G5 이모티콘
#문제를 보고 가장 먼저 최단 횟수-> BFS를 떠올릴 수 있어야합니다
s=int(input())
from collections import deque
visited=[[False]*1001 for _ in range(1001)]
def bfs(time,cnt,copy):
    queue=deque()
    queue.append((time, cnt, copy))
    while queue:
        time,cnt,copy=queue.popleft()
        visited[cnt][copy]=True
        if cnt==s:
            print(time)
            exit()
        else:
            if copy==0:
                queue.append((time+1, cnt, cnt))
            else:
                #이모티콘은 하나를 지우거나, 이모티콘 개수만큼 복사하거나, 이모티콘에 클립토드를 붙여넣기할 수 있다.끝~
                for cnt, copy in (cnt-1, copy),(cnt,cnt),(cnt+copy, copy):
                    if 0<cnt<1001:
                        if not visited[cnt][copy]:
                            visited[cnt][copy]=True
                            queue.append((time+1, cnt, copy))

bfs(0,1,0)