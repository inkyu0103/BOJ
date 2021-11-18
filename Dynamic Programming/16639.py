# 16639
import sys
input = sys.stdin.readline

def sol():
    def calculate(depth, targets):
        if depth == 3 or len(targets) == 1:
            return targets
        result = []
        for target in targets.split(operator[depth]):
            result.append(calculate(depth + 1, target))
        return str(eval(operator[depth].join(result)))

    N = int(input())
    expression = input().rstrip()
    operators = [["+","-","*"],["+","*","-"],["-","*","+"],["-","+","*"],["*","-","+"],["*","+","-"]]
    result = []

    for operator in operators:
        result.append(calculate(0,expression))

    print(result)
sol()