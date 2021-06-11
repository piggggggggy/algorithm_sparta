#스파르타 알고리즘 강의 1주차 2번문제
# Q. 다음과 같이 영어로 되어 있는 문자열이 있을 때,
# 이 문자열에서 반복되지 않는 첫번째 문자를 반환하시오.
# 만약 그런 문자가 없다면 _를 반환하시오

input = "abacabade"

def find_not_repeating_character(string):
    # 이 부분을 채워보세요!
    for i in string:
        result = 0
        if string.count(i) == 1:
            result = i
            break
        else:
            result = '_'
    return result


result = find_not_repeating_character(input)
print(result)