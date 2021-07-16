# 숨바꼭질 3
import sys
from collections import deque

INF = sys.maxsize
input = sys.stdin.readline


'''
    N<K
    N==K
    N>K 이렇게 3가지로 나뉠듯
    0,1 BFS?
'''

def BFS(start,K):
    q = deque([(0,start)])
    while(q):
        cur_time,cur_node=q.popleft()

        if cur_node <= 100000:
            # 1. 걷는 경우
            plus_1 = cur_node + 1
            if plus_1 <= K and dp[plus_1] > cur_time + 1:
                dp[plus_1] = cur_time+1
                q.append((cur_time+1,plus_1))

            minus_1 = cur_node-1
            if minus_1 >=0 and dp[minus_1] > cur_time + 1:
                dp[minus_1] = cur_time+1
                q.append((cur_time+1,minus_1))

            twice = cur_node*2
            if cur_node != 0 and  twice <= 100000 and dp[twice] > cur_time:
                dp[twice] = cur_time
                q.appendleft((cur_time,twice))

    return

if __name__ == '__main__':
    N,K = map(int,input().split())
    dp = [INF]*100001
    if N == K:
        print(0)
    elif N > K:
        print(N-K)
    else:
        BFS(N,K)
        print(dp[K])




