# 11779 최소비용과 경로를 둘 다 출력하는 문제 --> 트리로 가뿐하게 처리하면 되지 않을까?
# 간선 가중치 0보다 크거나 같음
import sys
import heapq
input= sys.stdin.readline
INF = sys.maxsize

def dijkstra(start):
    q = []
    dist[start] = 0
    heapq.heappush(q,(0,start))

    while q:
        curCost , curNode = heapq.heappop(q)

        if dist[curNode] < curCost:
            continue

        for n in graph[curNode]:
            nextCost,nextNode = n
            newCost = curCost + nextCost

            # 짧은 거리가 나왔을 때, 갱신
            if dist[nextNode] > newCost:
                dist[nextNode] = newCost
                parent[nextNode] = curNode
                heapq.heappush(q,(newCost,nextNode))

def findRoute (target):
    global cityNum
    Route = [target]
    while(target != parent[target]):
        cityNum += 1
        Route.append(parent[target])
        target = parent[target]

    return Route

if __name__=='__main__':
    N = int(input())
    M = int(input())
    cityNum = 1

    # 그래프
    graph = [[] for _ in range(N+1)]

    # 거리
    dist = [INF]*(N+1)

    # 최단 경로 출력을 위한 disjoint set
    parent = [i for i in range(N+1)]

    for _ in range(M):
        start,end,cost = map(int,input().split())
        graph[start].append((cost,end))

    start , end = map(int,input().split())
    dijkstra(start)
    route = findRoute(end)
    route.reverse()


    print(dist[end])
    print(cityNum)
    print(*route)

