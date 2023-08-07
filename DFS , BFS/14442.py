# 14442 벽 부수고 이동하기 2
import sys
import math
from collections import deque

input = sys.stdin.readline


def sol():
    N, M, K = map(int, input().split(" "))
    _map = [list(map(int, list(input().rstrip()))) for _ in range(N)]
    if N == 1 and M == 1:
        print(1)
        return
    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    answers = []

    def is_inbound(r, c):
        return 0 <= r < N and 0 <= c < M

    # visit[K][R][C] : k 개를 부셨을 때의
    visit = [[[math.inf] * M for _ in range(N)] for _ in range(K + 1)]

    # K,R,C
    q = deque([[0, 0, 0]])
    visit[0][0][0] = 1
    is_reachable = False

    while q:

        cur_k, cur_r, cur_c = q.popleft()

        for dr, dc in dirs:
            new_r, new_c = cur_r + dr, cur_c + dc

            # 범위가 아닌 경우 ||
            if not is_inbound(new_r, new_c):
                continue

            # 도착지점에 도달한 경우
            if new_r == N - 1 and new_c == M - 1:
                is_reachable = True
                answers.append(visit[cur_k][cur_r][cur_c] + 1)
                break

            # 벽을 만난 경우 + 벽을 부술 수 있는 경우
            if (
                _map[new_r][new_c]
                and cur_k + 1 <= K
                and visit[cur_k + 1][new_r][new_c] > visit[cur_k][cur_r][cur_c] + 1
            ):
                visit[cur_k + 1][new_r][new_c] = visit[cur_k][cur_r][cur_c] + 1
                q.append([cur_k + 1, new_r, new_c])
                continue

            # 벽이 아닌 경우
            if (
                not _map[new_r][new_c]
                and visit[cur_k][new_r][new_c] > visit[cur_k][cur_r][cur_c] + 1
            ):
                visit[cur_k][new_r][new_c] = visit[cur_k][cur_r][cur_c] + 1
                q.append([cur_k, new_r, new_c])
                continue

        # 도달해서 나온 경우 break
        if is_reachable:
            break

    print(min(answers) if is_reachable else -1)


sol()
