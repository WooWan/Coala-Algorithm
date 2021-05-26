from sys import stdin

#입력 받기
n = int(stdin.readline())
array = [int(x) for x in stdin.readline().split()]

array.sort() #음수는 산성, 양수는 알칼리 정렬

def get_min_value(arr):
    #i는 알칼리성 용액을 리스트의 왼쪽부터 보고, j는 산성 용액을 리스트의 오른쪽부터 봄.
    i, j = 0, len(arr) - 1
    min_value = abs(arr[i] + arr[j])
    min_set = i, j

    while i < j:
        current = arr[i] + arr[j]

        if abs(current) < min_value:
            min_value = abs(current) #두 용액으로 만들어지는 0에 가장 가까운 값의 절대값
            min_set = i, j #min_value를 만드는 두 용액 값

        if current == 0:
            return min_set #0을 만들었으니 해당 숫자 리턴
        elif current > 0:
            j -= 1 #0보다 크면 0에 가까운 값을 만들기 위해서 더 작은 수가 필요하니까 1을 빼줌
        else:
            i += 1 #0보다 작으면 0에 가까운 값을 만들기 위해서 더 큰 수가 필요하니까 1을 더함

    return min_set


a, b = get_min_value(array)

print(array[a], array[b])

#https://velog.io/@ready2start/Python-%EB%B0%B1%EC%A4%80-2470-%EB%91%90-%EC%9A%A9%EC%95%A1 참고했습니다.