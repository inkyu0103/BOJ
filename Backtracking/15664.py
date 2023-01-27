# N과 M (9)
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
tmp = []
already = []
visit = [0] * N


def backtracking(count, idx):
    if count == M:
        print(*tmp)
        return

    last = -1
    for i in range(idx, N):
        if not visit[i] and last != numbers[i]:
            visit[i] = 1
            last = numbers[i]
            tmp.append(numbers[i])
            backtracking(count + 1, i + 1)
            visit[i] = 0
            tmp.pop()


backtracking(0, 0)
