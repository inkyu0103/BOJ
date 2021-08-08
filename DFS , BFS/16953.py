# 16953

from collections import deque
import sys
input = sys.stdin.readline

def trans(target):
    return int(str(target)+"1")

A,B = map(int,input().split())
flag = 0
cnt =0
q = deque([(0,A)])
while q:
    count,cur_val = q.popleft()

    if cur_val == B:
        flag = 1
        cnt = count
        break

    plus_1 = trans(cur_val)

    for y in [plus_1,cur_val*2]:
        if y<=B:
            q.append((count + 1,y))


if not flag:
    print(-1)
else:
    print(cnt+1)




