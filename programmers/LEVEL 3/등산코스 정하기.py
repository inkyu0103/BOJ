from collections import deque
from math import inf


def solution(n, paths, gates, summits):
    set_gates = set(gates)
    set_summits = set(summits)

    answer_candidates = []

    graph = [[] for _ in range(n + 1)]
    dist = [inf] * (n + 1)
    q = deque()

    for s, e, c in paths:
        graph[s].append([e, c])
        graph[e].append([s, c])

    for gate in set_gates:
        q.append([0, gate])
        dist[gate] = 0

    while q:
        intensity, cur_node = q.popleft()
        for nxt_node, cost in graph[cur_node]:
            # 산 봉우리에 도달한 경우
            if nxt_node in set_summits:
                answer_candidates.append([nxt_node, max(cost, dist[cur_node])])
                continue
            if dist[nxt_node] > max(dist[cur_node], cost):
                q.append([max(intensity, cost), nxt_node])
                dist[nxt_node] = max(dist[cur_node], cost)

    answer_candidates.sort(key=lambda x: (x[1], x[0]))

    return answer_candidates[0]
