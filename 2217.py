start = int(input())
rope = list()
ans = 0

for _ in range(start):
    rope.append(int(input()))

if start == 1:  # 입력값이 하나일때 예외 처리
    print(rope[0])
else:
    rope.sort()

    for i in range(start - 1):
        if rope[i] * (start - i) >= rope[i + 1] * (start - i - 1):
            if ans <= rope[i] * (start - i):
                ans = rope[i] * (start - i)
        else:  # 마지막 하나가 정답일때
            if ans <= rope[i + 1] * (start - i - 1):
                ans = rope[i + 1] * (start - i - 1)

    print(ans)

# test = list()
# test.append(int(input()))
#
# test.append("Hi")
# print(test)
# print(test[0])
# print(int(test[0]))
# print(type(test[0]))
