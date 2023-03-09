import sys
import copy

input = sys.stdin.readline


def rotate():
    rotated_board = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            rotated_board[c][N - r - 1] = board[r][c]
    return rotated_board


def tilt(_dir):
    while _dir:
        rotate()

    for r in range(N):
        tilted = [0] * N
        idx = 0

        for c in range(N):
            if not board[r][c]:
                continue
            if not tilted[idx]:
                tilted[idx] = board[r][c]
            elif tilted[idx] == board[r][c]:
                tilted[idx] *= 2
                idx += 1

            else:
                idx += 1
                tilted[idx] = board[r][c]

        for c in range(N):
            board[r][c] = tilted[c]


N = int(input())
init_board = [list(map(int, input().split())) for _ in range(N)]
board = copy.deepcopy(init_board)
mx = 0
