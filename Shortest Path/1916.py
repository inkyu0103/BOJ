# 1916 최소비용 구하기
import sys
from collections import deque
import heapq
input = sys.stdin.readline

def dijkstra (start):
    dist[start] = 0
    pq = []

    # Node , Wei
    heapq.heappush(pq,(0,start))
    while(pq):
        wei,curNode = heapq.heappop(pq)
        # 이미 더 짧은 경로를 알고있는 경우 --> 무시
        if dist[curNode] < wei: continue
        for nextWei,nextNode in graph[curNode]:
            newWei = nextWei + wei
            # 거리 갱신
            if dist[nextNode] > newWei:
                dist[nextNode] = newWei
                pq.append((newWei,nextNode))


if __name__ =="__main__":
    # N : City , M: Bus
    N = int(input())
    M = int(input())
    dist = [sys.maxsize]*(N+1)
    graph = [[] for _ in range(N+1)]
    # 간선 입력
    for _ in range(M):
        s,e,w = map(int,input().split())
        graph[s].append((w,e))
    # 시작도시, 끝도시
    start,end = map(int,input().split())
    dijkstra(start)
    print(dist[end])
