# 11286 절댓값 힙
# 절댓값이 가장 작은 아이를 뽑아야 하는데, -1,1 이 들어있으면 -1을 출력해야 하네, 큐에 넣을때 (절댓값, 원래값) 쌍으로 넣어야 하나?

import heapq
import sys

def sol():
    count = int(input())
    plus_queue=[]
    minus_queue=[]

    for i in range(count):
        command = int(sys.stdin.readline())

        # 모두 비었을 때
        if command == 0:
            if len(plus_queue) == 0 and len(minus_queue) == 0:
                print(0)
            elif len(plus_queue) == 0 and len(minus_queue) != 0 :
                print(-heapq.heappop(minus_queue))
            elif len(plus_queue) != 0 and len(minus_queue) == 0:
                print(heapq.heappop(plus_queue))
            elif len(plus_queue) != 0 and len(minus_queue) != 0:
                plus_val =  heapq.heappop(plus_queue)
                minus_val = -heapq.heappop(minus_queue)

                if abs(plus_val) >= abs(minus_val):
                    print(minus_val)
                    heapq.heappush(plus_queue,plus_val)
                elif abs(plus_val) < abs(minus_val):
                    print(plus_val)
                    heapq.heappush(minus_queue,-minus_val)

        else:
            if command > 0:
                heapq.heappush(plus_queue,command)
            elif command < 0:
                heapq.heappush(minus_queue,-command)

sol()

#sys씁시다...