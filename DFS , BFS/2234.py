# 2234

import sys
from collections import deque
input = sys.stdin.readline

def filter(number,cur_r,cur_c):
    result = []
    # 서
    if not number & 1:
        result.append([cur_r,cur_c-1])
    # 북
    if not number & 2:
        result.append([cur_r-1,cur_c])
    # 동
    if not number & 4:
        result.append([cur_r,cur_c+1])
    # 남
    if not number & 8:
        result.append([cur_r+1,cur_c])

    return result





def sol():
    C,R = map(int,input().split())
    visit = [[0]*C for _ in range(R)]
    wall = [list(map(int,input().split())) for _ in range(R)]
    area_dict = {}
    max_area,room = 1,1

    def area_union():
        area_union_set = set()
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]

        for r in range(R):
            for c in range(C):
                for dr,dc in dirs:
                    new_r,new_c = r+dr,c+dc
                    if 0<=new_r<R and 0<=new_c<C and visit[new_r][new_c] != visit[r][c]:
                        area_union_set.add(area_dict[visit[new_r][new_c]]+area_dict[visit[r][c]])
        return max(area_union_set)

    def bfs(r, c):
        queue = deque([[r,c,1]])
        visit[r][c] = room
        local_area = 1

        while queue:
            cur_r,cur_c,cur_area = queue.popleft()

            for new_r,new_c in filter(wall[cur_r][cur_c],cur_r,cur_c):
                if 0<=new_r<R and 0<=new_c<C and not visit[new_r][new_c]:
                    queue.append([new_r,new_c,cur_area+1])
                    local_area+=1
                    visit[new_r][new_c] = room
        return local_area

    for r in range(R):
        for c in range(C):
            if not visit[r][c]:
                area = bfs(r,c)
                max_area = max(max_area,area)
                area_dict[room] = area
                room += 1




    print(room-1)
    print(max_area)
    print(area_union())



sol()
