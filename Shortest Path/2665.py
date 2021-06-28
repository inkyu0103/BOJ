# 2665 이거 몇 개의 벽을 부수고 가야하는가와 동일한 문제인데
'''
0과 1밖에 없는걸로 보아하니 0-1BFS 문제이려나?
근데 문제는 부수는게 달려있는데.
0-1 BFS로 풀면 될 것 같은데?
아하 dp도 같이 사용해야 하는구나.
'''

import sys
from collections import deque
input = sys.stdin.readline


def BFS():
    q = deque([(0,0)])

    graph[0][0] = True

    while(q):
        curR , curC = q.popleft()

        for move in dirs:
            newR,newC = curR + move[0], curC+ move[1]

            if 0<=newR<N and 0<=newC<N and answer[newR][newC] == -1:
                if graph[newR][newC] =='1':
                    q.appendleft((newR,newC))
                    answer[newR][newC] = answer[curR][curC]
                else:
                    q.append((newR,newC))
                    answer[newR][newC] = answer[curR][curC] + 1






if __name__ == '__main__':
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    N = int(input())
    graph = [list(input().strip()) for _ in range(N)]
    answer = [[-1]*N for _ in range(N)]
    answer[0][0] = 0

    BFS()
    print(answer[N-1][N-1])

