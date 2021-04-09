#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#백준 1003

p = int(input())
list = list()
arr = [[0] * 41 ] * 2

for i in range(0, p):
  list.append(int(input())) 

def fibo(n):
  if n==0 :
    arr[0][0] = 1
  elif n==1 : 
    arr[1][1] = 1
  else:
    for x in range(2, n):
        arr[0][x] = arr[0][x-1] + arr[0][x-2]
        arr[1][x] = arr[1][x-1] + arr[1][x-2]
  return

for j in range(0, len(list)):
  n = list[j]
  fibo(n)

for j in range(0, p):
  print("count0={}, count1={}".format(arr[0][j],arr[1][j]))

