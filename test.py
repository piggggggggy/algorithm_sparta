# 스파르타 알고리즘 강의 4주차 DF 문제
# Q. 피보나치 수열의 20번째 수를 구하시오.

input = 20


def fibo_recursion(n):
    # 구현해보세요!
    if n > 2:
        result = fibo_recursion(n-1) + fibo_recursion(n-2)
    else:
        result = 1
    return result


print(fibo_recursion(input))  # 6765