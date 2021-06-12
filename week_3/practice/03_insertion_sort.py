#스파르타 알고리즘 강의 1주차 3번문제
# Q. 다음과 같이 숫자로 이루어진 배열이 있을 때,
# 오름차순으로 삽입 정렬을 이용해서 정렬하시오.

input = [4, 6, 2, 9, 1,5,7,17,20]


def insertion_sort(array):
    # 이 부분을 채워보세요!
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                array[j-1], array[j] = array[j], array[j-1]
            else:
                break
    return array


insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!