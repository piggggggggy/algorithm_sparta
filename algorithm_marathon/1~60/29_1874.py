# 스택수열_스택_중상


import sys
from collections import deque

n = int(sys.stdin.readline())
stack = []
result_str = ''

cnt = 0
for i in range(n):
    k = int(sys.stdin.readline())
    while True:
        cnt += 1
        stack.append(cnt)
        result_str += '+\n'
        print(stack)
        print(result_str)
        if k in stack:
            if k == stack.pop():
                result_str += '-\n'
                break
            else:
                print('NO')
                exit()

print(result_str.rstrip())








# i = 0
# while data_dq:
#     if data_dq[0] not in stack:
#         stack.append(i+1)
#         result_str += '+\n'
#         i += 1
#     else:
#         if stack.pop() == data_dq[0]:
#             data_dq.popleft()
#             result_str += '-\n'
#         else:
#             print('NO')
#             exit()
#
# if not data_dq:
#     print(result_str.rstrip())
# else:
#     print('NO')

