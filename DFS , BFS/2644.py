#2644 촌수계산

import sys
input = sys.stdin.readline
from collections import deque


def bfs(start,end):
    chonsu = 0
    q = deque([start])
    visit[start] = 1

    length = 1
    count = 0


    while(q):
        curNode = q.popleft()
        count += 1

        for nextNode in graph[curNode]:
            print("nextNode is {}".format(nextNode))
            if nextNode == end:
                return chonsu

            if not visit[nextNode]:
                q.append(nextNode)
                visit[nextNode] = 1


        if count == length:
            count = 0
            length = len(q)
            chonsu += 1

    return -1

if __name__ == '__main__':
    n = int(input())
    start,end = map(int,input().split())

    graph = [[] for _ in range(n+1)]
    visit = [0] * (n+1)
    m = int(input())

    for  _ in range(m):
        s,e = map(int,input().split())
        graph[s].append(e)


    print(graph)


    print(bfs(start,end))
    print(visit)



