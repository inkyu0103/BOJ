# 4179 불!

from collections import deque
import sys

input = sys.stdin.readline
INF = 10000


R, C = map(int, input().split())
graph = [list(input().strip()) for _ in range(R)]
z_r, z_c, f_r, f_c = -1, -1, -1, -1
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

# print(graph)

# 지훈이가 움직이는 경로와 불이 퍼지는 경로를 따로 구해준다. 1은 지훈, 2는 불
queue1, queue2 = deque(), deque()
dist1, dist2 = [[INF] * C for _ in range(R)], [[INF] * C for _ in range(R)]

# 우선 지훈이와 불의 초기 좌표를 찾는다.
for r in range(R):
    for c in range(C):
        if graph[r][c] == "J":
            queue1.append([r, c])
            dist1[r][c] = 0
        elif graph[r][c] == "F":
            queue2.append([r, c])
            dist2[r][c] = 0
        else:
            continue

# 불부터 BFS를 실행한다.
while queue2:
    cur_r, cur_c = queue2.popleft()

    for i in range(4):
        new_r, new_c = cur_r + dr[i], cur_c + dc[i]

        # new_r,new_c가 범위안에 들어오고 / 아직 방문한 적이 없으며 / 벽이 아닌 경우 dist2[new_r][new_c] 거리를 갱신해준다.
        if (
            0 <= new_r < R
            and 0 <= new_c < C
            and dist2[new_r][new_c] == INF
            and graph[new_r][new_c] != "#"
        ):
            dist2[new_r][new_c] = dist2[cur_r][cur_c] + 1
            queue2.append([new_r, new_c])

# 지훈이의 BFS를 실행한다.

is_possible = False
dist = 0
while queue1:
    cur_r, cur_c = queue1.popleft()

    for i in range(4):
        new_r, new_c = cur_r + dr[i], cur_c + dc[i]
        # print(dr[i], dc[i])
        """
        print(
            "cur_r, cur_c : (", cur_r, cur_c, ")", "new_r,new_c : (", new_r, new_c, ")"
        )
        """

        if new_r < 0 or new_r >= R or new_c < 0 or new_c >= C:
            is_possible = True
            dist = dist1[cur_r][cur_c] + 1
            break

        # new_r,new_c가 범위에 들어오고 / 아직 방문한 적이 없으며 / 벽이 아니고 / 방문 예정인 곳의 거리가 불이 도착한 거리보다 빠를 경우 갱신해준다.
        if (
            # 0 <= new_r < R
            # and 0 <= new_c < C
            dist1[new_r][new_c] == INF
            and graph[new_r][new_c] != "#"
            and dist1[cur_r][cur_c] + 1 < dist2[new_r][new_c]
        ):
            dist1[new_r][new_c] = dist1[cur_r][cur_c] + 1
            queue1.append([new_r, new_c])

    if is_possible:
        break


print(dist if is_possible else "IMPOSSIBLE")

"""
반례1 -> 해결 
....
.JF.
....
....

답: 2
출력 : 4


반례 2 -> 불이 2개 이상인 경우
반례 3 -> 불이 없는 경우? -> -1로 초기화해서 생기는 문제 해결
5 4
####
#...
#.##
#.J#
####

for x in dist2:
    print(*x)

print("----------------------------")

for x in dist1:
    print(*x)


"""
