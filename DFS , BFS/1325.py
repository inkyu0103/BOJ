# 1325
from collections import deque
import sys
input = sys.stdin.readline

def sol():
    N,M = map(int,input().split())
    graph = [[] for  _ in range(N+1)]

    for _ in range(M):
        A,B = map(int,input().split())
        graph[B].append(A)

    def bfs(start):
        q = deque([start])
        visit = [0] * (N+1)
        visit[start] = 1
        count = 1

        while q:
            cur = q.popleft()
            for _next in graph[cur]:
                if not visit[_next]:
                    visit[_next] = 1
                    q.append(_next)
                    count += 1

        return count

    candidate = [0]
    for i in range(1,N+1):
        count = bfs(i)
        if count:
            candidate.append(count)
    _max = max(candidate)

    answer = [idx for idx,i in enumerate(candidate) if i == _max]
    print(*answer)

sol()
