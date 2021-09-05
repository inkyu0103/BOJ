# 에디터 -- 카카오에 비슷한 문제가 있었는데 보자.
# 기본적으로 0. 추가되면 +1씩
# 글자를 stack을 이용하는 것 같은데
'''
A스택 B스택으로 나눠서 문제를 해결

A스택 : 커서보다 앞에 있는 아이들
B스택 : 커서보다 뒤에 있는 아이들
초기 커서 위치는 user_input length와 같다.
'''

from collections import deque
import sys
input = sys.stdin.readline

stack_A,stack_B = list(input().strip()),deque()
command_number = int(input())

for _ in range(command_number):
    command = input().strip()

    if "P" in command:
        add_letter = command[-1]
        stack_A.append(add_letter)

    else:
        if command == "L" and stack_A:
            stack_B.appendleft(stack_A.pop())

        elif command=="D" and stack_B:
            stack_A.append(stack_B.popleft())

        elif command =="B" and stack_A:
            stack_A.pop()

print("".join(stack_A)+"".join(stack_B))








