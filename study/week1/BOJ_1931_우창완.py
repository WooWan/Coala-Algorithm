import sys

n=int(input())
time=list()
for i in range(n):
    start,end= map(int, input().split())
    time.append((start, end))
#끝나는 시간을 기준으로 정렬, 끝나는 시간이 같다면 시작하는 시간이 빠른순으로 정렬
sorted_time= sorted(time, key=lambda time:(time[1],time[0]))

current=sorted_time[0][1]
cnt=1
for i in range(1,n):
    #시작하는 시간이 늦거나 같다면,
    if current<= sorted_time[i][0]:
        current=sorted_time[i][1]
        cnt+=1
print(cnt)