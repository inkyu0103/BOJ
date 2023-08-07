# 5427 불

import sys
from collections import deque

input = sys.stdin.readline


def find_sangun(ground):
    for r in range(len(ground)):
        for c in range(len(ground[0])):
            if ground[r][c] == "@":
                return [r, c]


def find_fire(ground):
    fires = []
    for r in range(len(ground)):
        for c in range(len(ground[0])):
            if ground[r][c] == "*":
                fires.append([r, c])
    return fires


def is_inbound(cur_r, cur_c, r, c):
    return 0 <= cur_r < r and 0 <= cur_c < c


def sol():
    tc = int(input())
    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    for _ in range(tc):
        is_escape = False
        escape_time = -1
        fire_queue = deque()
        sangun_queue = deque()
        c, r = map(int, input().split())
        ground = [list(input().rstrip()) for _ in range(r)]

        # 불이 이동하는 지도
        f_visit = [[0] * c for _ in range(r)]

        # 상근이가 이동하는 지도
        s_visit = [[0] * c for _ in range(r)]

        # 불 먼저 이동 시키기
        fire_starts = find_fire(ground)

        for start in fire_starts:
            f_visit[start[0]][start[1]] = 1
            fire_queue.append(start)

        while fire_queue:
            cur_r, cur_c = fire_queue.popleft()

            for dr, dc in dirs:
                new_r, new_c = cur_r + dr, cur_c + dc

                if not is_inbound(new_r, new_c, r, c):
                    continue

                if ground[new_r][new_c] == "#":
                    continue

                if f_visit[new_r][new_c]:
                    continue

                f_visit[new_r][new_c] = f_visit[cur_r][cur_c] + 1
                fire_queue.append([new_r, new_c])

        # 상근이 움직이기
        sangun_start = find_sangun(ground)
        s_visit[sangun_start[0]][sangun_start[1]] = 1

        sangun_queue.append(sangun_start)

        while sangun_queue and not is_escape:
            cur_r, cur_c = sangun_queue.popleft()

            for dr, dc in dirs:
                new_r, new_c = cur_r + dr, cur_c + dc

                # 만약 배열의 범위를 벗어난 경우 -> 탈출에 성공함. 따라서 break
                if not is_inbound(new_r, new_c, r, c):
                    is_escape = True
                    escape_time = s_visit[cur_r][cur_c] + 1
                    break

                if ground[new_r][new_c] == "#":
                    continue
                if s_visit[new_r][new_c]:
                    continue

                if (
                    f_visit[new_r][new_c]
                    and f_visit[new_r][new_c] <= s_visit[cur_r][cur_c] + 1
                ):
                    continue

                s_visit[new_r][new_c] = s_visit[cur_r][cur_c] + 1
                sangun_queue.append([new_r, new_c])

        print(escape_time - 1 if escape_time != -1 else "IMPOSSIBLE")


sol()
