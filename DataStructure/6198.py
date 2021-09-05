# 6198 옥상정원 꾸미기
import sys
input = sys.stdin.readline

tc = int(input())
stack = []
result = 0
for _ in range(tc):
    val = int(input())

    if not stack:
        stack.append(val)

    elif stack[-1] <= val:
        while(stack and stack[-1] <= val):
            stack.pop()
        stack.append(val)
    else:
        stack.append(val)

    result += len(stack)-1

print(result)






