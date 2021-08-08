# 나무 재테크 첫 시도 45분 소요

from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__=="__main__":
    N,M,K = map(int,input().split())
    energy = [[5]*N for _ in range(N)]
    A = [list(map(int,input().split())) for  _ in range(N)]
    trees = defaultdict(list)
    dead_trees = defaultdict(list)
    dirs = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]

    for _ in range(M):
        r,c,old = map(int,input().split())
        trees[(r-1,c-1)].append(old)

    k = 0

    while(K>k):
        # 봄 - 나무가 자신의 나이만큼 양분을 먹는다. 고려할 문제는 나무가 매번 어디있는지 찾기는 쫌 그렇단말이지. 그러니 관리를 따로 해주자
        for tr,tc in trees:
            # 나이순 정렬
            trees[(tr,tc)].sort()

            # 나이가 적은 순으로 양분 섭취
            tmp_dead = []
            for idx in range(len(trees[(tr,tc)])):
                # 양분이 있는 경우
                if energy[tr][tc] >= trees[(tr,tc)][idx]:
                    energy[tr][tc] -=trees[(tr,tc)][idx]
                    trees[(tr, tc)][idx] += 1

                #양분이 없는 경우 - 여기가 문제인거 같은데
                else:
                    dead_trees[(tr,tc)].append(trees[(tr,tc)][idx])
                    tmp_dead.append((tr,tc,trees[(tr,tc)][idx]))

            for r,c,old in tmp_dead:
                trees[(r,c)].remove(old)

        # 여름 - 죽은 나무는 양분이 된다
        for tr,tc in dead_trees:
            for old in dead_trees[(tr,tc)]:
                energy[tr][tc] += old //2
            # 초기화
            dead_trees[(tr,tc)] = []


        # 가을 - 나무 번식
        target_land = []
        for tr,tc in trees:
            for tree in trees[(tr,tc)]:
                # 5의 배수이면
                if tree % 5 == 0:
                    for dr,dc in dirs:
                        new_tr , new_tc = tr+dr,tc+dc
                        # 나무의 자리가 적절하면
                        if 0<=new_tr<N and 0<=new_tc <N:
                            # 1짜리 나무 심기
                            target_land.append((new_tr,new_tc))
        for r,c in target_land:
            trees[(r,c)].append(1)

        # 겨울 - A에 있는 만큼 더하기
        for r in range(N):
            for c in range(N):
                energy[r][c] += A[r][c]


        # 1년이 지났습니다
        k+=1
    answer = 0
    for tree in trees:
        answer += len(trees[tree])
    print(answer)

