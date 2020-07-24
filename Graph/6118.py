#6118 숨바꼭질

import sys
import heapq

INF = 1e19

N,M = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(N)]

for _ in range(M):
    st,ed = map(int,sys.stdin.readline().split())
    graph[st-1].append([1,ed-1])
    graph[ed-1].append([1,st-1])

def dijkstra():
    dist =[INF]*N
    dist[0] = 0

    q =[]
    q.append([0,0])

    while q:
        w,c = heapq.heappop(q)
        for nw,nc in graph[c]:
            nw+=w
            if dist[nc]>nw:
                dist[nc] = nw
                heapq.heappush(q,[nw,nc])

    return dist

a = dijkstra()

maxVal = max(a)
idx = a.index(maxVal)
counting = a.count(maxVal)

print("{} {} {}".format(idx+1, maxVal,counting))


