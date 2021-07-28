# 5014 시작시간 1시 55분 / 코딩 시작 2:11 ( 생각 16분 ) / 첫 제출  2:29 (83% 오답) (34분) / 2차 제출(2:34) (83% 오답) / 3차 제출 (성공) 자잘자잘한 ...오류....

from collections import deque
import sys
input = sys.stdin.readline

# F: 총 층 , S : 현재 있는 층,  G: 목표층 , U : 위로 u칸 , D : 아래로 D칸
# 도착할 수 없으면 use the stairs
# 버튼을 몇 번 눌러야 합니까?
# 사실상 움직이는 값이 2개라서 0-1 이걸로 해도 될 거 같은데. 꼭 그렇지는 않네. 0-1은 우선순위 개념이 껴있을 때 사용하면 ㄱㅊ


def bfs(F,S,G,U,D):
    visit = [0]*(F+1)
    visit[S] = 1
    q = deque([S])
    push = 0
    length = 1
    count = 0

    while q:
        cur_s = q.popleft()
        if cur_s == G :
            return push

        count += 1

        up_s = cur_s + U
        down_s = cur_s - D


        # 자신보다 상층이고, 아직 방문하지 않은경우
        if up_s <= F and not visit[up_s]:
            visit[up_s] = 1
            q.append(up_s)
        # 자신보다 하층이고, 아직 방문하지 않은경우
        if 1 <= down_s and not visit[down_s]:
            visit[down_s] = 1
            q.append(down_s)

        if count == length:
            length = len(q)
            count = 0
            push += 1

    # 다 돌았는데 도달 못하는 경우
    return "use the stairs"

def sol():
    F,S,G,U,D = map(int,input().split())

    # F < G 인 경우
    if F < G :
        print('use the stairs')
        return

    # 목표층이 자신보다 높은데, U은 0인경우
    if S < G and U == 0:
        print('use the stairs')
        return

    # 위와 반대의 경우
    if S > G and D == 0:
        print('use the stairs')
        return

    #이미 도착해 있는 경우
    if S == G :
        print(0)
        return

    print(bfs(F,S,G,U,D))
sol()
