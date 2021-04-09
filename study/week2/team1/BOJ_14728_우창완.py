import sys

n, t= map(int,input().split())
# dp=[[0]*(t+1) for _ in range(n+1)]
dp=[0]*(t+1)

arr=[0]*(n+1)
for i in range(1,n+1):
    #time, score
    arr[i]=(list(map(int ,sys.stdin.readline().split())))

# for i in range(1,n+1):
#     for j in range(1,t+1):
#         if j-arr[i][0]>=0:
#             dp[i][j]=max(dp[i-1][j], dp[i-1][j-arr[i][0]]+arr[i][1])
#         else: dp[i][j]=dp[i-1][j]
for i in range(1, n+1):
    for j in range(t, 0,-1):
        if j-arr[i][0]>=0:
            dp[j]=max(dp[j], dp[j-arr[i][0]]+ arr[i][1])
print(dp[-1])