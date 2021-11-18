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

지금 중복되는게 문제

사방을 도는데, 자신의 땅일 가능성이 존재한다.
그러니까 음... visit을 좀 더 세분화 해서 문제를 풀면 되지 않을까?

1. island
2. island visit with number (island counter)
3. island for 간척사업


로직은 맞는 것 같은데 메모리 초과 해결을 어떻게 하지?

'''

import sys
from collections import deque
input = sys.stdin.readline

dirs = [(0,1),(0,-1),(1,0),(-1,0)]

def sol():
    def print_map():
        for r in range(N):
            print(island)
        print('-'*25)


    def find_island(r,c,island_count):
        q = deque()
        tmp_edge = deque()
        q.append([r,c])
        visit[r][c] = island_count

        while q:
            cur_r,cur_c = q.popleft()

            for dr,dc in dirs:
                new_r,new_c = cur_r+dr,cur_c+dc
                if 0<=new_r<N and 0<=new_c<N and not visit[new_r][new_c]:
                    # 땅인 경우
                    if island[new_r][new_c]:
                        visit[new_r][new_c] = island_count
                        q.append([new_r,new_c])
                    # 바다인 경우는 edge 이므로
                    else:
                        if [cur_r,cur_c,0] not in tmp_edge:
                            tmp_edge.append([cur_r,cur_c,0])


        island_edge.append(tmp_edge)





    N = int(input())
    min_length = sys.maxsize
    island_edge = []
    island = [list(map(int,input().split())) for _ in range(N)]
    visit = [[0]*N for _ in range(N)]
    island_count = 1


    # 전체 탐색
    for r in range(N):
        for c in range(N):
            if island[r][c] and not visit[r][c]:
                find_island(r,c,island_count)
                island_count += 1

    # 영역 넓히기
    while(1):
        meet_flag = 0
        for index,edges in enumerate(island_edge):
            max_pop_count = len(edges)
            while max_pop_count:
                cur_r,cur_c,step = edges.popleft()
                max_pop_count -= 1

                for dr,dc in dirs:
                    new_r,new_c = cur_r+dr,cur_c+dc
                    # 비어있는 땅이라면, 간척사업을 하자.
                    if 0<=new_r<N and 0<=new_c<N:
                        # visit이 0인 경우 (아예 섬이 아닌 경우)
                        if not visit[new_r][new_c]:
                            island[new_r][new_c] = step + 1
                            visit[new_r][new_c] = index + 1
                            edges.append([new_r,new_c,step+1])

                        # 여기에 자신의 섬이 아닌 조건이 추가되어야 한다. ( visit의 값이 0이 아닌 경우 island_num이 된다. )
                        elif index+1 != visit[new_r][new_c] :
                            min_length = min(min_length,step + island[new_r][new_c])
                            meet_flag = 1
        if meet_flag:
            break;

    print(min_length)

sol()