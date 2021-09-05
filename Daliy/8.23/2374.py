# 2374 시작시간 12:05 첫 코딩 12:40
'''
조건 : 무조건 1씩만 오름
결국 제일 작은 수와 제일 큰 수의 차이를 알아야 하는데. . .

ex ) 1 3 5 3
a[1]
a[1]
a[1] --> 3 3 5 3
a[1]
a[1] --> 5 5 5 3
a[4]
a[4]
'''
import sys
input = sys.stdin.readline
stack = []
answer =0
n= int(input())
for _ in range(n):
    val = int(input())
    if not stack:
        stack.append(val)
    elif stack[-1] <= val:
        answer += val-stack[-1]
        stack.pop()
        stack.append(val)
    else:
        stack.append(val)


while len(stack)>1:
    answer += stack[-2]-stack[-1]
    stack.pop()

print(answer)

