import sys
input = sys.stdin.readline
INF = sys.stdin.readline

def sol():
    def dfs(depth,before):
        if len(numbers) > N:
            return

        if depth == d:
            value = int("".join(result))

            if value in numbers:
                pass
            else:
                numbers.add(value)

            return

        for target in range(10):
            if not visit[target] and target <= before:
                visit[target] = 1
                result.append(str(target))
                dfs(depth+1,target)
                visit[target] = 0
                result.pop()


    N = int(input())
    if N > 1022:
        print(-1)
        return
    
    result = []
    numbers = set()
    visit = [0] * 10

    for d in range(1,10**9):
        for i in range(10):
            dfs(0,i)

        if len(numbers) > N:
            break

    numbers = list(numbers)
    numbers.sort()

    print(numbers[N])
sol()