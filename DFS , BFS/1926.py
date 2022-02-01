#1926 그림
from collections import deque
import sys
input = sys.stdin.readline

def sol():
    n,m = map(int,input().split())
    dirs=[[0,1],[0,-1],[1,0],[-1,0]]
    room,area = 0,0
    graph = [list(map(int,input().split())) for _ in range(n)]

    def bfs(r,c):
        q = deque([[r,c]])
        graph[r][c] = 0
        area = 1

        while q:
            cur_r,cur_c = q.popleft()

            for dr,dc in dirs:
                new_r,new_c = cur_r+dr,cur_c+dc

                if 0<=new_r<n and 0<=new_c<m and graph[new_r][new_c]:
                    graph[new_r][new_c] = 0
                    q.append([new_r,new_c])
                    area+=1

        return area



    for r in range(n):
        for c in range(m):
            if graph[r][c]:
                room += 1
                area = max(bfs(r,c),area)

    print(room)
    print(area)

sol()
