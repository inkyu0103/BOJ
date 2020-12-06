# 5585 거스름 돈

cost = int(input())

resi = 1000-cost
answer = 0

for i in [500,100,50,10,5,1]:
    a = resi//i
    resi -= i*a

    answer += a

print(answer)




