import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
Map = [list(map(int, list(input().rstrip()))) for _ in range(N)]
dist = [[[0] * M for _ in range(N)] for _ in range(2)]
di = [[1, 0], [0, 1], [-1, 0], [0, -1]]

for i in dist:
    print(i)

# dist[i][r][c] = i개 깬 상태에서 r/c 까지의 최단거리
# i,r,c
q = deque([[0, 0, 0]])
is_reach = False
answer = -1

while q:

    wall, cur_r, cur_c = q.pop()
    # print(f"wall : {wall} , cur_R : {cur_r} , cur_C :{cur_c}")

    for dr, dc in di:
        new_r, new_c = cur_r + dr, cur_c + dc

        if new_r == N - 1 and new_c == M - 1:
            is_reach = True
            answer = dist[wall][cur_r][cur_c] + 1
            break

        if new_r < 0 or new_r >= N or new_c < 0 or new_c >= M:
            continue

        else:
            if Map[new_r][new_c] and wall == 0 and not dist[1][new_r][new_c]:
                q.append([wall + 1, new_r, new_c])
                dist[wall + 1][new_r][new_c] = dist[wall][cur_r][cur_c] + 1

            if not Map[new_r][new_c] and not dist[wall][new_r][new_c]:
                q.append([wall, new_r, new_c])
                dist[wall][new_r][new_c] = dist[wall][cur_r][cur_c] + 1

    if is_reach:
        print("도달!", cur_r, cur_c)
        break

for i in dist:
    for j in i:
        print(j)
    print("---------")

print(answer + 1 if is_reach else -1)
