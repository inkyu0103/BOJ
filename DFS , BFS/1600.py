from collections import deque
import sys
input = sys.stdin.readline

# 1차시도 틀림
# 2차시도에서 고친 것 : 붙여넣기 하다가 틀린것 (k-1부분)
# 3차 시도에서 고친 것 : dirs1+dirs2 부분에서 대각으로 뛰지 않은 경우에는 k의 횟수가 줄어들면 안된다.
# 그렇다면, k가 존재하면, 무조건 대각으로만 뛰어야 하는가? 그건 아닌 것 같다.
# 따라서. k가 존재하면, 두 방식 모두 하고, 그렇지 않으면 한 방식만 하자.
# 아, 그 발견하자마자 해야한다. 엥 아니네.
# 흠... visit을 2차원으로 둔다면...? 엥 아니네 ㅋ;
# 어라 1 1인 케이스를 안 찾았네
# 음...... 그

def sol():
    K = int(input())
    # w = col , h = row
    W,H = map(int,input().split())
    graph = [list(map(int,input().split())) for _ in range(H)]
    dirs1 = [(0,1),(0,-1),(1,0),(-1,0)]
    dirs2 = [(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]

    if W==1 and H==1:
        print(0)
        return

    def bfs(K):
        visit =[[0]*W for _ in range(H)]

        q = deque()
        # time,K,r,c
        # 하나의 칸에 2개의 방식이 존재하는 경우가 있을텐데...
        visit[0][0] = 1
        q.append([0,K,0,0])

        while q:

            time,k,r,c=q.popleft()

            # 아직 대각선으로 뛸 기회가 있는 경우
            if k:
                for dr,dc in dirs2:
                    new_r,new_c = r+dr,c+dc

                    if (new_r, new_c) == (H - 1, W - 1):
                        return time + 1

                    if 0<=new_r<H and 0<=new_c<W and not graph[new_r][new_c] and not visit[new_r][new_c] <k-1:
                        q.append([time+1,k-1,new_r,new_c])
                        visit[new_r][new_c] += 1

            for dr, dc in dirs1:
                new_r, new_c = r + dr, c + dc
                if (new_r,new_c) == (H-1,W-1):
                    return time+1
                if 0 <= new_r < H and 0 <= new_c < W and not graph[new_r][new_c] and visit[new_r][new_c] < k:
                    q.append([time + 1, k, new_r, new_c])
                    visit[new_r][new_c] += 1
        return -1

    result = bfs(K)
    print(result)
sol()
