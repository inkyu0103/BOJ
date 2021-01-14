# 1700 멀티탭 스케줄링

hole, elec = map(int,input().split())
idx = list(map(int,input().split()))
resi = [0]*(elec+1)
concent =[]
full = 0
out = 0
min_resi = 1e20
# O(n)
for i in idx:
    resi[i] += 1

for i in idx:

    # 이미 꽂혀있는지 확인한다. (한번 썼으니 -1 해주기)
    if i in concent:
        resi[i] -= 1
        continue

    # 아직 꽂혀있지 않고, 꽂을 곳이 있다면 꽂는다.
    if full < hole:
        concent.append(i)
        full += 1

    # 꽂을 곳이 없다면 꽂혀있는 아이들 중 남아있는 곳이 가장 작은 곳을 뽑는다.
    else:
        for j in concent:
            if idx[j] < min_resi:
                min_resi = idx[j]

        # concent 내부는 중복될 일 x
        concent.remove(j)
        out += 1
        concent.append(i)

    resi[i] -= 1
    min_resi = 1e20


print(out)




