n = int(input())

for _ in range(n):
    sol = 0
    size = int(input())
    russia = list(map(int, input().split(" ")))
    korea = list(map(int, input().split(" ")))
    russia.sort()
    korea.sort()

    for rus in russia:
        for kor in korea:
            if rus <= kor:
                korea.remove(kor)
                sol += 1
                break

    print(sol)
