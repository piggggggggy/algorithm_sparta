#스파르타 알고리즘 강의 1주차 2번문제
# Q. 다음과 같이 숫자로 이루어진 배열이 있을 때,
# 오름차순으로 선택 정렬을 이용해서 정렬하시오.


input = [4, 6, 2, 9, 1]


def selection_sort(array):
    # 이 부분을 채워보세요!
    for i in range(len(array)-1):
        if array[i] > min(array[i:]):
            n = array.index(min(array[i:]))
            array[i], array[n] = array[n], array[i]
    return


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!