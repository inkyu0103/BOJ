# 11729

def hanoi(n,start,end):
    if n==1:
        print(start,end)
        return
    else:
        hanoi(n-1,start,6-start-end)
        print(start,end) # 맨 마지막 아이 옮기기
        hanoi(n-1,6-start-end,end)

n = int(input())
print(2**n-1)
hanoi(n,1,3)
