# 1167 DFS

def dfs(start,beforeLength,nextLength):
    global length,maxNode
    visit[start] = 1
    curLength = beforeLength + nextLength

    if length < curLength:
        length = curLength
        maxNode = start

    for nextNode in graph[start]:
        # 방문하지 않은 노드가 있다면
        if not visit[nextNode[0]]:
            dfs(nextNode[0],curLength,nextNode[1])

if __name__ == "__main__":
    V = int(input())
    graph=[[] for _ in range(V+1)]
    visit = [0]*(V+1)
    maxLength = 0
    maxNode = -1
    for _ in range(V):
        length = 0
        data = list(map(int,input().split()))
        idx = 1
        start = data[0]
        while(data[idx] != -1):
            end,wei = data[idx],data[idx+1]
            graph[start].append((end,wei))
            idx += 2
    dfs(1,0,0)
    length = 0
    visit = [0]*(V+1)
    dfs(maxNode,0,0)
    print(length)
