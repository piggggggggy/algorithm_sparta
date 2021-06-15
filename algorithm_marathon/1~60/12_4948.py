# 베르트랑 공준_하_기본수학2

import sys

n = 123456 * 2 + 1

prime_nums = [True] * n
m = int(n ** 0.5)
for i in range(2, m+1):
    if prime_nums[i]:
        for j in range(i+i, n, i):
            prime_nums[j] = False



while True:
    check_num = int(sys.stdin.readline())
    if check_num == 0:
        break
    print(len([i for i in range(check_num+1, check_num * 2 + 1) if prime_nums[i] == True]))


# 소수를 다루는 법과 (에라토스테네스의 체) 식을 간소화, 시간복잡도를 줄이는 법을 생각하자!



#
# while True:
#     n = int(input())
#     if n == 0:
#         break
#     check = []
#     if n == 1:
#         check.append(2)
#         prime.append(2)
#     else:
#         for i in range(n+1, n * 2):
#             if i in prime:
#                 check.append(i)
#             else:
#                 count = 0
#                 for j in range(2, n):
#                     if i%j == 0:
#                         count +=1
#                 if count == 1:
#                     check.append(i)
#                     prime.append(i)
#     print(len(check))