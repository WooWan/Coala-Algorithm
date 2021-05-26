import sys

def netural_liquid():
    N = int(sys.stdin.readline())
    number = list(map(int, sys.stdin.readline().split()))
    number.sort()

    left = 0
    right = N-1
    target_Left = 0
    target_Right = N-1
    sum = abs(number[left] + number[right])
    while left < right:
        temp = number[left] + number[right]
        if abs(temp) < sum:
            target_Left = left
            target_Right = right
            sum = abs(temp)
            if sum == 0: break

        if temp < 0:
            left += 1
        else:
            right -= 1

    print(number[target_Left], number[target_Right])

netural_liquid()
