import sys
input = sys.stdin.readline

def sol():
    string = input().strip()
    target = "PPAP"
    lt = len(target)
    stack = []

    for i in string:
        if i == "P":
            stack.append("P")
            if len(stack) >= lt and "".join(stack[-lt:]) == target:
                del stack[-lt:]
                stack.append("P")
        else:
            stack.append(i)

    if "".join(stack) == "P":
        print("PPAP")
    else:
        print("NP")

sol()
