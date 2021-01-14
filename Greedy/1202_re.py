# 보석도둑 re

import sys
import heapq

jem,bag = map(int,sys.stdin.readline().split())
jem_info =[]
answer  = 0
for i in range(jem):
    weight, value = map(int,sys.stdin.readline().split())
    heapq.heappush(jem_info,(-value,weight))
bag_info = []
for i in range(bag):
    value = int(sys.stdin.readline())
    bag_info.append(value)

bag_info.sort()

#가방을 기준으로돌 필요가 있을까
for i in range(bag):
    endure = bag_info[i]

    '''while(1):
        value, weight = heapq.heappop(jem_info)

        if endure >= weight :
            answer += -value
            break

        else:
            heapq.heappush(jem_info, (-value, weight))
            continue
            
    '''

    # 보석 정보가 남아있고, 무게를 견딜 수 있는 경우에는 뽑는다.
    while jem_info and endure >= jem_info[0][1]:
        value, weight = heapq.heappop(jem_info)





print(answer)






