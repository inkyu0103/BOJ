# 1863 스카이라인

import sys

def sol():
    case = int(sys.stdin.readline())
    stack = []
    count = 0
    for i in range(case):
        x,y = map(int,sys.stdin.readline().split())

        while(stack and stack[-1][1] > y):
            stack.pop()
            count += 1
        if not stack:
            if y != 0 :
                stack.append((x,y))

        elif stack[-1][1]< y:
            stack.append((x,y))

    # 스택에 한 개 이상 남을 수 있는지? (그치... 오름 차순인 경우 그럴 수 있지)
    if stack:
        count += len(stack)

    return count

print(sol())
