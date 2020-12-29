# 1158 요세푸스 문제
from collections import deque

people, nth = map(int,input().split())
nth -=1

q = deque()
seq = []


for i in range(1,people+1):
    q.append(i)

while(len(q) > nth):

    for i in range(nth):
        tmp = q.popleft()
        q.append(tmp)
    ele = q.popleft()
    seq.append(str(ele))

    print(seq)
    print(q)
for i in q:
    seq.append(str(i))
result = "<" + ", ".join(seq) + ">"

print(result)

#<3, 6, 2, 7, 1, 4, 5>
#<3, 6, 2, 7, 5, 1, 4>