# 14496
import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(start):
    q = [(0,start)]

    while q:
        cur_dist,cur_node = heapq.heappop(q)
        if dist[cur_node] < cur_dist:
            continue

        for n in graph[cur_node]:
            next_dist,next_node = n

            new_dist = cur_dist + next_dist

            if dist[next_node] > new_dist:
                dist[next_node] = new_dist
                heapq.heappush(q,(new_dist,next_node))



if __name__ == '__main__':
    start,end = map(int,input().split())
    v,e = map(int,input().split())
    graph = [[] for i in range(v+1)]
    dist = [INF]*(v+1)
    dist[start] =0

    for _ in range(e):
        s,e = map(int,input().split())
        if s==e:
            continue
        graph[s].append((1,e))
        graph[e].append((1,s))

    dijkstra(start)
    if dist[end] == INF:
        print(-1)
    else:
        print(dist[end])



