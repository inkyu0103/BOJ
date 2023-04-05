from itertools import product


def solution(n, info):
    info.reverse()
    ans = [-1]
    maxd = 0
    for wl in product((True, False), repeat=11):
        s = sum(info[i] + 1 for i in range(11) if wl[i])
        # 사용한 화살 개수가 적은 경우
        if s <= n:
            apeach = sum(i for i in range(11) if not wl[i] and info[i])
            ryan = sum(i for i in range(11) if wl[i])
            print(apeach, ryan)
            d = ryan - apeach
            if d > maxd:
                maxd = d
                ans = [info[i] + 1 if wl[i] else 0 for i in range(11)]
                print(ans)
                # 남은 화살은 어차피 0에다 꽂아버리기? -> 여러 경우인 경우, 가장 낮은 점수로 꽂으래
                ans[0] += n - s
    ans.reverse()
    return ans


solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0])
