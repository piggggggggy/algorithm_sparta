# 베르트랑 공준_하_기본수학2
prime = []
while True:
    n = int(input())
    if n == 0:
        break
    check = []
    if n == 1:
        check.append(2)
        prime.append(2)
    else:
        for i in range(n+1, n * 2):
            if i in prime:
                check.append(i)
            else:
                count = 0
                for j in range(2, n):
                    if i%j == 0:
                        count +=1
                if count == 1:
                    check.append(i)
                    prime.append(i)
    print(len(check))