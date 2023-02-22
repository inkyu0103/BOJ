import sys

input = sys.stdin.readline


def rotate():
    rotate_sticker = [[0] * R for _ in range(C)]

    for r in range(R):
        for c in range(C):
            rotate_sticker[c][R - r - 1] = sticker[r][c]

    return rotate_sticker


def attachable(start_r, start_c):
    # 스티커가 붙을 수 있는지 확인
    for r in range(R):
        for c in range(C):
            if result[start_r + r][start_c + c] == 1 and sticker[r][c]:
                return False

    # 붙을 수 있다면? 붙인다
    for r in range(R):
        for c in range(C):
            if sticker[r][c]:
                result[start_r + r][start_c + c] = 1
    # 붙일 수 있음을 알려줌
    return True


N, M, K = map(int, input().split())
result = [[0] * M for _ in range(N)]
answer = 0

for _ in range(K):
    R, C = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(R)]

    for _ in range(4):
        is_attachable = False

        for r in range(N - R + 1):
            if is_attachable:
                break
            for c in range(M - C + 1):
                if attachable(r, c):
                    is_attachable = True
                    break

        if is_attachable:
            break
        sticker = rotate()
        R, C = C, R

for r in range(N):
    for c in range(M):
        # 오호 이런거 좋다.
        answer += result[r][c]


print(answer)
