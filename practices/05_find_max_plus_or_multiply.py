#스파르타 알고리즘 강의 1주차 1번문제
# Q. 다음과 같이 0 혹은 양의 정수로만 이루어진 배열이 있을 때,
# 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에
# '*' 혹은 '+' 연산자를 넣어 결과적으로 가장 큰 수를 구하는 프로그램을 작성하시오.
# 단, '+' 보다 '*' 를 먼저 계산하는 일반적인 방식과는 달리, 모든 연산은
# 왼쪽에서 순서대로 이루어진다.
input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    # 이 부분을 채워보세요!
    _result = array[0]
    for i in range(len(array)-1):
        if _result*array[i+1] > _result+array[i+1]:
            _result *= array[i+1]
        else:
            _result += array[i+1]
    return _result


result = find_max_plus_or_multiply(input)
print(result)