#10828 스택
import sys
input = sys.stdin.readline

testCase = int(input())
stack = []

for i in range(testCase):
    command = input().split()

    if command[0] == 'push':
        stack.append(int(command[1]))
    elif command[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == 'top':
        if len(stack)==0:
            print(-1)
        else:
            print(int(stack[len(stack)-1]))
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
