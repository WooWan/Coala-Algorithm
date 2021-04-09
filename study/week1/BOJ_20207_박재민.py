N = int(input())
calendar = [0]*366
size = width = height =0
for i in range(N): # init calendar
    start,end = input().split(" ")
    start = int(start)
    end = int(end)
    for j in range(start,end+1):
        calendar[j] += 1

for i in range(1,len(calendar)):
   if calendar[i] != 0:
       width += 1
       height = max(height, calendar[i])
   else: #calendar[i] is 0
       size += width*height
       width = height = 0;
print(size)


