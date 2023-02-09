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

    # 만약 가로 세로 길이가 맞지 않다면... rotate를 시키고, 2번씩 회전 시켜야 한다.
    if N < R or M < C:
        rotate(g)
        is_rotate_essential = True

    # 두 번씩 회전시키지 않아도 되는 경우는 총 3번 회전시켜볼 수 있다.
    for _ in range(3):
        a = 1
