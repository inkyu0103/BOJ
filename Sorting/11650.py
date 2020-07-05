testcase = int(input())

box = []

for i in range(testcase):
    x,y = map(int, input().split())
    box.append([x,y])

box.sort()
for i in range(len(box)):
    for j in range(2):
        print(box[i][j], end=" ")
    print()

