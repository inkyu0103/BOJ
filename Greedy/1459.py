import sys

input = sys.stdin.readline


def sol():
    x, y, w, s = list(map(int, input().split()))

    if 2 * w >= s:
        x + y

    return (x + y) * w


print(sol())
