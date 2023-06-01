# 1074  Z
import sys

input = sys.stdin.readline


def visit(n, r, c, start):
    if n == 0:
        return start

    r_l = True if r < 2 ** (n - 1) else False
    c_l = True if c < 2 ** (n - 1) else False

    if r_l and c_l:
        return visit(n - 1, r, c, start)
    if r_l and not c_l:
        return visit(n - 1, r, c % 2 ** (n - 1), start + 2 ** (2 * (n - 1)))
    if not r_l and c_l:
        return visit(n - 1, r % 2 ** (n - 1), c, start + 2 * 2 ** (2 * (n - 1)))
    if not r_l and not c_l:
        return visit(
            n - 1, r % 2 ** (n - 1), c % 2 ** (n - 1), start + 3 * 2 ** (2 * (n - 1))
        )


def sol():
    n, r, c = map(int, input().split())
    print(visit(n, r, c, 0))


sol()
