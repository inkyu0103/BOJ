import sys
from collections import deque
input = sys.stdin.readline


def findStartPoint():
    for r in range(N):
        for c in range(N):
            if graph[r][c] == 1:
                for move in dirs:
                    newR , newC = r + move[0], c+move[1]
                    if 0<=newR<N and 0<=newC<N and not graph[newR][newC] and (newR,newC) not in startPoint:
                        startPoint.append((newR,newC))
                        graph[newR][newC] = 2


if __name__ == '__main__':
    N = int(input())
    graph = [list(map(int,input().split(' '))) for _ in range(N)]
    dirs = [(0,1),(0,-1),(-1,0),(1,0)]
    startPoint = []
    for i in range(N):
        print(graph[i])

    print('-----------------------------------------------')
    findStartPoint()
    print(startPoint)
    for i in range(N):
        print(graph[i])


