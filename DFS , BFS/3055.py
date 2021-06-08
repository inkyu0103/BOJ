# 3055 탈출
import sys
from collections import deque
input = sys.stdin.readline
dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def bfs(start):
    global graph
    q = deque([start])

    while(q):
        cur_r,cur_c = q.popleft()

        for move in dirs:
            nr,nc = cur_r+move[0],cur_c+move[1]

            if 0<=nr<R and 0<=nc<C and graph[cur_r][cur_c] == "*":
                q.append((nr,nc))
                graph[nr][nc] = "*"
            elif 0<=nr<R and 0<=nc<C and graph[cur_r][cur_c] == "S":
                q.append((nr,nc))
                graph[nr][nc] = "S"




if __name__ =="__main__":
    R,C = map(int,input().split())
    graph = []
    a_start = (-1,-1)
    w_start = (-1,-1)
    for i in range(R):
        tmp_val = list(input().strip())
        if 'S' in tmp_val:
            start = (i,tmp_val.index('S'))
        elif '*' in tmp_val:
            w_start = (i,tmp_val.index('*'))
        graph.append(tmp_val)



