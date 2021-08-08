# 기타레슨

import sys
input = sys.stdin.readline

def sol():
    N,M = map(int,input().split())
    arr = list(map(int,input().split()))
    l,r = 1, N *10000

    answer = sys.maxsize

    while l<=r :
        # mid는 블루레이의 크기 중 최소
        mid = (l+r)//2
        acc = 0
        cnt = 0

        for i in range(len(arr)):
            if acc + arr[i] > mid:
                cnt += 1
                acc = 0

            acc += arr[i]



        # 어라 블루레이 개수가 적어도 되는구나, 그러면 블루레이 시간을 줄이자.
        if cnt  < M :
            r = mid -1

        # 오호 더 크네? 그럼 블루레이 시간을 늘려도 되겠네
        else:
            l = mid + 1
            answer = min(answer,)

    print(answer)

sol()