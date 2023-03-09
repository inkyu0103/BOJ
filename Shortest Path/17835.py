# 17835 면접보는 승범이네
import sys
import heapq
from math import inf

input = sys.stdin.readline


def extract_max_val(arr):
    max_idx, max_val = 0, 0
    for idx, val in enumerate(arr):
        if val == inf or idx in places:
            continue

        if max_val < val:
            max_val = val
            max_idx = idx

    return [max_idx, max_val]


N, M, K = map(int, input().split())

adj = [[] for _ in range(N + 1)]

answer_candidates = {}


# 간선들 저장
for i in range(M):
    s, e, c = map(int, input().split())
    adj[e].append([c, s])


# 도시 저장
places = list(map(int, input().split()))
queue = []
dist = [inf] * (N + 1)

for i in places:
    # dist, vertex

    dist[i] = 0
    queue.append([0, i])


while queue:
    # 아 min heap이구나
    d, node = heapq.heappop(queue)

    # queue에서 나온 거리와 같지 않은 경우는 pass
    if d != dist[node]:
        continue
    for nxt_c, nxt_node in adj[node]:
        if dist[nxt_node] > dist[node] + nxt_c:
            dist[nxt_node] = dist[node] + nxt_c
            heapq.heappush(queue, [dist[nxt_node], nxt_node])

answer_city, answer_dist = extract_max_val(dist)
print(answer_city)
print(answer_dist)
