# Q. 다음과 같이 숫자로 이루어진 배열이 있을 때,
# 2가 존재한다면 True 존재하지 않는다면 False 를 반환하시오.

finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

def is_exist_target_number_binary(target, numbers):
    # 이 부분을 채워보세요!
    numbers.sort()
    mid = len(numbers) // 2
    while mid != 0:
        if target == numbers[mid]:
            return True
        if target > numbers[mid]:
            numbers = numbers[mid+1:]
        else:
            numbers = numbers[:mid]
        mid = len(numbers) //2
    return False
###### 틀림

result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)
