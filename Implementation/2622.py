# 2622 삼각형 만들기

import sys

input = sys.stdin.readline

N = int(input())
answer = 0

for x in range(1, N):
    for y in range(x, N):
        z = N - (x + y)

        if z < y:
            break

        if x + y > z:
            answer += 1

print(answer)
