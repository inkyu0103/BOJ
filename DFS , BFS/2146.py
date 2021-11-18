'''
어떻게 푸나?
섬을 돌면서 길을 찾아 나가는 방식을 선택해야 한다.

저장해야 할 내용은 다음과 같다.
(r,c,움직인 칸 수)
큐에 넣긴 할 건데, 이전 내용만 담고 있도록 하자.

visit 배열을 쓸지. 아니면 0으로 초기화 한 이후에 0이 아닌 곳에만 탐색할지 생각해보자.
깔끔하게 풀고 싶으니 visit을 사용하자.
visit은 처음에 섬을 탐색할 때 쓰이고, 앞으로 edge가 update 될 때도 사용된다.

필요한 것

- island_edge : 2차원 배열로, 각 인덱스마다 섬의 edge 정보가 들어있다.
- 모든 구간 돌기 -> 1이 있는 구간부터 섬 정보, edge 정보를 업데이트 한다.
'''

import sys
from collections import deque
input = sys.stdin.readline

dirs = [(0,1),(0,-1),(1,0),(-1,0)]

def sol():
    def find_island(r,c,island_count):
        q = deque()
        q.append([r,c])
        visit[r][c] = 1

        while q:
            cur_r,cur_c = q.popleft()

            for dr,dc in dirs:
                new_r,new_c = cur_r+dr,cur_c+dc
                if 0<=new_r<N and 0<=new_c<N and not visit[new_r][new_c]:
                    # 땅인 경우
                    if island[new_r][new_c]:
                        visit[new_r][new_c] = 1
                        q.append([new_r,new_c])
                    # 바다인 경우는 edge 이므로...
                    else:
                        island_edge[island_count].append([cur_r,cur_c,0])
                        continue













    N = int(input())
    island_count = 0
    island = [list(map(int,input().split())) for _ in range(N)]
    visit = [[0]*N for _ in range(N)]
    island_edge = [deque() for _ in range(N)]

    # 전체 탐색
    for r in range(N):
        for c in range(N):
            if island[r][c] and not visit[r][c]:
                find_island(r,c,island_count)
                island_count +=1 ;

    print(island_edge)



sol()