# 통계학_중_정렬

import sys

n = int(sys.stdin.readline())
data = [int(sys.stdin.readline()) for i in range(n)]



def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left_array = merge_sort(array[:mid])
    right_array = merge_sort(array[mid:])
    return merge(left_array, right_array)

def merge(array1, array2):
    result = []
    array1_index = 0
    array2_index = 0
    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] < array2[array2_index]:
            result.append(array1[array1_index])
            array1_index += 1
        else:
            result.append(array2[array2_index])
            array2_index += 1
    if array1_index == len(array1):
        while array2_index < len(array2):
            result.append(array2[array2_index])
            array2_index += 1
    if array2_index == len(array2):
        while array1_index < len(array1):
            result.append(array1[array1_index])
            array1_index += 1
    return result

sorted_array = merge_sort(data)

avg = round(sum(sorted_array)/n)
mid_num = sorted_array[n//2]
rng = sorted_array[-1]-sorted_array[0]

set_list = list(set(sorted_array))
set_list.sort()
m = len(set_list)
check_list = [0] * m
max_num = 0
fqc = 0

for i in range(m):
    a = sorted_array.count(set_list[i])
    if a > max_num:
        max_num = a
    check_list[i] = a


if check_list.count(max_num) == 1:
    fqc = set_list[check_list.index(max_num)]
else:
    count = 0
    for i in range(m):
        if max_num == check_list[i]:
            count += 1
        if count == 2:
            fqc = set_list[i]
            break


print(avg)
print(mid_num)
print(fqc)
print(rng)

########## 시간초과 시발


# def merge_sort(array):
#     mid = len(array)//2
#     if mid <= 1:
#         return array
#     left_array = merge_sort(array[:mid])
#     right_array = merge_sort(array[mid:])
#     return merge(left_array, right_array)
#
# def merge(array1, array2):
#     sorted_list = []
#     array_idx1 = 0
#     array_idx2 = 0
#     while array_idx1 < len(array1) and array_idx2 < len(array2):
#         if array1[array_idx1] < array2[array_idx2]:
#             sorted_list.append(array1[array_idx1])
#             array_idx1 += 1
#         else:
#             sorted_list.append((array2[array_idx2]))
#             array_idx2 += 1
#
#     if len(array1) == array_idx1:
#         while array_idx2 < len(array2):
#             sorted_list.append(array2[array_idx2])
#             array_idx2 += 1
#     if len(array2) == array_idx2:
#         while array_idx1 < len(array1):
#             sorted_list.append(array1[array_idx1])
#             array_idx1 += 1
#     return sorted_list