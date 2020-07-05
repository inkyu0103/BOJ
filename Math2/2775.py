#부녀회장이 될 거야
test_case = int(input())
# k층 n호
k = int(input())
n = int(input())

#k층 까지 도달
#0층
box = [0]*n
zero_floor = list(range(1,n+1))

print(zero_floor)
#1층을 만들려면
for i in range(0,n):
    if i==0:
        box[0] =1;

    else:
        box[i] += sum(zero_floor[:i])
print(box)


