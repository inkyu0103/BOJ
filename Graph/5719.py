#5719 거의 최단 경로

import sys
import heapq

INF = 1e20
val = sys.stdin.readline().rstrip()

#dijkstra + trace
def dijkstra():

    q = []
    q.append([0,sCity])

    dist = [INF] * city
    dist[sCity] = 0

    while q:
        Wei ,City = heapq.heappop(q)


        for nWei,nCity in graph[City]:
            nWei += Wei
            if dist[nCity] > nWei:
                dist[nCity] = nWei

                # 더 작은 값으로 갱신 될 경우 --> 모두 0으로 초기화 후 값 갱신
                for i in range(city):
                    trace[i][nCity] = 0

                trace[City][nCity] = 1
                heapq.heappush(q,[nWei,nCity])

            elif dist[nCity] == nWei:
                trace[City][nCity] = 1

    return dist





# 그래프에서 Shorted Path 제거 / 근데 for 문 돌면서 제거하면 안되는데 / 그래서 거리를 무한대로 바꿨다.
# path 모으기 (처음 node는 eCity)
# 아 문제 해결 : 그 일단 end 부분의 값이 더 작은 값으로갱신이 되면 싹다 0으로 초기화 하면 되네 와우!
def colPath(node):
    if node != sCity:
        for x in range(city):
            if trace[x][node]:
                    path.append((x,node))
                    colPath(x)






while(val != "0 0"):
    city , road = map(int,val.split())
    sCity,eCity = map(int,sys.stdin.readline().split())
    trace = [[0]*city for _ in range(city) ]
    graph=[[] for i in range(city)]
    path = []


    # 장소는 0부터 N-1까지 이름이 붙어있음
    # a->b로 가는 길이 무조건 하나라는 보장이 없으므로 다 받아야함.


    # 처음부터 최단경로를 찾지 못하는 경우
    # 최단 경로의 일부가 겹치는 경우 --> 최단 경로가 될 수 있는 간선을 모두 구한 후에 한번에 업데이트 해야함
    # 최단 거리를 갱신 및 같은 값일 경우에만 trace를 한다.

    #그래프 만들기
    for r in range(road):
        st,ed,wei = map(int,sys.stdin.readline().split())
        graph[st].append([wei,ed])


    f_dist = dijkstra()

    colPath(eCity)

    # 무한대로 바꾸기
    for i in path:
        st, ed = i
        for j in graph[st]:
            if j[1] == ed:
                j[0] = INF

    s_dist = dijkstra()



    if s_dist[eCity] == INF:
        print(-1)
    else:
        print(s_dist[eCity])






    val = sys.stdin.readline().rstrip()