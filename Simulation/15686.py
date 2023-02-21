# 15686 치킨 배달
import sys, math


input = sys.stdin.readline

N, M = map(int, input().split())
chicken_map = [list(map(int, input().split())) for _ in range(N)]
total_chicken_house = []
answer = math.inf

for r in range(len(chicken_map)):
    for c in range(len(chicken_map[0])):
        if chicken_map[r][c] == 2:
            total_chicken_house.append([r, c])

tmp = []


def min_chicken_dist():
    global answer
    sum_dist = 0
    for r in range(N):
        for c in range(N):
            if chicken_map[r][c] == 1:
                min_value = math.inf
                for idx, [chicken_r, chicken_c] in enumerate(total_chicken_house):
                    if idx in tmp:
                        min_value = min(
                            min_value, abs(r - chicken_r) + abs(c - chicken_c)
                        )
                sum_dist += min_value

    answer = min(answer, sum_dist)


def backtracking(level):
    # 최대로 폐업시켰다면 return
    if level == M:
        min_chicken_dist()
        return

    for idx in range(len(total_chicken_house)):
        if not tmp or tmp[-1] < idx:
            tmp.append(idx)
            backtracking(level + 1)
            tmp.pop()


backtracking(0)
print(answer)
