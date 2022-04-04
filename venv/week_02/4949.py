import sys

while True:
    qq = list()
    strs = sys.stdin.readline()

    if strs == ".\n":
        break

    for word in strs:
        if word == "(":
            qq.append(")")

        elif word == "[":
            qq.append("]")

        elif word == ")":
            try:
                if qq.pop() == ")":
                    continue
                else:
                    qq.append("x")
                    break
            except IndexError:
                qq.append("x")
                break

        elif word == "]":
            try:
                if qq.pop() == "]":
                    continue
                else:
                    qq.append("x")
                    break
            except IndexError:
                qq.append("x")
                break

    if len(qq) == 0:
        print("yes")

    else:
        print("no")
