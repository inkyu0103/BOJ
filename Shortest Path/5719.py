# 거의 최단경로
import sys
from math import inf
from collections import defaultdict, deque
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

            if nc + cc >= dist[nn] or nn in exclude_path[cn]:
                continue

            dist[nn] = nc + cc
            heapq.heappush(q, [nc + cc, nn])

    return dist


def solve2():
    q = deque()
    q.append(D)

    while q:
        cur = q.popleft()
        if cur == S:
            continue

        for cost, nxt_node in rev_adj[cur]:

            if dist[cur] == dist[nxt_node] + cost:
                exclude_path[nxt_node].add(cur)
                q.append(nxt_node)
    return exclude_path


while True:
    N, M = map(int, input().split())

    if not N and not M:
        break

    S, D = map(int, input().split())

    adj = [[] for _ in range(N)]
    rev_adj = [[] for _ in range(N)]

    for _ in range(M):
        U, V, P = map(int, input().split())
        adj[U].append([P, V])
        rev_adj[V].append([P, U])

    exclude_path = defaultdict(set)
    dist = solve()
    exclude_path = solve2()
    answer = solve()

    print(-1 if answer[D] == inf else answer[D])
