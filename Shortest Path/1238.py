# 1238 파티
import sys
import heapq
input = sys.stdin.readline

def dijkstra(start,target_d,target_g):
    q = []
    heapq.heappush(q,(0,start))
    target_d[start] = 0

    while(q):
        wei,curNode = heapq.heappop(q)

        # 이게 어떤 경우지 --> 이미 계산된 거리보다 가중치가 더 크게되면, 갱신할 필요가 없어진다. 따라서 넘어감
        if target_d[curNode] < wei:
            continue

        # wei가 더 작거나 같은 경우 (갱신)
        for n in target_g[curNode]:
            nextWei, nextNode = n
            newWei = nextWei + wei

            if target_d[nextNode] > newWei:
                target_d[nextNode] = newWei
                heapq.heappush(q,(newWei,nextNode))


if __name__ =='__main__':
    N,M,X = map(int,input().split())
    graph = [[] for _ in range(N+1)]
    dist = [sys.maxsize]*(N+1)
    graph_r = [[] for _ in range(N+1)]
    dist_r = [sys.maxsize]*(N+1)


    for _ in range(M):
        # start, end , time
        s,e,t = map(int,input().split())
        # 정방향 그래프
        graph[s].append((t,e))
        # 역방향 그래프
        graph_r[e].append((t,s))

    dijkstra(X,dist,graph)
    dijkstra(X,dist_r,graph_r)
    max_val = -1
    for i in range(1,len(dist)):
        max_val = max(max_val,dist[i]+dist_r[i])


    print(max_val)






