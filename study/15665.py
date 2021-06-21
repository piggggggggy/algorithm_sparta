# N과 M (11)

import sys

N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
visited = [False] * N
out = []

def eleven(depth, n, m):
    if depth == m:
        print(*out)
        return

    check = 0
    for i in range(n):
        if check != lst[i]:
            out.append(lst[i])
            check = lst[i]
            eleven(depth+1, n, m)
            out.pop()

eleven(0, N, M)