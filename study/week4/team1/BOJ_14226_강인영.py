#백준 14226 이모티콘 (https://hooongs.tistory.com/219 참고)

from collections import deque

s = int(input())

def bfs(s):
  q = deque()
  q.append([1, 0, 0]) #[현재 이모티콘 개수, 클립보드 개수, 횟수]

  #방문 리스트 만들기
  visited = [[False for _ in range(s+1)] for _ in range(s+1)]
  visited[1][0] = True


  while q:
    display, clip, cnt = q.popleft()

    if display == s: #화면에 있는 이모티콘이 전부이면 cnt그대로 반환
      return cnt

    #1번 -> 화면에 있는 이모티콘을 모두 복사해서 클립보드 저장 / 클립보드에 이모티콘을 복사하면 이전에 클립보드에 있던 내용은 덮어쓰기가 됨.
    if not visited[display][display]:
      visited[display][display] = True
      q.append([display,display, cnt+1])

    #2번 -> 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 / 클립보드가 비어있는 상태에는 붙여넣기 불가능하며 일부만 클립보드 복사 금지
    if display + clip <= s:
      if not visited[display + clip][clip]:
        visited[display+clip][clip] = True
        q.append([display+clip, clip, cnt+1])

    #3번 -> 화면에 있는 이모티콘 중 하나를 삭제 / 클립보드에 있는 이모티콘 중 일부 삭제 금지
    if display -1 >= 0:
      if not visited[display-1][clip]:
        visited[display-1][clip] = True
        q.append([display-1, clip, cnt+1])

print(bfs(s))