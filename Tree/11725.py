# 11725 트리의 부모찾기
# 트리 루트가 1이다.
import sys
from collections import deque
input = sys.stdin.readline

def sol():

    num = int(input())
    parent = [i for i in range(num+1)]
    visit = [0]*(num+1)
    graph = [[] for _ in range(num+1)]

    while(1):
        s,e = map(int,input().split())
        graph[s].append(e)
        graph[e].append(s)

    def bfs():
        q = deque()
        root = 1

        # root
        for i in graph[1]:
            q.append(i)
            parent[i] = 1
        visit[root] = 1


        while(q):
            print(q)
            val = q.popleft()
            visit[val] = 1

            for i in graph[val]:
                if not visit[i]:
                    q.append(i)
                    parent[i] = val

    bfs()
    print(parent)



sol()