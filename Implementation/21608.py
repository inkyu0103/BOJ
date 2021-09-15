#21608 상어 초등학교
import sys
input = sys.stdin.readline

def find_location(target):
    candidate = []

    for r in range(N):
        for c in range(N):
            if not graph[r][c]:
                blank,friends = 0,0
                for dr,dc in dirs:
                    new_r,new_c = r+dr,c+dc
                    if 0<=new_r<N and 0<=new_c<N:
                        # 비어있는 경우
                        if not graph[new_r][new_c]:
                            blank += 1
                        # 친구인 경우 --> 탐색을  전부 다 해야하는게 맘에 안든다. 시간초과 나면 여기를 바꿔보자.
                        elif graph[new_r][new_c] in preference[num]:
                            friends += 1
                candidate.append([friends,blank,[r,c]])

    candidate.sort(key=lambda x:(-x[0],-x[1],x[2][0],x[2][1]))
    new_r,new_c=candidate[0][2]
    graph[new_r][new_c] = target

N = int(input())
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
grade = [0,1,10,100,1000]
graph = [[0]*N for _ in range(N)]
preference  = dict()

# 선호도 기록하기
for _ in range(1,N**2+1):
    num,*prefer =map(int,input().split())
    preference[num] = prefer
    find_location(num)

# 만족도 조사
result = 0
for r in range(N):
    for c in range(N):
        friends = 0
        for dr,dc in dirs:
            new_r,new_c = r+dr,c+dc
            if 0 <= new_r < N and 0 <= new_c < N and graph[new_r][new_c] in preference[graph[r][c]]:
                friends += 1

        result += grade[friends]

print(result)