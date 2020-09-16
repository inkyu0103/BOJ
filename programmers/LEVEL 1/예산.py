def solution(d, budget):
    # 최대로 많은 부서에 지원 해주자.
    sorting = sorted(d)
    money = 0
    answer = 0

    for i in sorting:
        money += i
        answer += 1

        if money > budget:
            money -= i
            answer -= 1
            break

    return answer