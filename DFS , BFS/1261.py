# 1261 알고스팟

import sys
from collections import deque
input = sys.stdin.readline



def bfs():
    q = deque([(0,0)])

    while(q):

        x,y = q.popleft()
        for move in dirs:
            nx,ny = x+move[0] , y+move[1]

            if 0 <= nx < M and 0 <= ny < N and answer[ny][nx] == -1:
                if graph[ny][nx] == "0":
                    q.appendleft((nx,ny))
                    answer[ny][nx] = answer[y][x]

                else:
                    q.append((nx, ny))
                    answer[ny][nx] = answer[y][x] + 1


if __name__ == '__main__':
    # M : 가로 (column) - x , N : 세로 (row) - y
    M,N = map(int,input().split())
    graph = [list(input().strip()) for _ in range(N)]

    answer = [[-1]*M for _ in range(N)]
    answer[0][0] = 0

    dirs = [(0,1),(0,-1),(1,0),(-1,0)]

    bfs()

    print(answer[N-1][M-1])

