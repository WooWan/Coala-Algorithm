#BOJ_16918 봄버맨 (https://br-brg.tistory.com/27 참고)

direction = ((-1, 0), (1, 0), (0, -1), (0, 1)) #폭탄탐색 방향
r, c, n = map(int, input().split()) #인풋(세로, 가로, 초)
MAP = [list(input()) for _ in range(r)] #격자판
time = [[-1]*c for _ in range(r)] #타이머
cnt = 0
 
# 초기화
for i in range(r):
    for j in range(c):
        if MAP[i][j] == 'O':
            time[i][j] = 0 #폭탄이 있는 곳은 타이머 0으로 설정
 
while cnt != n:
    boom = [] #폭발하는 곳 리스트
    for i in range(r):
        for j in range(c):
            if MAP[i][j] == '.' and time[i][j] == -1 and cnt != 0: # 0초일 때는 무시
                MAP[i][j] = 'O' #폭탄이 없는 곳에 폭탄 채우기
                time[i][j] = 0 #타이머도 설정해주기
            elif MAP[i][j] == 'O' and time[i][j] < 3:
                time[i][j] += 1 #폭탄 타이머 카운트다운
                if time[i][j] == 3: #터질 시간
                    boom.append((i,j)) # 폭발 리스트를 만들어서 터지는 폭탄 삽입
 
    for i,j in boom: #폭발하게 되면
        MAP[i][j] = '.'
        time[i][j] = -1
        for d in direction:
            ny = i + d[0]
            nx = j + d[1]
            if 0 <= ny < r and 0 <= nx < c:
                MAP[ny][nx] = '.'
                time[ny][nx] = -1
 
    cnt += 1
 
for m in MAP:
    print(''.join(m))
