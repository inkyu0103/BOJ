# 파도반 수열
def find(start):
    if start < 6:
        return memo[start]

    else:
        if start in memo:
            return memo[start]

        else:
            memo[start] = find(start - 1) + find(start - 5)
            return memo[start]


testCase = int(input())
memo = {1:1,2:1,3:1,4:2,5:2}

for _ in range(testCase):
    userInput = int(input())
    print(find(userInput))



