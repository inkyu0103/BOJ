# 1167
import sys
from collections import deque
input = sys.stdin.readline

# 아 문제를 착각했다. 탐험하면서 거리가 늘어나면

def bfs():
    global length
    q = deque()
    q.append(1)

    curCount = 0
    targetCount = 1

    while(q):
        # 항상 어디서 visit을 갱신해야하는지 고민? 시행착오를 겪었는데.
        curNode = q.popleft()
        visit[curNode] = 1
        targetCount += 1


        for nextNode in graph[curNode]:
            if not visit[nextNode]:
                q.append(nextNode)

        # 데이터 타입에 따라 범위가 변하나?
        if curCount == targetCount:
            curCount = 0
            targetCount = len(q)
            length += 1


if __name__ == "__main__":
    V = int(input())
    graph=[[] for _ in range(V+1)]
    visit = [0]*(V+1)
    length = 0
    for _ in range(V):

        data = list(map(int,input().split()))
        # idx는 2씩 늘어난다.
        idx = 1
        start = data[0]
        while(data[idx] != -1):
            end,wei = data[idx+1],data[idx+2]
            graph[start].append((end,wei))
            idx += 2

    print(length)

