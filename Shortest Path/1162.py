# 1162

import sys
input = sys.stdin.readline
INF = sys.maxsize


def floyd():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
                    route[i][j] = route[i][k]

def findRoute():
    start = 0
    end = N-1
    route_dp = [0]
    while(1):
        val  = route[start][end]
        print(val)
        if val == 0:
            break
        val -=1
        start = val
        route_dp.append(start)

    return route_dp



def cal_time (target):
    length = len(target)-1
    dist = []
    for i in range(length):
        dist.append(graph[i][i+1])

    dist.sort()
    print(dist)
    for _ in range(K):
        dist.pop()

    print(dist)
    return sum(dist)



if __name__ == '__main__':
    N,M,K = map(int,input().split())
    graph = [[INF]*(N) for _ in range(N)]
    route = [[0]*(N) for _ in range(N)]

    for i in range(N):
        graph[i][i] = 0

    for _ in range(M):
        s,e,t = map(int,input().split())
        graph[s-1][e-1] = t
        graph[e-1][s-1] = t

        route[s-1][e-1] = e
        route[e-1][s-1] = s

    floyd()
    route_dp = findRoute()
    print(cal_time(route_dp))



