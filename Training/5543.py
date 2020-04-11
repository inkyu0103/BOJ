#5543 상근 날드

food = []
bev =[]
result = 0
for i in range(5):
    if i<3:
        u = int(input())
        food.append(u)
    else:
        u = int(input())
        bev.append(u)

result  = min(food) + min(bev)

print(result-50)