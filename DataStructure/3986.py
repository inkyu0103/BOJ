#3986 좋은 단어
import sys


def isGoodLetter(str):
    stack = []
    for i in range(len(str)):
        if len(stack) == 0 :
            stack.append(str[i])
        else:
            if stack[-1] == str[i]:
                stack.pop()
            else:
                stack.append(str[i])


    if len(stack) == 0:
        return 1

    else:
        return 0


def sol():
    answer = 0
    case = int(input())
    for i in range(case):
        text = sys.stdin.readline().strip()
        answer += isGoodLetter(text)


    print(answer)

sol()
