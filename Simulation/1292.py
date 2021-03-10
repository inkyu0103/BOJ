# 1292 쉽게 푸는 문제

def sol():
    a,b = map(int,input().split())
    a_val, b_val = 0,0
    answer = 0
    for n in range(45):
        if n*(n+1)//2 >= a:
            a_val = n

            break

    for n in range(45):
        if n*(n+1)//2 >= b:
            b_val = n
            break

    for i in range(a_val+1,b_val):
        answer +=  i ** 2
    answer += (a_val*(a_val+1)//2-a+1)*a_val + (b-(b_val*(b_val+1)//2-b_val+1)+1)*b_val
    print(answer)
sol()
