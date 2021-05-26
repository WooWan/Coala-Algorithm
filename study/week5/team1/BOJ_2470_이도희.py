#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
input = sys.stdin.readline

N = int(input())

liquid = [int(x) for x in input().split()]

# 오름차순 정렬
liquid.sort()

left = 0
right = N - 1
answer = liquid[left] + liquid[right]
l = left
r = right
while left < right:
    tmp = liquid[left] + liquid[right]
    # 새로 구한 tmp의 용액 합 절대값이 0에 더 가까움
    if abs(tmp) < abs(answer):
        answer = tmp
        l = left
        r = right
        # 만약 용액합이 0인 경우는 멈춰
        if answer == 0:
            break
    # answer에 담긴 값이 더 절대값이 작은 경우
    # 이때 용액합이 음수인 경우 작은 애를 한칸 높여
    if tmp < 0:
        left += 1
    # 용액 합이 양수인 경우 큰 애를 한칸 낮춰
    else:
        right -= 1
print(liquid[l], liquid[r])

