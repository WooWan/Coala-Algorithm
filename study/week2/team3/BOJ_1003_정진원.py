import sys

t = int(sys.stdin.readline().strip())
d = [[] for _ in range(42)]
for i in range(42):
    if i == 0:
        d[0].append(1)
        d[0].append(0)
    elif i == 1:
        d[1].append(0)
        d[1].append(1)
    elif i >= 2:
        d[i].append(d[i-1][0] + d[i-2][0])
        d[i].append(d[i-1][1] + d[i-2][1])
        
for i in range(t):
    n = int(sys.stdin.readline().strip())
    print(str(d[n][0]) + ' ' + str(d[n][1]))
