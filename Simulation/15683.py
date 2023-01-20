from itertools import product
import copy


def step(r, c, office, cardinal):
    dr, dc = -1, -1

    # 방향 분석
    if cardinal == 0:
        dr, dc = -1, 0

    elif cardinal == 1:
        dr, dc = 0, 1

    elif cardinal == 2:
        dr, dc = 1, 0

    elif cardinal == 3:
        dr, dc = 0, -1

    # 움직이기
    while True:

        # 새롭게 좌표 갱신
        r, c = r + dr, c + dc

        if (r < 0 or r >= R or c < 0 or c >= C) or office[r][c] == 6:
            break
        if office[r][c]:
            continue
        office[r][c] = 7


R, C = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(R)]
camera_counts = 0
answer = 64

# 카메라 개수 세기
for r in range(R):
    for c in range(C):
        if office[r][c] and office[r][c] < 6:
            camera_counts += 1


cardinal_points = list(product([0, 1, 2, 3], repeat=camera_counts))
# print(cardinal_points)


for points in cardinal_points:
    copy_office = copy.deepcopy(office)
    count = 0
    # print("points is :", points)

    for r in range(R):
        for c in range(C):
            if office[r][c] and office[r][c] < 6:
                if office[r][c] == 1:
                    step(r, c, copy_office, points[count] % 4)
                elif office[r][c] == 2:
                    step(r, c, copy_office, points[count] % 4)
                    step(r, c, copy_office, (points[count] + 2) % 4)
                elif office[r][c] == 3:
                    step(r, c, copy_office, points[count] % 4)
                    step(r, c, copy_office, (points[count] + 3) % 4)

                elif office[r][c] == 4:
                    step(r, c, copy_office, points[count] % 4)
                    step(r, c, copy_office, (points[count] + 1) % 4)
                    step(r, c, copy_office, (points[count] + 2) % 4)

                elif office[r][c] == 5:
                    step(r, c, copy_office, points[count] % 4)
                    step(r, c, copy_office, (points[count] + 1) % 4)
                    step(r, c, copy_office, (points[count] + 2) % 4)
                    step(r, c, copy_office, (points[count] + 3) % 4)

                else:
                    continue

                # 다음 카메라가 보고 있는 방향
                count += 1

    temp_blind_side = 0
    # 다 돌면 카운팅
    for r in range(R):
        for c in range(C):
            if not copy_office[r][c]:
                temp_blind_side += 1

    # for x in copy_office:
    #    print(*x)
    # print("temp_blind_side : ", temp_blind_side)

    # print("----------------------------------")

    answer = min(answer, temp_blind_side)

print(answer)
