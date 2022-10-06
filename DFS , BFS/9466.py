# 9466 텀 프로젝트
'''
사이클 여부 판단을 하는게 중요할 거 같은데..?
'''
import sys
input = sys.stdin.readline

def sol():
    tc = int(input())

    for _ in range(tc):
        already_grouped = set()
        N = int(input())
        selected = [0] + (list(map(int, input().split())))

        for i in range(1,N+1):
            if selected[i] == i:
                already_grouped.add(i)

        for i in range(1,N+1):
            temp_visited = set()
            next_node = selected[i]

            # 자기 자신이 이미 소속된 아이라면 검사를 진행할 필요 없음
            if i in already_grouped:
                continue

            while 1:
                # 다음 타겟이 자기 자신인 경우 (2가지로 나뉨)
                # 1. 자기가 자기를 선택한 경우
                # 2. 자신을 포함한 사이클이 생기는 경우
                if next_node == i:
                    temp_visited.add(i+1)
                    already_grouped = already_grouped.union(temp_visited)
                    break

                # 다음 타겟이 자기가 아닌 경우
                # 1. 다음 타겟이 이미 temp_visited 에 포함된 경우 (곧바로 종료)
                # 2. 그렇지 않은 경우 (next_node 갱신 + temp_visited에 넣기)
                if next_node not in temp_visited and next_node not in already_grouped:
                    temp_visited.add(next_node)
                    next_node = selected[next_node]
                else:
                    break

        print(N-len(already_grouped))
sol()
