# 2847

case = int(input())
data = []
std = 0
answer =0
for i in range(case):
    data.append(int(input()))

for i in range(1,len(data)):
    if data[i] <= data[i-1]:
        std = i

for i in range(std-1,-1,-1):

    if data[i] >= data[i+1]:
        answer += data[i]+1-data[i+1]
        data[i] = data[i+1]-1


print(answer)
