# 11866
from collections import deque

def sol ():
    answer =[]
    N,K = map(int,input().split())
    k=1
    # 큐에 곧바로 복사하는 편이 나을까? or 배열로 만들고 포인터로 하는게 좋을까?
    q = deque()
    for i in range(1,N+1):
        q.append(str(i))

    while(q):
        if k==K:
            answer.append(q.popleft())
            k = 1
        else:
            q.append(q.popleft())
            k+=1
    print("<"+", ".join(answer)+">")

sol()

