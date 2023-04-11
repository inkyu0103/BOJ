# 2669 네 직사각형 넓이

import sys

input = sys.stdin.readline

visited = [[0] * 101 for _ in range(101)]
answer = 0
for _ in range(4):
    xl, yl, xr, yr = map(int, input().split())

    for r in range(yl, yr):
        for c in range(xl, xr):
            if not visited[r][c]:
                answer += 1
                visited[r][c] = 1
print(answer)
