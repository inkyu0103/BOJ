# N과 M (7)
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
tmp = []


def backtracking(count, target):
    if count == M:
        print(*target)
        return

    for i in range(N):
        tmp.append(numbers[i])
        backtracking(count + 1, tmp)
        tmp.pop()


backtracking(0, numbers[0])
