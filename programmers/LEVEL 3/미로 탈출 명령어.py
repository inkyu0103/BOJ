from collections import deque


# n(r) 행, m(c) 열
def is_boundary(r, c, n, m):
    return 0 <= r < n and 0 <= c < m


def is_dest(cur_r, cur_c, dest_r, dest_c):
    return cur_r == dest_r and cur_c == dest_c


def solution(n, m, x, y, r, c, k):
    start_r, start_c, end_r, end_c = x - 1, y - 1, r - 1, c - 1
    answer_candidates = []
    dirs = {
        "d": [1, 0],
        "l": [0, -1],
        "r": [0, 1],
        "u": [-1, 0],
    }

    # dist, commands ,r, c
    q = deque([[0, "", start_r, start_c]])

    _map = [[0] * m for _ in range(n)]

    while q:
        cur_dist, cur_command, cur_r, cur_c = q.popleft()

        for d in dirs:
            dr, dc = dirs[d]
            new_dist, new_command, new_r, new_c, = (
                cur_dist + 1,
                cur_command + d,
                cur_r + dr,
                cur_c + dc,
            )

            if is_boundary(new_r, new_c, n, m) and new_dist <= k:

                if abs(new_r - end_r) + abs(new_c - end_c) + cur_dist + 1 > k:
                    continue

                # 거리가 k이고 다음 좌표가 도착지인 경우
                if new_dist == k and is_dest(new_r, new_c, end_r, end_c):
                    answer_candidates.append(new_command)
                    continue

                # 아닌경우
                q.append([new_dist, new_command, new_r, new_c])

                break

    if not answer_candidates:
        return "impossible"

    answer_candidates.sort()
    return answer_candidates[0]
