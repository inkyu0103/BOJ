# 강의실 배정

import sys

case = int(input())
data = [list(map(int,sys.stdin.readline().split())) for i in range(case)]
box = []
data.sort(key=lambda x:(x[1],x[0]))
box.append([data[0]])
print(data)
for i in range(1,(len(data))):
    for j in range(len(box)):
        if data[i][0] == box[j][-1][1]:
            # 정렬을 했기 떄문에 이게 가능
            box[j].append(data[i])
            break

        elif data[i][0] > box[j][-1][1]:
            # 정렬을 했기 떄문에 이게 가능
            box[j].append(data[i])
            break

        else:
            box.append([data[i]])
            break
print(box)
print(len(box))


