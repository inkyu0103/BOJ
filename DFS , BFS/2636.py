# 2636
import sys
from collections import deque
import copy
input = sys.stdin.readline

def findStart():
    flag = 0
    for r in range(R):
        for c in range(C):
            if tmp_graph[r][c]:
                bfs((r,c))
                start_point.append((r,c))
                flag = 1

    if not flag:
        return -1


def bfs(start):
    q = deque([start])
    while(q):
        r,c = q.popleft()
        tmp_graph[r][c] = 0

        for move in dirs:
            nr , nc = r + move[0] , c + move[1]
            if 0<= nr <R and 0<= nc <C and tmp_graph[nr][nc]:
                q.append((nr,nc))


def special_bfs(start):
    q = deque([start])
    while(q):
        r,c = q.popleft()

        for move in dirs:
            nr,nc = r+move[0] , c+move[1]
            flag = 0

            if 0<=nr<R and 0<=nc<C:
                for m in dirs:
                    #공기중 노출!
                    if 0<=nr+m[0]<R and 0<= nc+m[1] < C and not graph[nr+m[0]][nc+m[1]]:
                        flag = 1
                        break
                if flag == 1:
                    # 현재 치즈 녹음
                    q.append((nr,nc))

                graph[r][c] = 0

if __name__ == "__main__" :
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    R,C = map(int,input().split())
    graph= [list(map(int,input().split())) for _ in range(R)]
    tmp_graph = copy.deepcopy(graph)

    # 치즈 컴포넌트의 시작 --> findStart 하면 start_point의 길이가 곧 컴포넌트 개수
    start_point = []
    findStart()
    # 이제 돌자
    for s in start_point:
        special_bfs(s)


