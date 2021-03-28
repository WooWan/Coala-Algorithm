import sys

n = int(input().strip())
calender = []
high= [0 for i in range(10000)]
sum = 0

for i in range(n):
    a,b=map(int, sys.stdin.readline().split())
    calender.append([a,b])

sorted_calender = sorted(calender, key = lambda x:(x[0],x[1]))
s, e = sorted_calender[0]
for i in range(s,e+1):
    high[i] = high[i] + 1

for i in sorted_calender[1:]:
    ns, ne = i
    if(ns <= e+1):
        for i in range(ns, ne+1):
            high[i] = high[i] + 1
        if(e < ne):
            e = ne
    elif(ns > e+1):
        sum = sum + max(high) * (e-s+1)
        s = ns
        e = ne
        high= [0 for i in range(10000)]
        for i in range(ns, ne+1):
            high[i] = high[i] + 1
sum = sum + max(high) * (e-s+1)

print(sum)
