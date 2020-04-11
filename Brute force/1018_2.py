def check(data):
    # B가 0,0
    count_1 = 0
    for row in range(8):
        for col in range(8):
            row_ = (0 if row in [0,2,4,6] else 1)
            col_ = (0 if col in [0,2,4,6] else 1)

            # row_ == col_ 로 비교하면 빠지는게 있을까?
            if (row_ == 0 and col_ == 0) or (row_ == 1 and col_ == 1):
                if data[row][col] != "B":
                    count_1 += 1
            if (row_ == 1 and col_ == 0) or (row_ == 0 and col_ == 1):
                if data[row][col] != "W":
                    count_1 += 1

    # W가 0,0
    count_2 = 0
    for row in range(8):
        for col in range(8):
            row_ = (0 if row in [0,2,4,6] else 1)
            col_ = (0 if col in [0,2,4,6] else 1)
            # row_ == col_ 로 비교하면 빠지는게 있을까?
            if (row_ == 0 and col_ == 0) or (row_ == 1 and col_ == 1):
                if data[row][col] != "W":
                    count_2 += 1
            if (row_ == 1 and col_ == 0) or (row_ == 0 and col_ == 1):
                if data[row][col] != "B":
                    count_2 += 1

    return min(count_1,count_2)



r , c = map(int, input().split())
box = []
#Data input
data = [list(input()) for i in range(r)]

for i in range(r-7):
    for j in range(c-7):
        data_ = [z[j:j+8] for z in data[i:i+8]]
        box.append(check(data_))

print(min(box))



