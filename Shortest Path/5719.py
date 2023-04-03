# 거의 최단경로
import sys
from math import inf
import heapq

input = sys.stdin.readline


def solve():
    dist = [inf] * N
    dist[S] = 0
    q = [[0, S]]

    while q:
        cc, cn = heapq.heappop(q)
        if dist[cn] != cc:
            continue

        for nc, nn in adj[cn]:

            if nc + cc >= dist[nn]:
                continue

            dist[nn] = nc + cc
            heapq.heappush(q, [nc + cc, nn])

    return dist[D]


def solve2(min_dist):
    dist = [inf] * N
    dist[S] = 0
    q = [[0, S]]

    while q:
        cc, cn = heapq.heappop(q)
        if dist[cn] != cc:
            continue

        for nc, nn in adj[cn]:

            if nn == D and nc + cc <= min_dist:
                continue

            if nc + cc >= dist[nn]:
                continue

            dist[nn] = nc + cc
            heapq.heappush(q, [nc + cc, nn])

    return dist[D]


while True:
    N, M = map(int, input().split())

    if not N and not M:
        break

    S, D = map(int, input().split())

    adj = [[] for _ in range(N)]

    for _ in range(M):
        U, V, P = map(int, input().split())
        adj[U].append([P, V])

    min_dist = solve()
    answer = solve2(min_dist)
    print(-1 if answer == inf else answer)
