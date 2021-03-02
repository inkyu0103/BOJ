#1874 스택 수열

import sys
def sol():
    count = int(sys.stdin.readline())
    stack = []
    oper = []
    init_val = 1
    for i in range(count):
        _input = int(sys.stdin.readline())
        while not stack or stack[-1] < _input:
            stack.append(init_val)
            init_val += 1
            oper.append("+")

        if _input == stack[-1] :
            stack.pop()
            oper.append("-")
    if stack:
        print("NO")
    else:
        for i in oper:
            print(i)
sol()

