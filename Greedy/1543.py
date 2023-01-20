# 1543

import sys

input = sys.stdin.readline


def sol():
    target = input().rstrip()
    pattern = input().rstrip()

    idx = 0
    answer = 0

    while idx < len(target):
        if target[idx:].startswith(pattern):
            idx += len(pattern)
            answer += 1
        else:
            idx += 1

    print(answer)


sol()
