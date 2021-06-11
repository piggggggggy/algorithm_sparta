#스파르타 알고리즘 강의 1주차 숙제1번문제
# Q. 정수를 입력 했을 때, 그 정수 이하의 소수를 모두 반환하시오.
# 소수는 자신보다 작은 두 개의 자연수를 곱하여 만들 수 없는 1보다 큰 자연수이다.
input = 20


def find_prime_list_under_number(number):
    # 이 부분을 채워보세요!
    result = []
    for i in range(2,number+1):
        count = 0
        for j in range(2,i+1):
            if i%j == 0:
                count += 1
        if count == 1:
            result.append(i)
    return result


result = find_prime_list_under_number(input)
print(result)