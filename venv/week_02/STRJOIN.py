import collections

n = int(input())

for _ in range(n):
    sol = 0
    size = int(input())
    strs = list(map(int, input().split(" ")))
    strs.sort()
    while len(strs) != 1:
        size = len(strs)
        strs = collections.deque(strs)
        for _ in range(size // 2):
            temp = strs.popleft() + strs.popleft()
            sol += temp
            strs.append(temp)

        strs = list(strs)
        strs.sort()

    print(sol)

