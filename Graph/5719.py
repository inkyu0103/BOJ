#5719 거의 최단 경로

import sys
import heapq

INF = 1e20
val = sys.stdin.readline().rstrip()

#dijkstra
def dijkstra(D):
    q = []
    q.append([0,sCity])

    while q:
        Wei ,City = heapq.heappop(q)


        for nWei,nCity in graph[City]:
            nWei += Wei
            if D[nCity] > nWei:
                D[nCity] = nWei
                heapq.heappush(q,[nWei,nCity])
                #최솟 값으로 갱신이 될 때, 그 노드를 이전 노드로 취급한다.
                preNode[nCity] = City


#find path / ShortPath List에 reverse하게 담겨있다.
def findPath():
    global eCity
    endCity = eCity
    while 1:
        if preNode[endCity] != -1:
            shortPath.append(endCity)
            endCity = preNode[endCity]
        else:
            return


# 그래프에서 Shorted Path 제거 / 근데 for 문 돌면서 제거하면 안되는데 / 그래서 거리를 무한대로 바꿨다.
def delPath():
    for i in range(1, len(shortPath)):
        for j in range(len(graph[shortPath[i]])):
            w, c = graph[shortPath[i]][j]
            if c == shortPath[i - 1]:
                graph[shortPath[i]][j][0] = INF


while(val != "0 0"):
    city , road = map(int,val.split())
    sCity,eCity = map(int,sys.stdin.readline().split())

    dist = [INF] * city
    dist[sCity]=0

    graph=[[] for i in range(city)]
    preNode = [0]*city
    preNode[sCity] = -1

    # 장소는 0부터 N-1까지 이름이 붙어있음
    # a->b로 가는 길이 무조건 하나라는 보장이 없으므로 다 받아야함.


    #그래프 만들기
    for r in range(road):
        st,ed,wei = map(int,sys.stdin.readline().split())
        graph[st].append([wei,ed])

    dijkstra(dist)
    shortDis = dist[eCity]


    # 최단 경로가 여러개인 경우를 발견

    while(1):

        # shortPath 저장
        shortPath = []
        findPath()
        shortPath.append(sCity)


        # shortPath 지우기
        delPath()


        nDist = [INF] * city
        nDist[sCity] = 0
        dijkstra(nDist)




        #기존의 최단 거리와 새로운 최단거리가 같으면 다시 제거 한다.
        if nDist[eCity] != shortDis:
            break


    if nDist[eCity] == INF:
        print(-1)
    else:
        print(nDist[eCity])
    val = sys.stdin.readline().rstrip()