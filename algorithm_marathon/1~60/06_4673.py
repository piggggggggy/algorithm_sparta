# 셀프넘버_하_함수

def d(a):
    b = str(a)
    c = 0
    for i in b:
        c += int(i)
    return a+c
num = []
nums = range(1,10000)
for i in nums:
    j = d(i)
    if j <10000:
        num.append(j)
num = set(num)
nums = set(nums)
newnums = sorted(nums - num)
for l in newnums:
    print(l)