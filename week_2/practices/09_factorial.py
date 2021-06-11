def factorial(n):
    # 이 부분을 채워보세요!
    if n == 1:
        return 1
    result = n * factorial(n-1)

    return result


print(factorial(5))