'''
두 큐의 합을 같게 만들자.

1. 합을 비교한다.
2. 큰 쪽 큐의 원소를 하나 뽑는다.
3. 작은쪽에 넣는다.
4. 같을 때까지 반복한다.


언제 만들 수 없을까?

가장 큰 원소가 나머지의 합보다 큰 경우
'''

from collections import deque


def solution(queue1, queue2):
    total = queue1 + queue2
    if sum(total) - max(total) < max(total):
        return -1

    answer = 0
    deque1 = deque(queue1)
    deque2 = deque(queue2)
    print(deque1,deque2)

    deque1_sum, deque2_sum = sum(deque1), sum(deque2)

    while deque1_sum != deque2_sum:

        if deque1_sum > deque2_sum:
            deque2.append(deque1.popleft())
            deque2_sum += deque2[-1]
            deque1_sum -= deque2[-1]

        elif deque1_sum < deque2_sum:
            deque1.append(deque2.popleft())
            deque1_sum += deque1[-1]
            deque2_sum -= deque1[-1]

        answer += 1
    return answer

solution([3,2,7,2],[4,6,5,1])