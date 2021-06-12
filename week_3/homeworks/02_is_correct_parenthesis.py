# 스파르타 알고리즘 강의 3주차 숙제2번문제
# Q. 괄호가 바르게 짝지어졌다는 것은
# '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻이다.
# 예를 들어
# ()() 또는 (())() 는 올바르다.
# )()( 또는 (()( 는 올바르지 않다.
#
# 이 때, '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때,
# 문자열 s가 올바른 괄호이면 True 를 반환하고 아니라면 False 를 반환하시오.

s = "(()))(()"


def is_correct_parenthesis(string):
    # 구현해보세요!
    if string[-1] =='(':
        return False
    count = 0
    for i in string:
        if i == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            return False
    if count == 0:
        return True

print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!