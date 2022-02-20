# 13023
'''
무슨 문제일까..

아하 여러명의 친구 관계를 제시할테니
A-B-C-D-E 이런 관계가 존재하는지 물어보는 것이구나!


'''
import sys
input = sys.stdin.readline

def dfs(friends,visit,start,depth=1):
    if depth == 5:
        return depth

    max_depth = depth
    visit[start] = 1

    for next in friends[start]:
        if not visit[next]:
            max_depth = max(max_depth,dfs(friends,visit,next,depth+1))

    visit[start] = 0
    return max_depth



def sol():
    N,M = map(int,input().split())
    friends = [[] for _ in range(N)]
    visit = [0] * N

    for _ in range(M):
        s,e = map(int,input().split())
        friends[s].append(e)
        friends[e].append(s)

    for start in range(len(visit)):
        if not visit[start]:
            if(dfs(friends,visit,start)==5):
                print(1)
                return

    print(0)
    return



sol()