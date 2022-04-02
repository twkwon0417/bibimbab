case = int(input())
sdule = list()
for _ in range(case):
    sdule.append(tuple(map(int, input().split())))

sdule.sort(key=lambda x: x[0])
sdule.sort(key=lambda x: x[1])

result = 0
end_time = 0

for a, b in sdule:
    if a >= end_time:
        result += 1
        end_time = b

print(result)
