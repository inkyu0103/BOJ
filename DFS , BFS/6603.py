# 6603
#의존 그래프를 만들면 되지 않을까? 작으면 작을수록 왼쪽에 있어야 하니까 1 2 3 4 5 6 이 있으면
#  3을 먼저 고르면 3 4 ~ 이렇게 나와야 하네 ;그렇구나 애초에 작은 수가 나올 수 없구나
# 그러면 모든 경우의 수는 어떻게 체크를 하지?
# 계속 DFS를 돌려야 하나?
# a<b 이면 f(a) < f(b) 조합

#재귀를 하면 뒤로 돌아가는 특징이 있구나.

def dfs(start, depth):
    if depth == 6:
        for i in range(6):
            print(combi[i], end=' ')
        print()
        return
    for i in range(start, len(s)):
        combi[depth] = s[i]
        dfs(i + 1, depth + 1)

combi = [0 for i in range(13)]
while True:
    s = list(map(int, input().split()))
    if s[0] == 0:
        break
    del s[0]
    dfs(0, 0)
    print()