# 14499 주사위 굴리기
import sys

input = sys.stdin.readline


def oob(r, c):
    return 0 <= r < N and 0 <= c < M


def move_east():
    dice[1][0], dice[1][1], dice[1][2], dice[3][1] = (
        dice[3][1],
        dice[1][0],
        dice[1][1],
        dice[1][2],
    )


def move_west():
    dice[1][0], dice[1][1], dice[1][2], dice[3][1] = (
        dice[1][1],
        dice[1][2],
        dice[3][1],
        dice[1][0],
    )


def move_north():
    dice[0][1], dice[1][1], dice[2][1], dice[3][1] = (
        dice[1][1],
        dice[2][1],
        dice[3][1],
        dice[0][1],
    )


def move_south():
    dice[0][1], dice[1][1], dice[2][1], dice[3][1] = (
        dice[3][1],
        dice[0][1],
        dice[1][1],
        dice[2][1],
    )


def swap_dice_bottom(cur_r, cur_c):
    if _map[cur_r][cur_c]:
        dice[3][1] = _map[cur_r][cur_c]
        _map[cur_r][cur_c] = 0

    else:
        _map[cur_r][cur_c] = dice[3][1]


N, M, cur_r, cur_c, command_nums = map(int, input().split())
_map = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))
dice = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]


for command in commands:
    if command == 1 and oob(cur_r, cur_c + 1):
        move_east()
        cur_c += 1

    elif command == 2 and oob(cur_r, cur_c - 1):
        move_west()
        cur_c -= 1

    elif command == 3 and oob(cur_r - 1, cur_c):
        move_north()
        cur_r -= 1

    elif command == 4 and oob(cur_r + 1, cur_c):
        move_south()
        cur_r += 1

    else:
        continue

    swap_dice_bottom(cur_r, cur_c)
    print(dice[1][1])
