# N과 M(2)_중_백트래킹

import sys

N, M = map(int, sys.stdin.readline().split())

lst = [i+1 for i in range(N)]

dict = {}
for i in lst:
    dict[i] = lst

start_node = 1
cnt = 0
while cnt <= N:
    result = []
    stack = [lst[cnt]]
    n = stack.pop()
    if n not in result:
        result.append(n)
        count = 0
        while count < M-1:
            count += 1

    cnt += 1