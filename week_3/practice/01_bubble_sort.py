#스파르타 알고리즘 강의 1주차 1번문제
# Q. 다음과 같이 숫자로 이루어진 배열이 있을 때,
# 오름차순으로 버블 정렬을 이용해서 정렬하시오.

input = [4, 6, 2, 9, 1,10,7,8,3]


def bubble_sort(array):
    # 이 부분을 채워보세요!

    for j in range(len(array)-1):
        for i in range(len(array)-1 - j):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
    return array

bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!