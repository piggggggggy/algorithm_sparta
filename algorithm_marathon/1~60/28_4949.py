# 균형잡힌세상_중_스택

# import sys
# dd = sys.stdin.readline().strip()

data = []
while True:
    dd = input()
    if dd == '.':
        break
    data.append(dd)

for j in data:
    check_list = []
    count = 0
    for k in j:
        if k =='(':
            check_list.append('(')
            count += 1
        elif k == '[':
            check_list.append('[')
            count += 1
        elif k == ')':
            if len(check_list) > 0:
                if check_list.pop() != '[':
                    count += 1
                    continue
                else:
                    print('NO')
                    break
            else:
                print('NO')
                break
        elif k == ']':
            if len(check_list) > 0:
                if check_list.pop() != '(':
                    count += 1
                    continue
                else:
                    print('NO')
                    break
            else:
                print('NO')
                break
        else:
            count += 1
    if len(check_list) == 0 and count == len(j):
        print('YES')

# 왜 틀려 ㅅㅂ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    # check_list = []
    # count = 0
    # for k in j:
    #     if k == '(':
    #         check_list.append('a')
    #     if k == ')':
    #         if len(check_list) == 0:
    #             count += 1
    #             break
    #         else:
    #             if check_list.pop() != 'a':
    #                 count += 1
    #                 break
    #     if k == '[':
    #         check_list.append('b')
    #     if k == ']':
    #         if len(check_list) == 0:
    #             count += 1
    #             break
    #         else:
    #             if check_list.pop() != 'b':
    #                 count += 1
    #                 break
    # if len(check_list) == 0 and count == 0:
    #     print('YES')
    # else:
    #     print('NO')

    # count = 0
    # _count = 0
    # for k in j:
    #     if k == '(':
    #         count += 1
    #     elif k == ')':
    #         count -= 1
    #     elif k == '[':
    #         _count += 1
    #     elif k == ']':
    #         _count -= 1
    #     if count < 0 or _count < 0:
    #         break
    #
    # if count == 0 and _count == 0:
    #     print('YES')
    # else:
    #     print('NO')

