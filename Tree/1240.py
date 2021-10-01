# 1240
from collections import defaultdict,deque
import sys
input = sys.stdin.readline

def sol():
    N,M = map(int,input().split())


    def bfs(start,end):
        visit = [0] * (N + 1)
        visit[start] = 1
        q = deque()
        q.append([0,start])


        while q:
            cur_dist,cur_node = q.popleft()
            for dist,next_node in tree[cur_node]:
                if not visit[next_node]:
                    if next_node == end:
                        return cur_dist+dist

                    visit[next_node] = 1
                    q.append([cur_dist+dist,next_node])


    def dfs(start,end,dist):
        if start == end :
            return dist

        visit_dfs[start] = 1

        for next_dist,next_node in tree[start]:
            if not visit_dfs[next_node]:
                val = dfs(next_node,end,dist+next_dist)
                if val:
                    return val




    tree = defaultdict(list)

    for _ in range(N-1):
        s,e,dist = map(int,input().split())

        tree[s].append([dist,e])
        tree[e].append([dist,s])

    for _ in range(M):
        visit_dfs = [0] * (N + 1)
        s,e = map(int,input().split())
        #print(bfs(s,e))
        print(dfs(s,e,0))

sol()
