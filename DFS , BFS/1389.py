# 1389

from collections import deque
import sys
input = sys.stdin.readline

def bfs(s):
    q = deque([s])
    visit = [0] * (N+1)
    visit[s] = 1

    while q:
        cur_node = q.popleft()

        for nextNode in graph[cur_node]:
            if not visit[nextNode]:
                visit[nextNode] = visit[cur_node] + 1


    print(visit)









N,M = map(int,input().split())
graph =[[] for _ in range(N+1)]

for _ in range(M):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)


bfs(1)