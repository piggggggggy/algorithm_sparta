# 소수 구하기_중하_기본수학2

M, N = map(int, input().split())

prime_list = []
for l in range(2, M):
    for m in range(2,l+1):
        if l%m == 0 and m*m <=l:
            break
        else:
            prime_list.append(l)
for i in range(M, N+1):
    if i > 2:
        for j in prime_list:
            if i%j == 0 and j*j <=i:
                break
        else:
            prime_list.append(i)
            print(i)

    elif i == 2:
        print(i)