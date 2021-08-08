# 12851 (시작시간 17:36분)
# 8.4 11시 5분 ~ 11시 35분

from collections import deque
import sys
input = sys.stdin.readline
INF = sys.maxsize

def bfs(s,e):
    # visit을 활용해야 할 것 같은데 --> dp활용

    q = deque([(0,s)])
    dp[s] = 0
    answer = 0

    while q:

        cur_dist,cur_node = q.popleft()

        if cur_node == e:
            if dp[e] == cur_dist:
                answer += 1
            elif dp[e] > cur_dist:
                answer = 1
                dp[e] = cur_dist


        new_dist, new_node = cur_dist + 1, cur_node + 1
        if new_node <=100000 and dp[new_node] > new_dist and new_node<= e :
            q.append((new_dist,new_node))
            dp[new_node] = new_dist

        new_node = cur_node-1
        if dp[new_node] >= new_dist and 0<=new_node<=100000:
            q.append((new_dist,new_node))
            dp[new_node] = new_dist

        new_node = cur_node*2
        if new_node<=100000 and dp[new_node] >= new_dist:
            q.append((new_dist,new_node))
            dp[new_node] = new_dist


    return answer


if __name__ =='__main__':
    s,e = map(int,input().split())
    dp = [INF]*100001

    if s==e:
        print(0)
        print(1)

    elif s>e:
        print(s-e)
        print(1)
    else:
        way = bfs(s,e)
        print(dp[e])
        print(way)




