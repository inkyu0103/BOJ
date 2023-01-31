# 5427 불

import sys
from collections import deque


def printMap(m):
    for x in m:
        print(*x)


# sys.stdin = open("./F.in", "r")
input = sys.stdin
INF = 10e9
dh, dw = [1, 0, -1, 0], [0, 1, 0, -1]

TC = int(input())
for _ in range(TC):
    W, H = map(int, input().split())
    building = [list(input().strip()) for _ in range(H)]

    queue1, queue2 = deque(), deque()
    dist1, dist2 = [[INF] * W for _ in range(H)], [[INF] * W for _ in range(H)]

    # 불 먼저 돌리기
    for h in range(H):
        for w in range(W):
            if building[h][w] == "*":
                queue2.append([h, w])
                dist2[h][w] = 0

    while queue2:
        cur_h, cur_w = queue2.pop()

        for i in range(4):
            new_h, new_w = cur_h + dh[i], cur_w + dw[i]

            if (
                0 <= new_h < H
                and 0 <= new_w < W
                and dist2[new_h][new_w] == INF
                and building[new_h][new_w] != "#"
            ):
                dist2[new_h][new_w] = min(dist2[cur_h][cur_w] + 1, dist2[new_h][new_w])
                queue2.append([new_h, new_w])

    # printMap(dist2)

    # 사람
    for h in range(H):
        for w in range(W):
            if building[h][w] == "@":
                queue1.append([h, w])
                dist1[h][w] = 0

    isExit = False
    answer = -1

    while queue1:
        cur_h, cur_w = queue1.pop()

        for i in range(4):
            new_h, new_w = cur_h + dh[i], cur_w + dw[i]

            if new_h < 0 or new_h >= H or new_w < 0 or new_w >= W:
                answer = dist1[cur_h][cur_w]
                isExit = True
                break

            if (
                dist2[new_h][new_w] > dist1[cur_h][cur_w] + 1
                and building[new_h][new_w] != "#"
                and dist1[new_h][new_w] == INF
            ):
                queue1.append([new_h, new_w])
                dist1[new_h][new_w] = dist1[cur_h][cur_w] + 1

        if isExit:
            break

    print(answer + 1 if isExit else "IMPOSSIBLE")
