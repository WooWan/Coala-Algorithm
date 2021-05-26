#1470 두 용액 이분탐색
#기본 아이디어는 투포인터를 활용

import sys
input= sys.stdin.readline

n=int(input())
liquid=list(map(int, input().split()))

liquid.sort()
INF= sys.maxsize

start=0
end=n-1
result=INF
answer=[]
while(start<end):

    total= liquid[start]+liquid[end]

    if abs(total)<result:
        result=abs(total)
        answer= (liquid[start], liquid[end])
    if total<0:
        start+=1
    else: end-=1
print(answer[0],answer[1])