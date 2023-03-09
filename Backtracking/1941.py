# 1941 소문난 칠공주
import sys

input = sys.stdin.readline


def oob(r, c):
    return 0 <= r < 5 and 0 <= c < 5


def backtracking(S, Y, cur_r, cur_c):
    if Y == 4:
        return

    if S + Y == 7 and S > Y:
        print()
        answer.append(1)

    visit = [0] * 4

    for d in range(4):
        if d == 0 and oob(cur_r, cur_c + 1) and not visit[d]:
            visit[d] = 1
            backtracking(S + 1, Y, cur_r, cur_c + 1) if _map[cur_r][
                cur_c + 1
            ] == "S" else backtracking(S, Y + 1, cur_r, cur_c + 1)
            visit[d] = 0

        if d == 0 and oob(cur_r, cur_c - 1) and not visit[d]:
            visit[d] = 1
            backtracking(S + 1, Y, cur_r, cur_c - 1) if _map[cur_r][
                cur_c - 1
            ] == "S" else backtracking(S, Y + 1, cur_r, cur_c - 1)
            visit[d] = 0

        if d == 0 and oob(cur_r + 1, cur_c) and not visit[d]:
            visit[d] = 1
            backtracking(S + 1, Y, cur_r + 1, cur_c) if _map[cur_r + 1][
                cur_c
            ] == "S" else backtracking(S, Y + 1, cur_r + 1, cur_c)
            visit[d] = 0

        if d == 0 and oob(cur_r - 1, cur_c) and not visit[d]:
            visit[d] = 1
            backtracking(S + 1, Y, cur_r - 1, cur_c) if _map[cur_r - 1][
                cur_c
            ] == "S" else backtracking(S, Y + 1, cur_r - 1, cur_c)
            visit[d] = 0


_map = [list(input().rstrip()) for _ in range(5)]
answer = []

for r in range(5):
    for c in range(5):
        if _map[r][c] == "Y":
            backtracking(0, 1, r, c)
        else:
            backtracking(1, 0, r, c)

print(answer)
