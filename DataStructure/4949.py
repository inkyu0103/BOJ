#4949 균형잡힌 세상

import sys



while(1):
    sentence = sys.stdin.readline().rstrip()
    if sentence == ".":
        break
    stack = []
    flag = 0


    for char in sentence:
        if char == "(" or char == "[":
            stack.append(char)

        elif char == ")":
            if len(stack) > 0 and stack[len(stack)-1] == "(":
                stack.pop(len(stack)-1)

            else:
                flag = 1


        elif char == "]":
            if len(stack) > 0 and stack[len(stack)-1] == "[":
                stack.pop(len(stack)-1)
            else:
                flag = 1


    if len(stack) != 0 or flag == 1:
        print("no")
    else:
        print("yes")







