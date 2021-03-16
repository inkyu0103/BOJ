# K번째 수

def sol():
    N = int(input())
    K = int(input())

    start,end = 1,K
    answer = 0
    while start<=end:
        mid = (start+end)//2
        tmp = 0
        for i in range(1,N+1):
            tmp += min(mid//i,N)

        if tmp>=K:
            answer = mid
            end =mid-1
        else:
            start = mid+1
    print(answer)

sol()