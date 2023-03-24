# 16598 Maaaaaaaze

import sys
import copy
from math import inf
from itertools import product, permutations
from collections import deque


def rotate(board):
    result = copy.deepcopy(board)
    for r in range(5):
        for c in range(5):
            result[c][5 - r - 1] = board[r][c]
    return result


def oob(h, r, c):
    return 0 <= h < 5 and 0 <= r < 5 and 0 <= c < 5


# 입구와 출구가 열려있는지?
def is_in_out_open(_in, _out, maze):
    return maze[_in[0]][_in[1]][_in[2]] and maze[_out[0]][_out[1]][_out[2]]


def bfs(maze):
    # h,r,c
    # 동, 서, 남, 북 , 위 , 아래
    dirs = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]
    in_out = [
        [[0, 0, 0], [4, 4, 4]],
        [[0, 0, 4], [4, 4, 0]],
        [[0, 4, 0], [4, 0, 4]],
        [[0, 4, 4], [4, 0, 0]],
    ]
    tmp_answer = inf

    for _in, _out in in_out:
        if not is_in_out_open(_in, _out, maze):
            continue

        visit = [[[0] * 5 for r in range(5)] for h in range(5)]
        is_reach = False

        q = deque()
        q.append(_in)
        visit[_in[0]][_in[1]][_in[2]] = 1

        while q:
            cur_h, cur_r, cur_c = q.popleft()

            for dh, dr, dc in dirs:
                new_h, new_r, new_c = cur_h + dh, cur_r + dr, cur_c + dc

                if new_h == _out[0] and new_r == _out[1] and new_c == _out[2]:
                    tmp_answer = min(tmp_answer, visit[cur_h][cur_r][cur_c] + 1)
                    is_reach = True
                    break

                if (
                    oob(new_h, new_r, new_c)
                    and maze[new_h][new_r][new_c]
                    and not visit[new_h][new_r][new_c]
                ):
                    visit[new_h][new_r][new_c] = visit[cur_h][cur_r][cur_c] + 1
                    q.append([new_h, new_r, new_c])

            if is_reach or tmp_answer == 12:
                break

    return tmp_answer


input = sys.stdin.readline
boards = [[] for _ in range(5)]

case = list(product([0, 1, 2, 3], repeat=5))
answer = inf


for _ in range(5):
    boards[_].append([list(map(int, input().split())) for i in range(5)])

# 회전시킨 케이스를 모두 담는다. board[층][회전 케이스]
for _ in range(5):
    for i in range(1, 4):
        boards[_].append(rotate(boards[_][i - 1]))


for f in permutations([0, 1, 2, 3, 4], 5):
    rotated_boards = [
        boards[f[0]],
        boards[f[1]],
        boards[f[2]],
        boards[f[3]],
        boards[f[4]],
    ]

    for floor in case:
        maze = [
            rotated_boards[0][floor[0]],
            rotated_boards[1][floor[1]],
            rotated_boards[2][floor[2]],
            rotated_boards[3][floor[3]],
            rotated_boards[4][floor[4]],
        ]

        answer = min(answer, bfs(maze))


print(answer - 1 if answer != inf else -1)
"""
와 판을 쌓는 순서 고려!
"""
