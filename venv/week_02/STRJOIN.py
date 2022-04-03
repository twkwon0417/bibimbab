n = int(input())

for _ in range(n):
    sol = 0
    size = int(input())
    strs = list(map(int, input().split(" ")))
    strs.sort(reverse=True)
    while len(strs) != 1:
        temp = strs.pop() + strs.pop()
        sol += temp
        strs.append(temp)
        strs.sort(reverse=True)

    print(sol)

