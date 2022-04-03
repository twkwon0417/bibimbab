# 투포인터 느낌
n = int(input())
data = list(map(int, input().split(" ")))

data.sort()
left, right = 0, len(data) - 1
sol_left, sol_right = 0, 0
standard = 2000000000

while left != right:
    if data[left] + data[right] >= 0:
        if abs(data[left] + data[right]) < standard:
            sol_left, sol_right = left, right
            standard = abs(data[left] + data[right])
        right -= 1

    else:
        if abs(data[left] + data[right]) < standard:
            sol_left, sol_right = left, right
            standard = abs(data[left] + data[right])
        left += 1

print(data[sol_left], data[sol_right])
