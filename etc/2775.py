
testCase = int(input())
# k 층 n 호

for t in range(testCase):

    k = int(input())
    n = int(input())

    Lower = [x for x in range(1,n+1)]  #[1,2,3,4, ... , n]
    tmp = [0 for y in range(1,n+1)]

    for f in range(k):
        for x in range(n):
            tmp[x] = sum(Lower[:x+1])

        Lower = list(tmp)
        tmp = [0 for y in range(1,n+1)]

    print(Lower[n-1])


