import sys

input = sys.stdin.readline


def rotate(sticker):
    sticker_row, sticker_col = len(sticker), len(sticker[0])
    rotate_sticker = [[0] * sticker_row for _ in range(sticker_col)]

    for r in range(sticker_row):
        for c in range(sticker_col):
            rotate_sticker[c][sticker_row - r - 1] = sticker[r][c]

    return rotate_sticker


N, M, K = map(int, input().split())
result = [[0] * M for _ in range(N)]

for _ in range(K):
    R, C = map(int, input().split())
    g = [list(map(int, input().split())) for _ in range(R)]
    is_rotate_essential = False

    is_stick = True
