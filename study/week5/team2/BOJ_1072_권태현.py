x, y = map(int, input().split())
start = 0
end = 1000000000
result = 0
z = int(y * 100 / x)

if z >= 99:
    print(-1)
    exit()

while start <= end:
    m = (start + end) // 2
    s = ((y + m) * 100 // (x + m))
    if  s > z:
        end = m - 1
        result = m
    else:
        start = m + 1

print(result)
