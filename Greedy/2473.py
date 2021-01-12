# 2437 저울

'''
측정할 수 없는 양의 정수 무게중 최솟값을 구하는 프로그램
어떻게 구해야할까?
아.. 가장 작은 수를 구해야하니까 순서대로 더해야줘야하는구나.
'''

num = int(input())
weight_box = list(map(int,input().split()))
weight_box.sort()
ans = 1

for i in range(len(weight_box)):
    if ans < weight_box[i]:
        break
    ans += weight_box[i]

print(ans)








