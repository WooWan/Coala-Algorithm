
def solution(stones, k):
    INF=int(1e9)
    start=0
    end=INF
    answer=0
    while(start<=end):
        mid=(start+end)//2
        result=0
        cnt=0
        flag=True
        # for stone in stones:
        #     if stone<mid:cnt+=1
        #     else:
        #         result=max(result, cnt+1)
        #         cnt=0
        #     result=max(result,cnt)
        # print(result)
        for i in range(len(stones)-1):
            if stones[i]<=mid:
                cnt+=1
            else: cnt=0
            if cnt>=k:
                flag=False
                break
        if not flag:
            end=mid-1
            answer=mid
        else:
            start= mid+1
    print(answer)
    return answer

solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)