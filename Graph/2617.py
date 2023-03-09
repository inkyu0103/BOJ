# 2617 구슬 찾기
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

smaller = [0] * (N + 1)
bigger = [0] * (N + 1)

graph = [[] for _ in range(N + 1)]
reverse_graph = [[] for _ in range(N + 1)]

visit = [0] * (N + 1)

# 그래프 세팅
for _ in range(M):
    heavy, light = map(int, input().split())
    graph[heavy].append(light)
    reverse_graph[light].append(heavy)


for i in range(1, N + 1):
    dist = 0
    q = deque([i])

    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if visit[nxt]:
                continue
            q.append(nxt)
            visit[nxt] = 1
            dist += 1

    smaller[i] = dist

for i in range(1, N + 1):
    dist = 0
    q = deque([i])

    while q:
        cur = q.popleft()
        for nxt in reverse_graph[cur]:
            if visit[nxt]:
                continue
            q.append(nxt)
            visit[nxt] = 1
            dist += 1

    bigger[i] = dist

print(smaller, bigger)
