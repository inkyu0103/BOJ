# 1707 이분그래프
import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    q = deque()
    q.append(start)
    visit[start] = 1

    while(q):
        node = q.popleft()
        for nextNode in graph[node]:
            if visit[nextNode] == 0:
                visit[nextNode] = -1*visit[node]
                q.append(nextNode)
            else:
                # 같은 색으로 칠해진 경우
                if visit[nextNode] == visit[node]:
                    return 0
                # 아닌경우는 그냥 넘어가도 되는걸까?
    return 1

if __name__=="__main__":
    tc = int(input())
    for _ in range(tc):
        V, E = map(int, input().split())
        graph = [[] for x in range(V)]
        visit = [0] * V

        for e in range(E):
            s, e = map(int, input().split())
            s, e = s - 1, e - 1

            graph[s].append(e)
            graph[e].append(s)

        flag = 0
        for i in range(len(visit)):
            if visit[i] == 0 :
                if not bfs(i):
                    flag = 1
                    print("NO")
                    break

        if flag == 0:
            print("YES")
