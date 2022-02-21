# 3184
'''
한 영역에서 양의 수가 늑대보다 많으면 늑대는 살아남을 수 있다.
탈출 하는 경우가 있는지 모르겠네...?

각 영역을 돌면서, 한 영역 당 늑대와 양 수를 세어야 한다.

'''

import sys
from collections import deque
input = sys.stdin.readline

def sol():
    R,C = map(int,input().split())
    dirs = [[0,1],[0,-1],[1,0],[-1,0]]
    grass_land = [list(input().strip()) for _ in range(R)]
    visit = [[0]*C for _ in range(R)]

    total_sheep,total_wolf = 0,0


    def count_animals(r,c):
        q = deque([[r,c]])
        visit[r][c] = 1
        local_sheep , local_wolf = 1 if grass_land[r][c] == 'o' else 0 ,1 if grass_land[r][c] == 'v' else 0

        while q:
            cur_r,cur_c = q.popleft()

            for dr,dc in dirs:
                new_r,new_c = cur_r+dr,cur_c+dc

                if 0<=new_r<R and 0<=new_c<C and not visit[new_r][new_c]:
                    if grass_land[new_r][new_c] == '.':
                        q.append([new_r,new_c])

                    if grass_land[new_r][new_c] == 'o':
                        q.append([new_r,new_c])
                        local_sheep += 1

                    if grass_land[new_r][new_c] == 'v':
                        q.append([new_r,new_c])
                        local_wolf += 1

                    visit[new_r][new_c] = 1

        return local_sheep,local_wolf


    for r in range(R):
        for c in range(C):
            if not visit[r][c] and grass_land[r][c] != '#':

                sheep,wolf = count_animals(r,c)

                if sheep > wolf:
                    total_sheep += sheep

                else:
                    total_wolf += wolf

    print(total_sheep, total_wolf)


sol()
