# 1863 스카이라인

import sys

def sol():
    case = int(sys.stdin.readline())
    stack = []
    count = 0
    for i in range(case):
        x,y = map(int,sys.stdin.readline().split())

        # 이 경우에는 하나씩만 빼는 거라 while부터 돌리지 않아야겠다.
        if not stack or stack[-1][1] <y:
            stack.append((x,y))

        # 같은 건 들어오지 않는다. 고도의 차이가 있을 때만 입력으로 주어짐
        elif stack[-1][1] > y:
            stack.pop()
            count += 1

            #요렇게 해서 0이 아니면 다 붙이면 되지 않을까?

            if stack and y!= 0 and stack[-1][1] != y:
                stack.append((x,y))
            elif not stack and y!=0:
                stack.append((x,y))

            # 스택이 비었거나, y값이 다른 경우에는 append
            # 스택이 비었는데, y값이 0인경우도 append 하면 안되는데,

        if i == case-1:
            # 스택에 남아있다면, 계속 pop해버려
            if stack:
                while stack:
                    stack.pop()
                    count += 1

            # 스택이 비었긴 한데, 마지막이 0으로 끝나는지에 따라
            elif not stack:
                if y != 0 :
                    count += 1


    return count

print(sol())
