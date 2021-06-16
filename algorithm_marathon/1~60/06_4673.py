# 셀프넘버_하_함수

def d(a):
    b = str(a)
    for i in b:
        a += int(i)
    return a

not_self_nums = []
nums = range(1,10000)
for i in nums:
    not_self_num = d(i)
    if not_self_num <10000:
        not_self_nums.append(not_self_num)

_not_self_nums = set(not_self_nums)
_nums = set(nums)
self_nums = sorted(_nums - _not_self_nums)
for l in self_nums:
    print(l)

# a = set(range(1, 10001))
# b = set()
# for x in range(1, 10001):
#     for y in str(x):
#         x += int(y)
#     b.add(x)
#
# selfNums = sorted(a - b)
# for selfNum in selfNums:
#     print(selfNum)