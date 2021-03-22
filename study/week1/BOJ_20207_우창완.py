import sys

n=int(input())
callendar=[0]*367
for i in range(n):
    a,b = map(int, sys.stdin.readline().split())
    for i in range(a,b+1):
        callendar[i]+=1

x=0
y=0
answer=0
for i in range(1,367):
    if callendar[i]!=0:
        x+=1
        y=max(y, callendar[i])
    else:
        answer+=x*y
        x=y=0
print(answer)