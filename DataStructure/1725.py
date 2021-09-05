# 1725 히스토그램

import sys
input = sys.stdin.readline

N = int(input())
arr = [(0,0)]
for i in range(N):
    arr.append((i+1,int(input())))
arr.append((len(arr),0))

stack = []

answer = 0

for idx,ele in arr:

    if not stack:
        stack.append((idx,ele))
        continue
    # 스택 맨 위에 있는 높이
    top = stack[-1][1]

    if top >ele:
        while stack[-1][1] > ele:
            right = idx
            left = stack[-2][0] + 1

            answer = max(answer,stack[-1][1]*(right-left))
            stack.pop()

        stack.append((idx,ele))

    else:
        stack.append((idx,ele))

print(answer)










