#10844

num = int(input())
base = [0,1,1,1,1,1,1,1,1,1]

def solve(arr):
    tmp = [0]*10
    for i in range(10):
        if i == 0 :
             tmp[i+1] += arr[i]

        elif i == 9:
             tmp[i-1] += arr[i]
        else:
            tmp[i-1] += arr[i]
            tmp[i+1] += arr[i]
    return tmp


for i in range(num-1):
    base = solve(base)

print(sum(base)%1000000000)




