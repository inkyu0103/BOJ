#6593
from collections import deque
import sys
input = sys.stdin.readline

def sol():
    # 방향은 l,r,c / 상,하(바뀌어도 크게 상관 없다), 북, 남 ,동, 서
    dirs = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    def find_loc():
        start = (-1,-1,-1)
        end = (-1,-1,-1)
        for l in range(L):
            for r in range(R):
                for c in range(C):
                    if graph[l][r][c] == 'S':
                        start = (l, r, c)
                    elif graph[l][r][c] =='E':
                        end = (l,r,c)

        return start,end

    def BFS(start):
        sl,sr,sc = start
        # 방문한 곳은 -1로 표시하자
        graph[sl][sr][sc] = '#'
        # 걸린 시간, 시작 위치
        q = deque([[0,sl,sr,sc]])

        while q:
            time,l,r,c = q.popleft()

            for dl,dr,dc in dirs:
                new_l,new_r,new_c =l+dl,r+dr,c+dc

                # 범위에 만족하는 경우 & 빈 공간일 경우 --> 방문한 공간은 더 이상 방문할 필요가 없으므로 벽으로 표시하자.
                if 0<=new_l<L and 0<=new_r<R and 0<=new_c<C:
                    if graph[new_l][new_r][new_c] == 'E':
                        return time + 1
                    elif graph[new_l][new_r][new_c] != '#':
                        q.append([time+1,new_l,new_r,new_c])
                        graph[new_l][new_r][new_c] = "#"
        return -1


    while 1:

        # 테스트케이스 입력받기
        L,R,C = map(int,input().split())

        if L==0 and R==0 and C==0:
            break

        # 빌딩정보 입력받기 (중간에 공백이 존재)
        graph = []
        for l in range(L):
            tmp = []
            for r in range(R):
                tmp.append(list(input().strip()))
            # 공백문자 받기
            input()
            graph.append(tmp)

        # 시작 지점 찾기
        start,end = find_loc()
        result = BFS(start)

        if result != -1:
            print('Escaped in {} minute(s).'.format(result))
        else:
            print('Trapped!')

sol()