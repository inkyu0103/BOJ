# 9466 텀 프로젝트
import sys
from collections import deque

input = sys.stdin.readline

VISITED = 1
NO_CYCLE = 2
CYCLE = 3


def sol():
    tc = int(input())

    for _ in range(tc):
        N = int(input())
        arr = [0] + list(map(int, input().split(" ")))

        # print(arr)
        visit = [0] * (N + 1)

        for i in arr:
            if not visit[i]:
                cur = i
                while True:
                    visit[cur] = VISITED
                    cur = arr[cur]

                    # case 1
                    if visit[cur] == CYCLE or visit[cur] == NO_CYCLE:
                        cur = i
                        while visit[cur] == VISITED:
                            visit[cur] = NO_CYCLE
                            cur = arr[cur]
                        break

                    # case 2
                    if visit[cur] == VISITED and cur != i:
                        while visit[cur] != CYCLE:
                            visit[cur] = CYCLE
                            cur = arr[cur]
                        cur = i
                        while visit[cur] != CYCLE:
                            visit[cur] = NO_CYCLE
                            cur = arr[cur]
                        break
                    # case 3
                    if visit[cur] == VISITED and cur == i:
                        while visit[cur] != CYCLE:
                            visit[cur] = CYCLE
                            cur = arr[cur]
                        break
        print(N - visit.count(3) + 1)


sol()
