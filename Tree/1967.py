# 1967 트리의 지름

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(start,beforeLength,nextLength):
    global length,maxNode
    visit[start] = 1
    curLength = beforeLength + nextLength

    if length < curLength:
        length = curLength
        maxNode = start

    for nextNode in graph[start]:
        # 방문하지 않은 노드가 있다면
        if not visit[nextNode[0]]:
            dfs(nextNode[0],curLength,nextNode[1])


if __name__ == "__main__":
    V = int(input())
    graph = [[] for _ in range(V+1)]
    visit = [0] * (V+1)
    length = 0
    maxNode = 0

    # 그래프 입력
    for i in range(V-1):
        s,e,w = map(int,input().split())
        graph[s].append((e,w))
        graph[e].append((s,w))

    dfs(1, 0, 0)
    length = 0
    visit = [0] * (V + 1)
    dfs(maxNode, 0, 0)
    print(length)

