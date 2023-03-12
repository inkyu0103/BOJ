# 20183 골목 대장 호석
import sys
import heapq
from math import inf

input = sys.stdin.readline


def solve(limit):
    q = []
    # 시작 거리 0

    dist[A] = 0
    q.append([0, A])

    while q:
        cur_cost, cur_node = heapq.heappop(q)
        if dist[cur_node] != cur_cost:
            continue

        for nxt_cost, nxt_node in adj[cur_node]:
            # 최대 지불 상한보다 큰 경우 pass
            if limit < nxt_cost:
                continue

            # 이미 dist 값이 더 작은 경우는 갱신할 필요가 없음
            if dist[nxt_node] <= cur_cost + nxt_cost:
                continue

            dist[nxt_node] = cur_cost + nxt_cost
            heapq.heappush(q, [cur_cost + nxt_cost, nxt_node])

    if dist[B] > C:
        return False
    return True


N, M, A, B, C = map(int, input().split())
dist = [inf] * (N + 1)

adj = [[] for _ in range(N + 1)]

low_cost = 1
high_cost = 1

# adj
for _ in range(M):
    s, e, cost = map(int, input().split())
    adj[s].append([cost, e])
    adj[e].append([cost, s])
    high_cost = max(high_cost, cost)


while low_cost < high_cost:
    mid = (low_cost + high_cost) // 2
    if solve(mid):
        high_cost = mid
    else:
        low_cost = mid + 1


print(low_cost if solve(low_cost) else -1)
