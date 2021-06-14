# 4386 별자리 만들기
import sys
import math
input = sys.stdin.readline

def distance(x1,y1,x2,y2):
    return abs(math.sqrt((x2-x1)**2+(y2-y1)**2))

def sol():
    n = int(input())
    starInfo = []
    graph = [[] for _ in range(n)]
    minWeight = [sys.maxsize] * n
    visit = [0] * n
    parent = [0] * n
    selected = []

    for _ in range(n):
        x,y = map(float,input().split())
        starInfo.append((x,y))

    # 간선 추가
    for i in range(n):
        for j in range(i+1,n):
            dist = distance(starInfo[i][0],starInfo[i][1],starInfo[j][0],starInfo[j][1])
            graph[i].append((j,dist))
            graph[j].append((i,dist))
    minWeight[0] , parent[0] = 0,0
    result = 0
    for _ in range(n):
        u = -1
        for v in range(n):
            if not visit[v] and (u == -1 or minWeight[u] > minWeight[v]):
                u = v

        if parent[u] != u:
            selected.append((parent[u],u))

        result += minWeight[u]
        visit[u] = 1

        for i in range(len(graph[u])):
            nextNode ,weight = graph[u][i][0],graph[u][i][1]

            if not visit[nextNode] and minWeight[nextNode] > weight:
                parent[nextNode] = u
                minWeight[nextNode] = weight

    print(round(result,2))

sol()
