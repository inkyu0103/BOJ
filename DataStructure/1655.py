# 1655 아이디어
import heapq
import sys
input = sys.stdin.readline

def sol():
    left,right = [], []
    N = int(input())

    for _ in range(N):
        num = int(input())
        l_length,r_length = len(left),len(right)

        # 길이가 같은 경우
        if l_length == r_length:
            heapq.heappush(left,-num)

        else:
            heapq.heappush(right,num)

        if right and -left[0] > right[0]:
            l_val = -heapq.heappop(left)
            r_val = heapq.heappop(right)

            heapq.heappush(left,-r_val)
            heapq.heappush(right,l_val)

        print(-left[0])


sol()