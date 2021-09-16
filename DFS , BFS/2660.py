# 2660
from collections import deque
import sys
input = sys.stdin.readline
INF = sys.maxsize

def sol():
    def bfs(start):
        # 거리 / 시작 회원 숫자
        dp = [-1] * (people+1)
        #시작 회원의 거리는 0
        dp[start] = 0

        q = deque([[0,start]])

        while q:
            dist,curPeople=q.popleft()

            for nextPeople in graph[curPeople]:
                # 한 번도 방문하지 않은 경우 or 여기서 방문하는 것이 더 가까운 경우
                if dp[nextPeople] == -1 or dp[nextPeople] > dist + 1:
                    dp[nextPeople] = dist + 1
                    q.append([dist+1,nextPeople])

        return [start,max(dp)]

    people = int(input())
    graph = [[] for _ in range(people+1)]

    # 간선 입력
    while True:
        s,e = map(int,input().split())
        if s==-1 and e==-1:
            break
        graph[s].append(e)
        graph[e].append(s)

    #bfs를 시행
    minScore = INF
    answerCandidate = []
    answer = []
    for i in range(1,people+1):
        start,score = bfs(i)
        minScore = min(minScore,score)
        answerCandidate.append([start,score])

    for num,score in answerCandidate:
        if score == minScore:
            answer.append(num)


    print(minScore,len(answer))
    print(*answer)

sol()
