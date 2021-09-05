# 19939

def sol ():
    N, K = map(int,input().split())
    varN , varK = N,K
    data = []

    for _ in range(K):
        portion = (varN//varK)+1
        if portion in data :
            return -1
        data.append(portion)
        varK -= 1
        varN -= portion

    return data[-1]-data[0]

print(sol())
