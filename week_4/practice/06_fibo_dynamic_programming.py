# 스파르타 알고리즘 강의 4주차 DF 문제
# Q. 피보나치 수열의 100번째 수를 구하시오.

input = 100

# memo 라는 변수에 Fibo(1)과 Fibo(2) 값을 저장해놨습니다!
memo = {
    1: 1,
    2: 1
}


def fibo_dynamic_programming(n, fibo_memo):
    # 구현해보세요!
    if n in fibo_memo:
        result = fibo_memo[n]
    else:
        fibo_memo[n] = fibo_dynamic_programming(n-1, fibo_memo) + fibo_dynamic_programming(n-2, fibo_memo)
        result = fibo_memo[n]

    return result


print(fibo_dynamic_programming(input, memo))