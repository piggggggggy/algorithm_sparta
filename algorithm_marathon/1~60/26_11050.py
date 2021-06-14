# 이항계수1_하_정수론 및 조합론
import sys

N, K = map(int, sys.stdin.readline().split())

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

if K <= N and K >= 0 :
    print(int(factorial(N)/(factorial(K)*factorial(N-K))))
elif K < 0:
    print(0)
elif K > N:
    print(0)

