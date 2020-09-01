# 1219 오민식의 고민

import sys
INF = sys.maxsize




N ,start_city,end_city, M = map(int,input().split())
graph = [[] for _ in range(N)]

dist =[INF] * N
dist[start_city] = 0

for i in range(M):
    start,end,cost =  map(int,sys.stdin.readline().split())
    # 단방향
    graph[start].append([end,cost])

get_money = list(map(int,input().split()))
myMoney = get_money[start_city]

for v in range(N):
    #v가 출발점 [도착, 비용] --> [도착 , 도착해서 받을 수 있는 돈 - 갈때 드는 비용  ]
    for g in graph[v]:
        g[1] = get_money[0] - g[1]

def solve () :
    for it in range(N):
        for v in range(N):
            for e , cost in graph[v]:
                









print(graph)
print(get_money)
