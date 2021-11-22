# 2638 치즈

import sys
from collections import deque
input = sys.stdin.readline

'''
cheese 1 _map에 1로 표시 / _visit 에 0 

outer air 2 / _map에 2로 표시 , _visit에 1

inner air 3  / _map,_visit에 둘 다 0
'''


def sol():
    def check_outer_air(r,c):
        q = deque([[r,c]])
        _visit[r][c] = 1

        while q:
            cur_r,cur_c= q.popleft()
            for dr,dc in dirs:
                new_r,new_c = cur_r+dr,cur_c+dc

                # _map이 비어있고, 방문하지 않은 경우 , map에 2로 표시해준다.
                if 0<=new_r<N and 0<=new_c <M and not _map[new_r][new_c] and not _visit[new_r][new_c] :
                    q.append([new_r,new_c])
                    _map[new_r][new_c] = 2



    def melt_cheese(cheeses):
        '''map에서 outer air로 바꾸고 , 방문처리 해주자.'''
        for r,c in cheeses:
            _map[r][c] = 2
            _visit[r][c] = 1
            # 혹시 inner air과 연결되어 있는 경우를 대비...
            check_outer_air(r,c)


    def is_melt_target(r,c):
        count = 0
        for dr,dc in dirs:
            if 0 <= r+dr < N and 0<= c+dc < M and _map[r+dr][c+dc] == 2:
                count += 1
        return True if count >= 2 else False

    def find_cheese():
        candidate_cheese = []
        for r in range(N):
            for c in range(M):
                if _map[r][c] == 1 and is_melt_target(r,c):
                    candidate_cheese.append([r,c])

        return candidate_cheese

    dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    hours = 0
    N,M = map(int,input().rstrip().split())
    _map = [list(map(int,input().rstrip().split())) for _ in range(N)]
    _visit = [[0]*M for _ in range(N)]

    check_outer_air(0,0)

    while 1:
        is_exist = find_cheese()
        if not is_exist:
            break


        melt_cheese(is_exist)
        hours += 1

    print(hours)

sol()