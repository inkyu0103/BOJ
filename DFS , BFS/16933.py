# 16933 벽 부수고 이동하기 3
import sys
from collections import deque

input = sys.stdin.readline

"""
0 : 이동 가능
1 : 이동 불가
시작하는 칸, 끝나는 칸 포함해서 최단 경로
이동하지 않고 같은 칸에 머물러 있는 경우도 가능 ( 한 칸으로 친다 )
낮과 밤
한 번 움직일 때마다 낮과 밤이 바뀜
벽을 부수는 건 낮만 가능
벽을 부수면 그 자리에 머물러 있는건가 싶다.
"""

N, M, K = map(int, input().split())
graph = [list(map(int, list(input().rstrip()))) for _ in range(N)]

# 낮과 밤을 나타내는 변수
isDay = True
