from collections import deque
import sys

def sol():
    case = int(input())

    for i in range(case):
        queue = deque()
        numofDoc , firstIdx = map(int,sys.stdin.readline().split())
        for i in sys.stdin.readline().split():
            queue.append(int(i))

        idx = firstIdx
        count = 0

        # 큐에서 슬라이스 사용
        #      |
        # 미리뽑고 비교
        #      |
        # 빈 큐에서 max 사용
        #      |
        # base case를 따로 만들어야 하나?
        while(1):
            if len(queue) == 1:
                count += 1
                break


            # 내가 보고싶은 아이 위치가 처음일 때
            if idx == 0:
                # 이런 변수명이 나쁜 것 같다. 의식해서라도 바꾸자.
                tmpVal = queue.popleft()
                if max(queue) <= tmpVal:
                    count+=1
                    break
                else:
                    queue.append(tmpVal)
                    idx = len(queue)-1
            else:
                tmpVal = queue.popleft()
                if max(queue) <= tmpVal:
                    count += 1
                else:
                    queue.append(tmpVal)
                idx-=1


        print(count)


sol()
