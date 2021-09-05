# 아기 상어 응애

from collections import deque
import sys
input = sys.stdin.readline


def find_shark():
    for r in range(N):
        for c in range(N):
            # 상어가 있다면 위치 반환
            if ocean[r][c] == 9:
                return (r,c)

def bfs(r,c):
    global shark_initial_size,consume_times,eat_fish_num
    # queue에 들어가는 내용은 [step,r,c] --> sort()시 맨 앞에 것만 뽑으면 됩니다 ^.^
    q = deque([[0,r,c]])
    can_eat_fishes = []
    visit = [[0]*N for _ in range(N)]
    visit[r][c] = 1

    while q:
        cur_step,cur_r,cur_c = q.popleft()

        for dr,dc in dirs:
            new_step ,new_r, new_c = cur_step + 1 , cur_r+ dr, cur_c + dc

            # 상어의 크기보다 작으면 지나갈 수 있음. --> 1.비어있는 경우 /2.자신보다 크기가 작은 경우 /3.자신과 크기가 같은 경우
            if 0<= new_r < N and 0<= new_c<N and ocean[new_r][new_c] <= shark_initial_size and not visit[new_r][new_c]:
                # 자신보다 크기가 작은 물고기가 있는 경우 추가
                if ocean[new_r][new_c] and ocean[new_r][new_c] <shark_initial_size:
                    can_eat_fishes.append((new_step,new_r,new_c))

                q.append((new_step,new_r,new_c))
                visit[new_r][new_c] = 1
    can_eat_fishes.sort()

    if can_eat_fishes:
        step, nr,nc = can_eat_fishes[0]

        # 먹은 물고기는 깔끔하게 'ㅇ'
        ocean[r][c] = 0
        ocean[nr][nc] = 9



        # 물고기 먹으러 달려간 시간
        consume_times += step
        eat_fish_num += 1

        # 상어 크기가 커졌나?
        if shark_initial_size == eat_fish_num:
            shark_initial_size += 1
            eat_fish_num = 0


        return nr,nc

    return 0



N = int(input())
ocean = [list(map(int,input().split())) for _ in range(N)]
dirs =[(0,1),(0,-1),(1,0),(-1,0)]
shark_start_location = find_shark()
shark_initial_size = 2
eat_fish_num = 0
consume_times = 0

shark_location = deque([shark_start_location])

while shark_location:
    cur_r,cur_c = shark_location.popleft()

    next_val = bfs(cur_r,cur_c)

    if next_val :
        shark_location.append(next_val)

print(consume_times)

# 쩝 다 한거 같은데 뭔가 빠진거 같네 'ㅇ'....?






