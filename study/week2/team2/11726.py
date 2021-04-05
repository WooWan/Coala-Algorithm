def H(i,j):
    c_1 = i+j-1
    c_2 = j
    result = factorial(c_1)/(factorial(c_2)*factorial(c_1-c_2))
    return result

def factorial (j):
    result = 1
    for i in range(j):
        result *= (i+1)
    return result;

result = 0
num = int(input())
for i in range(int(num/2)+1):
    if(i==0):
        result += 1
    else:
        result += H(i+1, num-2*i)
print(int(result))
