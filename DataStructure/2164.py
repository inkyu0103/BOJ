# 2164 카드
from collections import deque
def sol():
    N = int(input())
    q = deque([i for i in range(1,N+1)])
    while(len(q)!=1):
        q.popleft()
        q.rotate(-1)


    print(q[0])
sol()