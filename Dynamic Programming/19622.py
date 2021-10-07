# 19622
import sys
input = sys.stdin.readline
# 시작시간, 끝나는 시간, 회의 인원
'''
K번재 회의는 K+1번째 회의와만 시간이 겹친다.
초기에 내가 1번 회의를 선택하냐, 2번을 선택하냐에 따라 갈림.
1번 선택 --> 2번 선택 못함.

'''

def sol():
    N = int(input())
    time_info = []
    for _ in range(N):
        time_info.append(list((map(int,input().split()))))

    dp = []



sol()