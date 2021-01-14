#1700 재도전

# 1700 멀티탭 스케줄링

hole, elec = map(int,input().split())
use_info = list(map(int,input().split()))
concent = []
full = 0
last_use = 0
out = 0
out_value = 0

for i in range(len(use_info)):

    # 이미 꽂혀있는 경우 넘어감
    if use_info[i] in concent :
        continue

    # 공간이 있는 경우
    if full < hole:
        concent.append(use_info[i])
        full +=1

    # 공간이 없는 경우
    else:
        for c in range(len(concent)):
            # 안 사용하는 아이가 있으면 이걸로 끝
            if concent[c] not in use_info[i:]: # i+1도 상관 없을듯
                out_value = concent[c]
                break

            else:
                if use_info[i:].index(concent[c]) > last_use:
                    last_use = use_info[i:].index(concent[c])
                    out_value = use_info[i:][last_use]

        concent.remove(out_value)
        out += 1
        concent.append(use_info[i])

        last_use = 0
        out_value = 0
       # 어짜피 뺏다 끼니까 full은 변하지 않음



print(out)



