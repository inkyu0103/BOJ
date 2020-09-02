# 1219 오민식의 고민

import sys
from collections import deque

INF = -1e10
N ,start_city,end_city, M = map(int,input().split())
graph = [[] for _ in range(N)]
visited= [[] for _ in range(N)]
dist =[INF] * N

for i in range(M):
    start,end,cost =  map(int,sys.stdin.readline().split())
    # 단방향
    graph[start].append([end,cost])
    visited[start].append([end,False])

get_money = list(map(int,input().split()))
dist[start_city] = get_money[start_city]
# (start,end) 순으로 모을 것입니다.
last_relax =[]

for v in range(N):
    #v가 출발점 [도착, 비용] --> [도착 , 도착해서 받을 수 있는 돈 - 갈때 드는 비용  ]
    for g in graph[v]:
        g[1] = get_money[g[0]] - g[1]

# last_ relax 가 들어갈 자리
def bfs (arr):
    visit = list()
    q = deque()
    q.extend(arr)

    while q:
        s,e = q.popleft()
        visit.append((s,e))


        for item in visited[s]:
            if item[0] == e and item[1] == False:
                item[1] = True
                visit.append(item)
                for i in visited[e]:
                    if i[1] == False :
                        q.append((e,i[0]))


    return visit




def solve () :
    for it in range(N):
        for v in range(N):
            for e , cost in graph[v]:
                if dist[e] < dist[v] + cost :
                    dist[e] = dist[v] + cost
                    if it == N-1 :
                        last_relax.append((v,e))

        if it == N-1:
            final = bfs(last_relax)
            for i in final :
                # 도착 도시에 도달한다면
                if i[1] == end_city:
                    print("Gee")
                    return


    if dist[end_city] == INF:
        print("gg")
        return
    else:
        print(dist[end_city])
        return

solve()