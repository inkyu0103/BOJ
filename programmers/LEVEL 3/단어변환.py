from collections import deque

answer = 1
def worddiff(w1, w2):
    count = 0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            count += 1

    if count == 1:
        return True

    return False


def solution(begin, target, words):
    if target not in words:
        return 0
    answer = 1
    words.append(begin)
    words_len = len(words)
    visit = [0] * words_len

    def bfs(start):
        global answer
        q = deque([start])
        visit[start] = 1

        length = 1
        count = 0

        while (q):
            curNode = q.popleft()
            count += 1
            for nextNode in graph[curNode]:
                if words[nextNode] == target:
                    return answer
                elif not visit[nextNode]:
                    q.append(nextNode)
                    visit[nextNode] = 1

            if count == length:
                count = 0
                length = len(q)
                answer += 1

        return answer

    # 단어간 관계 표현 (1글자 차이가 나면 간선이 있는 것으로 표현)
    graph = [[] for _ in range(words_len)]

    for i in range(words_len):
        for j in range(words_len):
            if i != j and worddiff(words[i], words[j]):
                graph[i].append(j)

    return bfs(words_len - 1)
