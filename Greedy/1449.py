# 1449 수리공 항승

def sol():
    case, length = map(int,input().split())
    data = list(map(int,input().split()))
    data.sort()

    answer = 0
    cover = 0

    for i in range(case):

        if data[i] <= cover :
            continue
        answer += 1
        cover = data[i] + length - 1

    return answer
print(sol())