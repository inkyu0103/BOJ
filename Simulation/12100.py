import sys
import copy

input = sys.stdin.readline


def rotate():
    tmp = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            tmp[r][c] = board[r][c]

    for r in range(N):
        for c in range(N):
            board[r][c] = tmp[N - 1 - c][r]


def tilt(_dir):
    while _dir:
        rotate()
        _dir -= 1

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
mx = 0

for tmp in range(1024):
    board = copy.deepcopy(init_board)

    brute = tmp
    for d in range(5):
        _dir = brute % 4
        brute = brute // 4
        tilt(_dir)

    for r in range(N):
        for c in range(N):
            mx = max(mx, board[r][c])

print(mx)
