# 2887 행성 터널 ( 메모리 초과 )
import sys
input = sys.stdin.readline

def dist(node1,node2):
    x1,y1,z1,idx1 = node1
    x2,y2,z2,idx2 = node2
    return min(abs(x2-x1),abs(y2-y1),abs(z2-z1))

def Prim():
    global minWeight,N
    ret = 0
    minWeight[0] = 0
    for _ in range(N):
        u = - 1
        for v in range(N):
            if not added[v] and (u==-1 or minWeight[u] > minWeight[v]):
                u = v
        ret += minWeight[u]
        added[u] = 1

        for v,dis in graph[u]:
            print("v is {} dis is {}".format(v,dis))
            if not added[v] and minWeight[v] > dis:
                print("갱신 ! ")
                minWeight[v] = dis
                print(minWeight)

    return ret

if __name__ =="__main__":
    N = int(input())
    graph = [[] for _ in range(N)]
    Node = []
    added = [0] * N
    minWeight = [sys.maxsize] * N

    # 위치 입력받기
    for idx in range(N):
        x,y,z = map(int,input().split())
        Node.append((x,y,z,idx))

    # 행성간 간선거리 입력
    # x좌표 기준
    Node.sort(key=lambda x:x[0])
    for i in range(N-1):
        dis = dist(Node[i],Node[i+1])
        graph[i].append((i+1,dis))
        graph[i+1].append((i,dis))

    # y좌표 기준
    Node.sort(key=lambda x:x[1])
    for i in range(N-1):
        dis = dist(Node[i],Node[i+1])
        graph[i].append((i+1,dis))
        graph[i+1].append((i,dis))

    # z좌표 기준
    Node.sort(key=lambda x:x[2])
    for i in range(N-1):
        dis = dist(Node[i],Node[i+1])
        graph[i].append((i+1,dis))
        graph[i+1].append((i,dis))


    print(graph)

    print(Prim())



