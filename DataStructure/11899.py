# 11899 괄호 끼워넣기
import sys
input = sys.stdin.readline

def sol():
    broken = input().strip()
    stack = []
    answer = 0
    for c in broken:
        if c =="(":
            stack.append("(")

        elif not stack and c==")":
            answer += 1

        elif stack and c==")":
            stack.pop()

    if stack:
        answer += len(stack)
    print(answer)
sol()
