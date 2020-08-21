#2565 전깃줄
import sys
import bisect
num = int(input())
box=[]
emptyBox =[]
dp  = [0]*num

for _ in range(num):
    start,end =map(int,sys.stdin.readline().split())
    box.append((start,end))
box.sort()
emptyBox.append(box[0][1])
for i in range(1,num):
    if emptyBox[len(emptyBox)-1] < box[i][1]:
        emptyBox.append(box[i][1])

    elif emptyBox[len(emptyBox)-1] > box[i][1]:
        idxval = bisect.bisect_left(emptyBox,box[i][1],0,len(emptyBox))
        emptyBox[idxval] = box[i][1]

print(num-len(emptyBox))








