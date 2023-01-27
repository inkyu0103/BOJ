# N과 M (12)
import sys

input = sys.stdin.readline


N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
tmp = []
visit = [0] * N


def backtracking(count, start):
    if count == M:
        print(*tmp)
        return

    last = -1
    for i in range(start, N):
        if last != numbers[i]:
            tmp.append(numbers[i])
            backtracking(count + 1, i)
            last = numbers[i]
            tmp.pop()


backtracking(0, 0)
