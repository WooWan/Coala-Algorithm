import sys

n = int(sys.stdin.readline().strip())
time = [[0,0]]
for i in range(1,n+1):
    time.append(list(map(int, sys.stdin.readline().split())))

sorted_time = sorted(time, key = lambda x:(x[1], x[0]))

cnt = 1

s, e = sorted_time[1]

for i in sorted_time[2:]:
    ns, ne = i
    if ns >= e:
        cnt += 1
        e = ne

print(cnt)