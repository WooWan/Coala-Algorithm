
n = int(input())
input = [int(i) for i in input().split()]

input.sort()
result = 0

left_idx = 0
right_idx = n-1

answer = input[left_idx] + input[right_idx]

while True:
    if answer == 0 or left_idx >= right_idx :break
    temp_ans = input[left_idx] + input[right_idx]
    if(abs(temp_ans) <= abs(answer)):
        answer = temp_ans
        result=([left_idx,right_idx])
    if temp_ans < 0: left_idx+=1
    if temp_ans >0 : right_idx-=1

print(input[result[0]], input[result[1]])
