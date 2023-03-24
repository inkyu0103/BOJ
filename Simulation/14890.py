# 14890 경사로
import sys

input = sys.stdin.readline


def is_walkable_downside(arr, cur_idx, is_slope):
    if cur_idx + L >= N:
        return False

    # 다음 L칸이 같아야 하므로
    for i in range(1, L + 1):
        if arr[cur_idx + 1] != arr[cur_idx + i] or is_slope[cur_idx + i]:
            return False

    for i in range(1, L + 1):
        is_slope[cur_idx + i] = 1

    return True


def is_walkable_upside(arr, cur_idx, is_slope):
    if cur_idx - L + 1 < 0:
        return False

    # 자신을 포함한 이전 L칸이 같아야 하므로
    for i in range(L):
        # 이 부분 좀 의심됨
        if arr[cur_idx] != arr[cur_idx - i] or is_slope[cur_idx - i]:
            return False

    for i in range(L):
        is_slope[cur_idx - i] = 1

    return True


def is_walkable(arr):
    cur_idx = 0
    is_slope = [0] * N

    while True:
        height_diff = abs(arr[cur_idx] - arr[cur_idx + 1])

        if height_diff >= 2:
            return 0

        if height_diff == 1:
            if arr[cur_idx] < arr[cur_idx + 1]:
                if not is_walkable_upside(arr, cur_idx, is_slope):
                    return 0

                else:
                    cur_idx += 1

            elif arr[cur_idx] > arr[cur_idx + 1]:
                if not is_walkable_downside(arr, cur_idx, is_slope):
                    return 0

                else:
                    cur_idx += 1

        else:
            cur_idx += 1

        if cur_idx == N - 1:
            # print("성공  :", arr)
            return 1


N, L = map(int, input().split())

_map = [list(map(int, input().split())) for _ in range(N)]

answer = 0

for arr in _map:
    answer += is_walkable(arr)

vertical_map = [[] for _ in range(N)]

for i in range(N):
    for j in range(N):
        vertical_map[i].append(_map[j][i])

for arr in vertical_map:
    answer += is_walkable(arr)

print(answer)
