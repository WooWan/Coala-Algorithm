#1072 게임


x,y=map(int, input().split())

proba= y*100//x
start=1
end=int(1e9)
result=-1
while (start<=end):
    mid=(start+end)//2
    pred=(y+mid)*100//(x+mid)
    if proba!=pred:
        result=mid
        end=mid-1
    else:
        start=mid+1
print(result)

