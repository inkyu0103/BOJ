# 천재 수학자 성필 후위연산자 문제
import sys
input = sys.stdin.readline

def sol():
    exp = input().strip()
    operator = "+-*/"
    operand_stack = []

    for i in exp:

        if i in operator:
            second = operand_stack.pop()
            first = operand_stack.pop()

            if i == "+":
                operand_stack.append(first+second)
            elif i =="-":
                operand_stack.append(first-second)
            elif i =="*":
                operand_stack.append(first*second)
            elif i =="/":
                operand_stack.append(first/second)
        else:
            operand_stack.append(float(i))


    print(int(operand_stack[-1]))
sol()
