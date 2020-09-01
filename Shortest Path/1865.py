# 1865
'''
    도로는 양방향 / 웜홀은 방향 그래프
    새로 갱신할 때


    벨만 포드를 한번만 사용해도 되는걸까
'''

import sys

INF = 1e9


def solve():

    for n in range(N):
        for edge in edges:
            if dist[edge[1]] > dist[edge[0]] + edge[2]:
                dist[edge[1]] = dist[edge[0]] + edge[2]

                if n == N - 1:
                    print("YES")
                    return

    print("NO")
    return


tc = int(input())
for i in range(tc):
    N, M, W = map(int, input().split())

    dist = [INF] * N
    dist[0] = 0
    edges = []

    # 도로 (양방향)
    for i in range(M):
        start, end, time = map(int, sys.stdin.readline().split())
        edges.append((start - 1, end - 1, time))
        edges.append((end - 1, start - 1, time))


    # 웜홀 (단방향)
    for i in range(W):
        start, end, time = map(int, sys.stdin.readline().split())
        edges.append((start - 1, end - 1, -time))


    solve()
