# 17952

import sys
input = sys.stdin.readline

def sol():
    tc = int(input())
    stack = []
    answer = 0
    for i in range(tc):
        val = input().strip()

        if val[0] == '0' and stack:
            stack[-1][1] -= 1

            if stack[-1][1] == 0:
                answer += stack[-1][0]
                stack.pop()

        elif val[0] == '1':
            tic,score,time = map(int,val.split(" "))
            if time == 1:
                answer += score
            else:
                stack.append([score,time-1])

    print(answer)
sol()
