#1021
from collections import deque

def sol():
    N, M = map(int,input().split())
    pick_data = list(map(int,input().split()))
    data = [i for i in range(1,N+1)]
    q = deque(data)
    count = 0

    # 자신의 위치에서 목표 대상까지 얼마만큼의 거리가 필요한지 계산 해야함.
    # .index()로 알면 되나...? --> 0을 기준으로 인덱스의 절댓값이 작은쪽으로 이동.

    # pick _data의 길이는 중간에 변하지 않도록 주의하자.
    for i in pick_data:

        q_length = len(q)
        location = q.index(i)

        if location <= q_length - location:
            count +=  location
            q.rotate(-location)
            q.popleft()

        else:
            count += q_length - location
            q.rotate(q_length-location)
            q.popleft()

    print(count)
sol()
