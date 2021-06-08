# 11725 트리의 부모 찾기

import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    q = deque()
    visit[1] = 1
    q.append(1)


    while(q):
        curNode = q.popleft()

        for nextNode in graph[curNode]:
            if not visit[nextNode]:
                visit[nextNode] = curNode
                q.append(nextNode)



if __name__ =="__main__":
    V = int(input())
    graph = [[] for _ in range(V+1)]
    visit = [0] * (V+1)

    for i in range(V-1):
        s,e = map(int,input().split())
        graph[s].append(e)
        graph[e].append(s)

    bfs()
    for i in visit[2:]:
        print(i)




