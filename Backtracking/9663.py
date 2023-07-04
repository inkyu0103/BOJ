# 9663 N-Queen

import sys
import copy

input = sys.stdin.readline


def sol():
    N = int(input())
    answer = []
    _map = [[0] * N for _ in range(N)]
    _visit = [[0] * N for _ in range(N)]

    def make_queen_area(m, r, c):
        result = copy.deepcopy(m)

        # 대각 왼쪽 상단
        cur_r, cur_c = r - 1, c - 1
        while cur_r >= 0 and cur_c >= 0:
            if not result[cur_r][cur_c]:
                result[cur_r][cur_c] = 1
            cur_r, cur_c = cur_r - 1, cur_c - 1

        # 대각 오른쪽 상단
        cur_r, cur_c = r - 1, c + 1
        while cur_r >= 0 and cur_c < N:
            if not result[cur_r][cur_c]:
                result[cur_r][cur_c] = 1
            cur_r, cur_c = cur_r - 1, cur_c + 1

        # 대각 오른쪽 하단
        cur_r, cur_c = r + 1, c + 1
        while cur_r < N and cur_c < N:
            if not result[cur_r][cur_c]:
                result[cur_r][cur_c] = 1
            cur_r, cur_c = cur_r + 1, cur_c + 1

        # 대각 왼쪽 하단
        cur_r, cur_c = r + 1, c - 1
        while cur_r < N and cur_c >= 0:
            if not result[cur_r][cur_c]:
                result[cur_r][cur_c] = 1
            cur_r, cur_c = cur_r + 1, cur_c - 1

        # 상하좌우
        for dr in range(N):
            if not result[dr][c]:
                result[dr][c] = 1

        for dc in range(N):
            if not result[r][dc]:
                result[r][dc] = 1

        result[r][c] = 2

        return result

    def queen(m, v, d):
        if d == N:
            for r in range(N):
                for c in range(N):
                    if m[r][c] == 2:
                        v[r][c] = 1
            return answer.append(1)

        for r in range(N):
            for c in range(N):
                if not m[r][c] and not v[r][c]:
                    v[r][c] = 1
                    queen(make_queen_area(m, r, c), v, d + 1)
                    v[r][c] = 0

    queen(_map, _visit, 0)
    print(sum(answer))


sol()
