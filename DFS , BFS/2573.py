# 2573 빙산
from collections import deque
import sys
input = sys.stdin.readline

def sol():
    # year은 한 해가 지날 때마다 빙하를 없애준다.
    def year():
        acc = [[0]*M for _ in range(N)]
        for r in range(N):
            for c in range(M):
                if ocean[r][c]:
                    count = 0
                    # 주위에 비어있는 곳 확인
                    for dr,dc in dirs:
                        new_r,new_c =r+dr,c+dc
                        if 0<= new_r <N and 0<=new_c<M and not ocean[new_r][new_c]:
                            count += 1
                    acc[r][c] = count

        for r in range(N):
            for c in range(M):
                if ocean[r][c]:
                    ocean[r][c] = max(0,ocean[r][c]-acc[r][c])

    def is_glacier():
        flag = 0
        visit = [[0]*M for _ in range(N)]
        for r in range(N):
            for c in range(M):
                if ocean[r][c]:
                    flag = 1
                    # 일단 bfs로 죽 둘러본다.
                    q = deque()
                    q.append([r,c])
                    visit[r][c] = 1

                    while q:
                        r,c = q.popleft()
                        for dr,dc in dirs:
                            new_r,new_c = r+dr,c+dc

                            if 0<=new_r<N and 0<=new_c<M and ocean[new_r][new_c] and not visit[new_r][new_c]:
                                visit[new_r][new_c] = 1
                                q.append([new_r,new_c])

                    for x in range(N):
                        for y in range(M):
                            # 만약 빙하는 있는데, 방문한 흔적이 없다면, segment가 2개 이상. 그러므로, 원하는 조건에 만족.
                            if ocean[x][y] and not visit[x][y]:
                                return 1
                    return 2

        # 빙하가 없네?
        if not flag:
            return 0


    dirs=[(0,1),(0,-1),(1,0),(-1,0)]
    N,M = map(int,input().split())
    ocean = [list(map(int,input().split())) for _ in range(N)]
    years = 0


    while 1:
        year()
        years += 1


        val = is_glacier()

        if not val :
            print(0)
            return

        elif val == 1:
            print(years)
            return

        elif val == 2:
            continue


sol()
