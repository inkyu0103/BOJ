# 10217 retry
import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

# 최소 비용이 주어진 비용보다 적은것을 판단하기 위한 다익스트라
def mincost_dijkstra(N):
    q = [(0,1)]
    dist = [sys.maxsize]*(N+1)
    dist[1] = 0

    while q:
        cost,curNode = heapq.heappop(q)
        if dist[curNode] < cost:
            continue

        for nextNode in cost_graph[curNode] :
            nextCost = cost_graph[curNode][nextNode]
            newCost = cost + nextCost

            if dist[nextNode] > newCost:
                dist[nextNode] = newCost
                q.append((newCost,nextNode))

    return dist[N]

# 최소 시간을 소요 할 때 드는 비용 측정 (최소 시간이 기준)
def mintime_dijkstra(N):
    q = [(0, 1)]
    timedp = [sys.maxsize] * (N + 1)
    costdp = [sys.maxsize] * (N + 1)
    timedp[1],costdp[1] = 0,0


    while q:
        curTime, curNode = heapq.heappop(q)
        curCost = costdp[curNode]

        if timedp[curNode] < curTime:
            continue

        for nextNode in time_graph[curNode]:
            nextTime = time_graph[curNode][nextNode]
            nextCost = cost_graph[curNode][nextNode]

            newTime = curTime + nextTime
            newCost = curCost + nextCost

            if timedp[nextNode] > newTime:
                timedp[nextNode] = newTime
                costdp[nextNode] = newCost
                heapq.heappush(q,(newTime, nextNode))

    return timedp[N],costdp[N]

# 주어진 '비용'을 최대로 간주하여 경로를 찾는 경우 --> 근데 사실 이거 하나면... 끝 아니여...?
# 어라... 값을 어떻게 구해야하지
def fitcost_dijkstra(maxCost):
    q = [(0,1)]

    timedp = [sys.maxsize]*(N+1)
    costdp = [sys.maxsize]*(N+1)

    timedp[1],costdp[1] = 0,0

    while q:
        curCost,curNode = heapq.heappop(q)
        curTime = timedp[curNode]

        # 이 부분이 의심스럽네
        if costdp[curNode] < curCost:
            continue

        for nextNode in cost_graph[curNode]:
            nextCost = cost_graph[curNode][nextNode]
            nextTime = time_graph[curNode][nextNode]

            if costdp[nextNode] > nextCost and nextCost <= maxCost














if __name__ == '__main__':
    tc = int(input())
    for _  in range(tc):
        N,M,K = map(int,input().split())
        time_graph = [{} for _ in range(N+1)]
        cost_graph = [{} for _ in range(N+1)]


        for k in range(K):
            # s : 시작 공항, e : 끝 공항 , c : 비용 , t : 소요 시간 / 단방향이며, 같은 도로가 여러 개 있는 경우도 존재 할 수 있다.
            s,e,c,t = map(int,input().split())

            # 시간 그래프에서 추가되지 않은 경우
            if e not in time_graph[s]:
                time_graph[s][e] = t
            # 비용 그래프에서 추가되지 않은 경우 (사실 시간 그래프 추가 할 때 같이 추가해도 될 것 같은데, 가독성을 위해 )
            if e not in cost_graph[s]:
                cost_graph[s][e] = c

            # 시간 그래프에서 같은 간선이 존재하는데 더 적은 간선이 존재하는 경우 ( e in time_graph[s] 이 부분은 빼도 될텐데 )
            elif e in time_graph[s] and time_graph[s][e] > t:
                time_graph[s][e] = t

            # 비용 그래프에서도 마찬 가지
            elif e in cost_graph[s] and cost_graph[s][e] > c:
                cost_graph[s][e] = c
        print(time_graph)
        print(cost_graph)

        mincost = mincost_dijkstra(N)

        # 최소 비용보다 돈을 안 준 경우
        if mincost > M:
            print("Poor KCM")
            break

        else:
            mintime_dijkstra(N)











