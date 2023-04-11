from collections import deque


def is_bound(r, c, N):
    return 0 <= r < N and 0 <= c < N


def solution(board, aloc, bloc):
    answer = 0
    board_length = len(board)
    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    visit_a = [[[0, 0] for c in range(board_length)] for r in range(board_length)]
    visit_b = [[[0, 0] for c in range(board_length)] for r in range(board_length)]

    def bfs_a():
        q = deque([aloc])
        r, c = aloc
        # 방문 여부, 움직인 step 수
        visit_a[r][c] = [1, 0]

        while q:
            cur_r, cur_c = q.popleft()

            for dr, dc in dirs:
                new_r, new_c = cur_r + dr, cur_c + dc

                if (
                    is_bound(new_r, new_c, board_length)
                    and not visit_a[new_r][new_c][0]
                ):
                    visit_a[new_r][new_c] = [1, visit_a[cur_r][cur_c][1] + 1]
                    q.append([new_r, new_c])

    def bfs_b():
        q = deque([bloc])
        r, c = bloc
        visit_b[r][c] = [1, 0]

        while q:
            print(q)
            cur_r, cur_c = q.popleft()

            for dr, dc in dirs:
                new_r, new_c = cur_r + dr, cur_c + dc

                if (
                    is_bound(new_r, new_c, board_length)
                    and not visit_b[new_r][new_c][0]
                    and visit_a[new_r][new_c][1] > visit_b[new_r][new_c][1]
                ):
                    print(new_r, new_c)
                    visit_b[new_r][new_c] = [1, visit_b[cur_r][cur_c][1] + 1]
                    q.append([new_r, new_c])

    bfs_a()
    bfs_b()

    for i in visit_b:
        print(i)

    return answer


solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1, 0], [1, 2])
