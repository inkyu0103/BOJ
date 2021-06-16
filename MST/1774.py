# 1774 우주신과의 교감
import sys
import math
input = sys.stdin.readline

def dist(x1,y1,x2,y2):
    return abs(math.sqrt((x2-x1)**2 + (y2-y1)**2))

def Prim():
    global ret
    minWeight[1] = 0
    for _ in range(1,N+1):
        u = -1
        for v in range(1,N+1):
            if not added[v] and (u==-1 or minWeight[u] > minWeight[v]):
                u = v
        ret += minWeight[u]
        added[u] = 1

        for nextNode in graph[u]:
            nodeNum = nextNode
            wei = graph[u][nextNode]

            if not added[nodeNum] and minWeight[nodeNum] > wei:
                minWeight[nodeNum] = wei

if __name__ == "__main__":
    N,M =  map(int,input().split())
    added = [0] * (N+1)
    graph = [{} for _ in range(N+1)]
    minWeight = [sys.maxsize] * (N+1)
    Node = [(-1,-1)]
    ret = 0

    # 우주신 위치
    for _ in range(N):
        x,y = map(int,input().split())
        Node.append((x,y))

    # 위치 계산
    for i in range(N):
        for j in range(N):
            if i==j:
                continue
            graph[i+1][j+1] = dist(*Node[i+1],*Node[j+1])

    #연결되어있는 간선
    for _ in range(M):
        s,e = map(int,input().split())
        graph[s][e] = 0
        graph[e][s] = 0

    Prim()
    print(format(ret,".2f"))
