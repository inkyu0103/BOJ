# 9370 마음을 다잡고...

import sys
import heapq
import math

#틀린 이유 math.inf 가 잘못 된 듯 싶다.


def dijkstra(start):
    q = []
    q.append([0, start])
    dist = [math.inf] * (n + 1)
    dist[start] = 0

    while q:
        weight, p_node = heapq.heappop(q)
        for n_node, n_weight in graph[p_node]:
            nw = weight+ n_weight
            if dist[n_node] > nw:
                dist[n_node] = nw
                heapq.heappush(q,[nw, n_node])

    return dist


testCase = int(input())

for _ in range(testCase):
    n ,m ,t = map(int,sys.stdin.readline().split())
    s ,g, h = map(int,sys.stdin.readline().split())

    graph = [[] for i in range(n+1)]
    destination = []

    #간선
    for e in range(m):
        a, b, d = map(int,sys.stdin.readline().split())
        graph[a].append([b,d])
        graph[b].append([a,d])



    #후보
    for c in range(t):
        destination.append(int(input()))

    s_to_all = dijkstra(s)
    g_to_all = dijkstra(g)
    h_to_all = dijkstra(h)

    result = []
    for v in destination:
        if s_to_all[g] + g_to_all[h]+h_to_all[v] == s_to_all[v] or s_to_all[h]+h_to_all[g]+g_to_all[v] == s_to_all[v]:
            result.append(v)

    result.sort()

    for i in result:
        print(i, end=' ')
    print()




