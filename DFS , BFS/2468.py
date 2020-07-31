#2468 안전영역
'''
뭐지 이거
2 <= x <= n-1 까지 모두 조사를 해봐야 하는데요?
'''
import sys
from collections import deque

def find():
    for y in range(N):
        for x in range(N):
            if graph[y][x] < N:
                return (y, x)

    return -1

def find2():
    for y in range(N):
        for x in range(N):
            if graph[y][x] != Flood:
                return (y, x)

    return -1


def BFS(cri):
    tmpGraph = graph.copy()
    while 1:
        val = find()

        if val == -1:
            return tmpGraph

        else:
            q = deque()
            sY, sX = val
            q.append((sY, sX))
            tmpGraph[sY][sX] = Flood

            while q:
                y, x = q.popleft()

                for move in dirs:
                    newY = y + move[0];
                    newX = x + move[1]
                    if 0 <= newY < N and 0 <= newX < N and tmpGraph[newY][newX] < cri:
                        q.append((newY, newX))
                        tmpGraph[newY][newX] = Flood


def BFS2(G):
    count =0
    while 1:
        val = find2()
        if val == -1:
            return count

        else:
            q = deque()
            sY, sX = val
            q.append((sY, sX))
            G[sY][sX] = Flood

            while q:
                y, x = q.popleft()

                for move in dirs:
                    newY = y + move[0];
                    newX = x + move[1]
                    if 0 <= newY < N and 0 <= newX < N and G[newY][newX] != Flood:
                        q.append((newY, newX))
                        G[newY][newX] = Flood

            count +=1



Flood = 1e20
N = int(input())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
dirs = [(0,1),(0,-1),(1,0),(-1,0)]
count = 0
maxRegion = 0
maxHeight = max(max(graph))




for x in range(0,maxHeight):
    if x == 0:
        maxRegion = 1

    TMP = BFS(x)
    tempMax = BFS2(TMP)
    if maxRegion < tempMax :
        maxRegion = tempMax

print(maxRegion)





