# 3060 욕심쟁이 돼지
import sys
input = sys.stdin.readline
# 맞은편 돼지는 어떻게 구하지?
def calculate_feeding_days (day_limit,need_foods):
    if sum(need_foods) > day_limit : return 1

    count_day = 2

    adj_idx = {
        0:[1,5,3],
        1:[0,2,4],
        2:[1,3,5],
        3:[2,4,0],
        4:[3,5,1],
        5:[0,4,2]
    }

    # copy
    new_foods = [food for food in need_foods]
    tmp_foods = [food for food in need_foods]

    while 1:
        for idx in range(len(new_foods)):
            tmp_foods[idx] += sum([new_foods[other] for other in adj_idx[idx]])

        new_foods = [food for food in tmp_foods]

        if day_limit >= sum(new_foods):
            count_day += 1
            continue

        break

    return count_day



def sol():
    tc = int(input())
    for _ in range(tc):
        day_limit = int(input())
        need_foods = list(map(int,input().split()))

        count_day = calculate_feeding_days(day_limit,need_foods)
        print(count_day)


sol()

