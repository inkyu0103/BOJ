# 2019 카카오 개발자 겨울 인턴십 > 징검다리 건너기

from collections import deque

def solution(stones, k):
    min_value = min(stones)

    q = deque(stones)
    length = len(stones)
    answer = min_value

    # 최솟값 빼기
    for i in range(length):
        q[i] -= min_value

    # 돌기
    zero_cnt = 0
    rotate_cnt = 0
    while (1):
        if q[0] == 0:
            zero_cnt += 1
            if zero_cnt == k:
                return answer

        else:
            q[0] -= 1
            zero_cnt = 0

        q.rotate(-1)
        rotate_cnt += 1
        if rotate_cnt == length:
            answer += 1
            rotate_cnt = 0

    return answer