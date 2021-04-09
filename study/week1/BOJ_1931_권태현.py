n = int(input())

result_list = []
for i in range(n):
    start, end = map(int, input().split())
    result_list.append((start,end))

result_list.sort(key=lambda x:(x[1],x[0]))

cnt = 0
end_time = 0

for j in range(len(result_list)):
    if end_time <= result_list[j][0]:
        end_time = result_list[j][1]
        cnt += 1

print(cnt)