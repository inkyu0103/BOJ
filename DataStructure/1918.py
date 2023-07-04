# 1918 후위연산자
import sys

input = sys.stdin.readline


def sol():
    exp = list(input())
    stack = []
    answer = ""

    for c in exp:
        if c.isalpha():
            answer += c
            continue

        if c == "(":
            stack.append(c)
            continue

        if c == "*" or c == "/":
            while stack and (stack[-1] == "*" or stack[-1] == "/"):
                answer += stack.pop()
            stack.append(c)
            continue

        if c == "+" or c == "-":
            while stack and stack[-1] != "(":
                answer += stack.pop()
            stack.append(c)
            continue

        if c == ")":
            while stack and stack[-1] != "(":
                answer += stack.pop()
            stack.pop()
            continue
    while stack:
        answer += stack.pop()

    print(answer)


sol()
