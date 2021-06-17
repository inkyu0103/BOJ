from collections import deque


def solution(n, computers):
    visit = [0] * n

    def bfs(start):
        q = deque([start])
        visit[start] = 1

        while (q):
            curNode = q.popleft()
            for idx in range(len(computers[curNode])):
                if computers[curNode][idx] and not visit[idx]:
                    q.append(idx)
                    visit[idx] = 1

    answer = 0

    for i in range(n):
        if not visit[i]:
            bfs(i)
            answer += 1

    return answer