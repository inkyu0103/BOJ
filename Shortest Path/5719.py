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

            if nc + cc >= dist[nn] or used[cn][nn]:
                continue

            dist[nn] = nc + cc
            heapq.heappush(q, [nc + cc, nn])
            pre[nn] = cn

    return dist[D]


def mark_used_route():
    idx = D
    while idx:
        st, ed = pre[idx], idx
        used[st][ed] = 1
        idx = pre[idx]


while True:
    N, M = map(int, input().split())

    if not N and not M:
        break

    S, D = map(int, input().split())

    adj = [[] for _ in range(N)]
    used = [[0] * N for _ in range(N)]

    for _ in range(M):
        U, V, P = map(int, input().split())
        adj[U].append([P, V])

    # 한 번 수행
    pre = [0] * N
    min_dist = solve()
    mark_used_route()
    for i in used:
        print(i)
    print("-----------------")

    while True:
        pre = [0] * N

        # 만약 다익스트라를 다시 수행했는데, 거리가 같은 경우 -> 또 다시 실행
        cal_dist = solve()

        if min_dist == cal_dist:
            mark_used_route()
            continue

        # 만약 다익스트라를 다시 수행했는데, 거리가 다른 경우 -> 오호 얘가 최단 경로구나!
        else:
            print(-1 if cal_dist == inf else cal_dist)
            for i in used:
                print(i)

            print(pre)
            break
