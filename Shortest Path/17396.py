#17396
import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

def sol():
    N,M = map(int,input().split())
    visible = list(map(int,input().split()))
    graph = [[] for _ in range(N)]

    # 넥서스도 지날 수 있으니 0 처리
    visible[N-1] = 0

    # 경로 입력
    for _ in range(M):
        s,e,d = map(int,input().split())
        if not visible[s] and not visible[e]:
            graph[s].append([d,e])
            graph[e].append([d,s])


    def dijkstra(s):
        # dist,node
        q = [[0,s]]
        dis = [INF] * N
        dis[s] = 0

        while q:
            dist,node = heapq.heappop(q)
            if dis[node] < dist:
                continue

            for ndist,nnode in graph[node]:
                if dist + ndist < dis[nnode]:
                    dis[nnode] = dist + ndist
                    heapq.heappush(q,[dist + ndist,nnode])

        return dis

    result = dijkstra(0)

    print(result[-1] if INF!= result[-1] else -1)









sol()
