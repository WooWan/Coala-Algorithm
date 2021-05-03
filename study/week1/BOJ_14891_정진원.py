#작성중
import sys

wheel = []
score = 0
t = 0

for i in range(4):
    wheel.append(list(map(int,sys.stdin.readline().strip())))

k = int(sys.stdin.readline().strip())

for i in range(k):
        a,b = map(int, sys.stdin.readline().split())

        direction = [0 for _ in range(4)] 
        direction[a-1] += b
        t = b

        for i in range(a-1,a+3):
            if(i+1 > 3):
                break
            if(wheel[i][2]!=wheel[i+1][6]):
                if(t > 0):
                    direction[i+1] += -1
                else:
                    direction[i+1] += 1
            else:
                break
            t = -t
        print(t)
        t = b
        
        for i in range(a-1,a-5):
            if(i-1 < 0):
                break
            if(wheel[i][6]!=wheel[i-1][2]):
                if(t > 0):
                    direction[i-1] += -1
                else:
                    direction[i-1] += 1
            else:
                break
            t = -t

        for i in range(4):
            if(direction[i]>=1):
                temp = wheel[i].pop()
                wheel[i].insert(0,temp)
            elif(direction[i]<=-1):
                temp = wheel[i].pop(0)
                wheel[i].append(temp)
        

for i in range(4):    
    score += wheel[i][0]*(2**i)            

print(score)