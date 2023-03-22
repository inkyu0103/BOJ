# 16598 Maaaaaaaze

import sys
import copy
from math import inf
from itertools import product
from collections import deque


def rotate(board):
    result = copy.deepcopy(board)
    for r in range(5):
        for c in range(5):
            result[r][c] = board[c][5 - r - 1]
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
        bb
        if is_in_out_open(_in, _out, maze):
            continue

        visit = [[[0] * 5 for r in range(5)] for h in range(5)]
        is_reach = False

        q = deque()
        q.append(_in)

        while q:
            cur_h, cur_r, cur_c = q.popleft()

            for dh, dr, dc in dirs:
                new_h, new_r, new_c = cur_h + dh, cur_r + dr, cur_c + dc

                if new_h == _out[0] and new_r == _out[1] and new_c == _out[2]:

                    # 만약 도착지라면, tmp_answer과 비교 한 후 도착
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

            if is_reach:
                break

    return tmp_answer


input = sys.stdin.readline
boards = [[] for _ in range(5)]

case = list(product([0, 1, 2, 3], repeat=4))
answer = inf


for _ in range(5):
    boards[_].append([list(map(int, input().split())) for i in range(5)])

# 회전시킨 케이스를 모두 담는다. board[층][회전 케이스]
for _ in range(5):
    for i in range(1, 4):
        boards[_].append(rotate(boards[_][i - 1]))


for floor in case:
    maze = [boards[i][floor[i]] for _ in range(5)]
    answer = min(answer, bfs(maze))

print(answer if answer != inf else -1)
