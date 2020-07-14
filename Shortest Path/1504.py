#1504
import sys
import heapq
import math

INF = math.inf
# N : 정점 개수 , E : 간선 개수
N, E = map(int,sys.stdin.readline().split())

Graph = [[] for _ in range(N+1)]

#그래프 만들기
for _ in range(E):
    s, l, w = map(int,sys.stdin.readline().split())
    #양방향
    Graph[s].append([w,l])
    Graph[l].append([w,s])


#반드시 지나가야 하는 정점 정보
V1,V2 = map(int,sys.stdin.readline().split())

def dijkstra (Map,start,last):
    # 주어지는 두 정점 사이에 연결이 되어있나.
    q = []
    dist = [INF] * (N + 1)
    dist[start]=0
    #초기 값
    q.append([0,start])

    while q:
        cost , node = heapq.heappop(q)

        for c , n in Map[node]:
            if dist[n] > c + dist[node]:
                c += cost
                dist[n] = c
                heapq.heappush(q,[c,n])

    return dist[last]

ans1 = dijkstra(Graph,1,V1)+dijkstra(Graph,V1,V2)+dijkstra(Graph,V2,N)
ans2 = dijkstra(Graph,1,V2)+dijkstra(Graph,V2,V1)+dijkstra(Graph,V1,N)

if (ans1 == INF and ans2 == INF):
    print(-1)
else:
    print(min(ans1,ans2))

'''
1 --> v1 --> v2 --> N
1 --> v2 --> v1 --> N
특정 정점을 방문하고, 최단거리...?

일단 다익스트라를 통해서 1번 노드부터 모든 노드의 거리를 잰다.
둘 중에 하나라도 INF 면 길이 없는 것이다.

. 이전 노드들이 있는 리스트를 뒤져보자
1 -> N까지 가는 방법중에 각각의 이전 노드가 표시 되어 있을 텐데.
이전노드 역 추적을 해보아야 하나?

'''

