# 14938

'''
어디로 낙하해야 자신의 수색 범위 내에서 가장 많은 아이템을 얻을 수 있는지?

양방향 통행 가능

수색범위 (1~15m)
다익스트라는 한 정점에서 모든 정점에 대한 최단 거리를 나타낸다.
'''


import sys
import math
import heapq

input = sys.stdin.readline

INF = math.inf


def sol():
    n, m, r = list(map(int, input().split()))
    item_numbers_list = list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]
    result = []

    # 그래프 입력
    for _ in range(r):
        start, end, cost = list(map(int, input().split()))
        graph[start].append([end, cost])
        graph[end].append([start, cost])

    for initial_node in range(1, n+1):
        # 초기화
        hq = [[initial_node, 0]]
        dist = [INF] * (n + 1)
        values = [0] * (n + 1)

        dist[initial_node] = 0
        values[initial_node] = item_numbers_list[initial_node - 1]
        tmp_result = 0


        # hq 돌면서 최단 경로 구하기
        while hq:
            print(hq)
            cur_node, cur_dist = heapq.heappop(hq)
            # 현재 기록되어있는 dist보다 cost가 더 크면 갱신할 필요 없음 -> 첫 번째 순회에서는 무조건 포함되게 되어있다.
            if dist[cur_node] < cur_dist:
                continue

            for node_info in graph[cur_node]:
                next_node, next_dist = node_info

                new_dist = cur_dist + next_dist

                if dist[next_dist] > new_dist and new_dist < m:
                    dist[next_dist] = new_dist
                    heapq.heappush(hq, [next_node, new_dist])


        print(dist)
        for i in range(1, len(dist)):
            if dist[i] != INF:
                tmp_result += item_numbers_list[i-1]
        print(tmp_result)






sol()
