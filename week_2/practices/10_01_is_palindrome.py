input = "aaasaaa"


def is_palindrome(string):
    # if len(string) <= 1:
    #     return True
    # if string[0] == string[-1]:
    #     _string = string[1:-1]
    #     is_palindrome(_string)
    # return False
    # 틀림 아직 구조이해가 부족한듯

    # 정답
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False
    return is_palindrome(string[1:-1])

print(is_palindrome(input))