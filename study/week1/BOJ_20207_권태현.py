n = int(input())

schedule = [0]*367


for i in range(n):
    s,e = map(int, input().split())
    for i in range(s,e+1):
        schedule[i]+=1

x_axis = 0
y_axis = 0
result = 0

for i in range(1,367):
    if schedule[i] != 0:
        x_axis += 1
        y_axis = max(y_axis, schedule[i])
    else:
        result += x_axis*y_axis
        x_axis = y_axis = 0
print(result)
