#1202 보석도둑
import sys
import heapq
# N :보석의 개수, K : 가방의 개수

# 한 가방에 하나 밖에 담지 못하니까 최대한 비싼 걸 담아야 한다.

ruby_info = []
bag_wei = []
N , K = map(int,sys.stdin.readline().split())

# 보석 정보 담기
for i in range(N):
    wei,val = map(int,sys.stdin.readline().split())
    heapq.heappush(ruby_info,(wei,val))


# 가방 무게 정보
for i in range(K):
    bw = int(sys.stdin.readline())
    bag_wei.append(bw)

bag_wei.sort()
c=0
p=[]

for i in range(K):
    capacity = bag_wei[i]

    while ruby_info and capacity >= ruby_info[0][0]:
        m,v =heapq.heappop(ruby_info)
        heapq.heappush(p,-v)


    if p:
        c -= heapq.heappop(p)
    elif not ruby_info:
        break

print(c)



