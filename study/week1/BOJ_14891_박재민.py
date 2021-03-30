def wheel_rotate(wheel_idx, direction):
    temp = 0
    if direction == 1:
        temp = wheel[wheel_idx][7]
        for i in range(7):
            wheel[wheel_idx][i + 1] = wheel[wheel_idx][i]
        wheel[wheel_idx][0] = temp
    elif direction == -1:
        temp = wheel[wheel_idx][0]
        for i in range(1, 8):
            wheel[wheel_idx][i - 1] = wheel[wheel_idx][i]
        wheel[wheel_idx][7] = temp

def rotate_check(wheel_idx,direction): // 코드 작성중
    if wheel_idx == 1:
        if wheel[wheel_idx -1][2] != wheel[wheel_idx][6]: # 1번톱니바퀴 2번 톱니바퀴 만나는 부분이 같지 않아야 rotate
            wheel
    elif wheel_idx == 2 or 3:
    else:

wheel = list()
for i in range(4):
    wheel.append(list(map(int, input())))
N = int(input())
for i in range(N):
    wheel_to_move_idx, direction = map(int, input().split(" "))
    wheel_rotate(wheel_to_move_idx - 1, direction)

print(wheel)
