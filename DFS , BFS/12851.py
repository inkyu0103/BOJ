# 12851 (시작시간 17:36분)

from collections import deque
import sys
input = sys.stdin.readline
INF = sys.maxsize

def bfs(s,e):
    # visit을 활용해야 할 것 같은데
    q = deque([(0,s)])
    dp[s] = 0
    way = 0

    while q:

        cur_time,cur_node = q.popleft()
        if cur_node == e:
            if dp[cur_node] == cur_time:
                way += 1

            elif dp[cur_node] > cur_time:
                way = 1
                dp[cur_node] = cur_time

            continue

        if cur_time <= 100000:
            plus_1 = cur_node+1
            if plus_1 <= e and dp[plus_1] >= cur_time+1:
                dp[plus_1] = cur_time + 1
                q.append((cur_time+1,plus_1))

            minus_1 = cur_node -1
            if minus_1 >= 0 and dp[minus_1] >= cur_time+1:
                dp[minus_1] = cur_time + 1
                q.append((cur_time+1,minus_1))

            twice = cur_node*2
            if cur_node != 0 and twice <= e and dp[twice] >= cur_time+1:
                dp[twice] = cur_time + 1
                q.append((cur_time+1,twice))

    return way


if __name__ =='__main__':
    s,e = map(int,input().split())
    dp = [INF]*100001

    if s==e:
        print(0)
        print(1)

    elif s>e:
        print(e-s)
        print(1)
    else:
        way = bfs(s,e)
        print(dp[e])
        print(way)


