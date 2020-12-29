# 2217 로프
import sys
case = int(sys.stdin.readline())
box = [int(sys.stdin.readline()) for i in range(case)]
box.sort()

length = len(box)
max_weight = 0

for i in range(length):
    # 자신의 무게 * 자신부터 뒤에 있는 무게
    endure_weight = box[i]*(length-i)
    #print(endure_weight)

    if endure_weight > max_weight:
        max_weight = endure_weight

print(max_weight)