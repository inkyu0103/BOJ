# 13305 주유소

# 자신 도시보다 싼 주유소를 발견하기 전까지는 계속 넘어가자.

city =int(input())
dis = list(map(int,input().split()))
price = list(map(int,input().split()))

payment = dis[0]*price[0]
std = 0
it = 1

while(1):
    try:

        if price[std] <= price[std+it]:
            payment += dis[std+it]*price[std]
            it += 1

        # 더 싼 경우
        else:
            std = std + it
            it = 0

    except :
        break

print(payment)















