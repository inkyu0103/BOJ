# N과 M (11)

import sys

input = sys.stdin.readline


N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
tmp = []
visit = [0] * N


def backtracking(count):
    if count == M:
        print(*tmp)
        return

    last = -1
    for i in range(N):
        if last != numbers[i]:
            tmp.append(numbers[i])
            backtracking(count + 1)
            last = numbers[i]
            tmp.pop()


backtracking(0)
