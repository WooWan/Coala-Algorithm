from operator import itemgetter
N = int(input())
table = list()
for i in range(N):
    start,end = input().split(" ")
    start = int(start)
    end = int(end)
    table.append([start, end])
table.sort(key=itemgetter(1))

sum = 1
cur_idx = 0
for i in range(len(table)):
    if table[i][0] >= table[cur_idx][1]:
        sum += 1
        cur_idx = i;
print(sum)