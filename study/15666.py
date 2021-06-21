# N과 M (12)

import sys

N, M = map(int, sys.stdin.readline().split())
visited = [False] * N
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
out = []

def twelve(depth, idx, n, m):
    if depth == m:
        print(*out)
        return
    check = 0
    for i in range(idx, n):
        if not visited[i] and check != lst[i]:
            out.append(lst[i])
            check = lst[i]
            twelve(depth+1, i, n, m)
            out.pop()

twelve(0, 0, N, M)