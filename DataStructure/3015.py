# 3015 오아시스 재결합
# 1차 시도 시간초과 아마  같은것이 많은 경우 문제가 될 거 같다. 스택보다 더 효율적인 것은...?
# 2차 시도 틀린 답. . .
# 3차 우선순위 큐
# 4차 deque
# 5차 예... 같은 걸 처리하는 방법에서 시간을 O지게 잡아먹었네요 ㅎㅎ;
# 반복문 스타일 고치기

import sys
import heapq

def sol () :
    people = int(sys.stdin.readline())
    people_data = [int(sys.stdin.readline()) for _ in range(people)]
    answer = 0
    queue = []

    for i in people_data:

        while queue and queue[-1][0] < i:
            answer += queue.pop()[1]

        if not queue:
            queue.append((i,1))
        else:
            #같은 경우
            if queue[-1][0] == i:
                cnt = queue.pop()[1]
                answer += cnt

                if queue:
                    answer += 1
                queue.append((i,cnt+1))

            else:
                queue.append((i,1))
                answer += 1

    print(answer)
sol()