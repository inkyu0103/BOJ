from itertools import combinations

problem = [*input().strip()]
p, idx_brs = [],[]

for i,v in enumerate(problem):
    if v == '(': problem[i] = '';p += [i]
    if v == ')': problem[i] = '';idx_brs += [[p.pop(), i]]

out = set()

for i in range(len(idx_brs)):
    for j in combinations(idx_brs,i):
        P = problem[:]

        for v, w in j:
            P[v] = '('
            P[w] = ')'
        out.add(''.join(P))

for i in sorted(out):
    print(i)

