# 1935 후위 표기식 2

import sys

def sol():
    stack =[]
    operator = ["+","-","/","*"]
    alphaToNum = {}
    operandNum = int(input())
    exp = sys.stdin.readline().strip()
    numArr = [int(sys.stdin.readline()) for i in range(operandNum)]
    count = 0
    for e in range(len(exp)):
        if 65<=ord(exp[e])<=122 and exp[e] not in alphaToNum:
            alphaToNum[exp[e]] = numArr[count]
            count += 1

    for e in range(len(exp)):
        if exp[e] not in operator:
            stack.append(alphaToNum[exp[e]])

        else:
            val2 = stack.pop()
            val1 = stack.pop()

            if exp[e] == "+":
                stack.append(val1+val2)
            elif exp[e] == "-":
                stack.append(val1-val2)
            elif exp[e] == "*":
                stack.append(val1*val2)
            elif exp[e] == "/":
                stack.append(val1/val2)



    print("%.2f"%stack[0])
sol()








