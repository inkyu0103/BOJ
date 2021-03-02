# 1476
# (1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19)

def sol():
    E,S,M = map(int,input().split())

    year = 1
    e,s,m = 1,1,1

    while(1):
        if (e,s,m) == (E,S,M):
            break

        # 나머지로 하면 0이 되는경우가 있구나.
        e+=1;s+=1;m+=1;
        if e >15:
            e = 1
        if s > 28:
            s = 1
        if m > 19:
            m = 1
        year += 1

    print(year)
sol()
