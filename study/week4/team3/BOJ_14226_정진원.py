import sys
from collections import deque

S = sys.stdin.readline().strip()

emoticon = 1
clipboard = 0
currentTime = 0


def copy():
    clipboard = emoticon
    currentTime += 1

def paste():
    emoticon += clipboard
    currentTime += 1

def delete():
    emoticon -= 1
    currentTime += 1

while(S == emoticon):

print(currentTime)

# visited = [[False] * (n+1) for _ in range(n+1)]
# graph = [[0] * (n+1) for _ in range(n+1)]
# currentTime = 0

# def bfs(ecnt, ccnt, currentTime, visited, graph):
#     q = deque()
#     # (화면에 있는 이모티콘 개수, 클립보드에 저장된 이보티콘 개수, 현재 초)
#     q.append((ecnt, ccnt, currentTime))
#     visited[ecnt][ccnt] = True
#     while queue:
#         ecnt, ccnt, currentTime = q.popleft()

#         next_ccnt = ecnt
#         if not visited[ecnt][next_ccnt]:
#             visited[ecnt][next_ccnt] = True
#             q.append((ecnt, next_ccnt, currentTime+1))
    
#         if ccnt > 0:
#             next_ecnt = ecnt + ccnt
#             if next_ecnt <= 1000 and ccnt <= 1000


#     return currentTime

# print(bfs(1, 0, 0, visited, graph))