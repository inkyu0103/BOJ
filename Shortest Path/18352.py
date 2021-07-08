# 18352 특정 거리의 도시 찾기
'''
단방향 도로 / 모든 도로의 거리 1
모든 도로의 거리가 1이라 BFS 로도 접근할 수 있을 듯
?? 왜때문에 정답률 27%?

가중치가 어차피 1이라 더 작은 간선에 대한 갱신은 필요없음
메모리부족도 아닐거 같은데 두구두구두구두구 3132ms

1240ms는 뭘까
'''
import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(start_node):
    q = [(0,start_node)]

    while q:
        curWei, curNode = heapq.heappop(q)
        # 현재 기록된 거리보다 더 높은 가중치를 뽑으면 --> pass
        if dist[curNode] < curWei:
            continue

        for n in graph[curNode]:
            nextWei, nextNode = n
            newWei = nextWei + curWei

            if dist[nextNode] > newWei:
                dist[nextNode] = newWei
                heapq.heappush(q,(newWei,nextNode))

if __name__ == '__main__':
    # N:도시 개수 , M:도로개수 , K: 거리정보, X:출발 도시번호
    N,M,K,X = map(int,input().split())
    graph = [[] for _ in range(N+1)]
    answer = []

    dist = [INF]*(N+1)
    dist[X] = 0

    for m in range(M):
        s,e = map(int,input().split())
        graph[s].append((1,e))

    dijkstra(X)

    for i in range(len(dist)):
        if dist[i] == K:
            answer.append(i)

    answer.sort()
    if not answer:
        print(-1)

    else:
        for i in answer:
            print(i)
