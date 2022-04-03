cards, target = map(int, input().split(" "))

pae = list(map(int, input().split(" ")))

pae.sort()

ans = 0
for i in range(cards):
    for j in range(i + 1, cards):
        for k in range(j + 1, cards):
            current = pae[i] + pae[j] + pae[k]

            if current > target:
                break
            if current > ans:
                ans = current


print(ans)
