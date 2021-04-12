# 로봇청소기 재도전 ver2

import sys
input = sys.stdin.readline

dirs = [(-1,0),(0,1),(1,0),(0,-1)]

def sol():
    N,M = map(int,input().split())
    r,c,d = map(int,input().split())
    graph = [[int(i) for i in input().split()] for _ in range(N)]
    answer = 1
    search_count = 0

    # 초기에 청소한 방
    graph[r][c] = 2

    while(1):
        # 현재 방향 기준의 왼쪽?
        cur_left = d-1 if d-1>=0 else 3

        # 범위를 넘지 않는다면
        if 0<=r+dirs[cur_left][0]<N and 0<=c+dirs[cur_left][1] < M:
            if graph[r + dirs[cur_left][0]][c + dirs[cur_left][1]] == 0:
                # ㅇㅋ 회전시켜줄게
                d = cur_left; r += dirs[cur_left][0]; c += dirs[cur_left][1]
                answer += 1
                graph[r][c] = 2
                search_count = 0
            # 벽이거나 청소를 한 곳이라면?
            else:
                #회전만 해
                d= cur_left
                search_count += 1

        #범위를 넘는다면?
        else:
            search_count += 1

        if search_count == 4:
            if 0<=r-dirs[d][0]<N and 0<= c-dirs[d][1] < M:
                if graph[r-dirs[d][0]][c-dirs[d][1]] == 1:
                    print(answer)
                    return

                else:
                    r -= dirs[d][0] ; c -= dirs[d][1]
                    search_count = 0
                    continue
sol()

