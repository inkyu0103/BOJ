# 직관적인 풀이

def sol ():
    arr = [0]
    for i in range(1,46):
        arr += [i]*i
    a,b = map(int,input().split())
    print(sum(arr[a:b+1]))
sol()