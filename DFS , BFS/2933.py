#2933 미네랄.

import sys
input = sys.stdin.readline

def sol():
    R,C = map(int,input().split())
    _map = [list(input().rstrip()) for _ in range(R)]
    N = int(input())

    # 실제 접근하는 idx로 변경
    H = list(map(lambda x:R-int(x),input().split()))
    print(H)

    for i in _map:print(i)
    print('---------------------')

    for idx,h in enumerate(H):
        # 홀수인 경우 - 오른쪽 부터 시작
        if not idx%2:
            for c in range(C-1,-1,-1):
                if _map[h][c] == "x":
                    _map[h][c] = '.'
                    break

        # 짝수인 경우 - 왼쪽 부터 시작
        else:
            for c in range(C):
                if _map[h][c] == 'x':
                    _map[h][c] = '.'
                    break

    for i in _map:print(i)







sol()

'''
1. 왼쪽 플레이어, 오른쪽 플레이어 구분 - idx 짝홀수
'''