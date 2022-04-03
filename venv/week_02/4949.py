import sys

while True:
    strs = sys.stdin.readline()

    if strs == ".\n":
        break

    print(strs)
    left_pren = strs.count("(")
    right_pren = strs.count(")")

    left_brac = strs.count("[")
    right_brac = strs.count("]")

    print(left_brac)
    print(right_brac)
    print(left_pren)
    print(right_pren)
    if left_brac == right_brac and left_pren == right_pren:
        print("yes")

    else:
        print("no")