# 1162 도로포장
import sys
from math import inf
import heapq

input = sys.stdin.readline


def solve():
    q = [[0, 0, 1]]

    while q:
        cur_cost, pave_num, cur_node = heapq.heappop(q)
        if cur_cost != dist[pave_num][cur_node]:
            continue

        for nxt_cost, nxt_pave_num, nxt_node in adj[cur_node]:
            if pave_num + nxt_pave_num > K:
                continue

            if cur_cost + nxt_cost >= dist[pave_num + nxt_pave_num][nxt_node]:
                continue

            dist[nxt_pave_num + pave_num][nxt_node] = cur_cost + nxt_cost
            heapq.heappush(q, [cur_cost + nxt_cost, pave_num + nxt_pave_num, nxt_node])


N, M, K = map(int, input().split())
dist = [[inf] * (N + 1) for _ in range(K + 1)]
answer = inf

for i in range(K + 1):
    dist[i][1] = 0

adj = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e, c = map(int, input().split())

    # 포장을 안하는 경우
    adj[s].append([c, 0, e])
    adj[e].append([c, 0, s])

    # 포장을 하는 경우
    adj[s].append([0, 1, e])
    adj[e].append([0, 1, s])

solve()

for i in range(K + 1):
    answer = min(answer, dist[i][N])
print(answer)
