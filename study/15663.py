# N과 M (9)

import sys

N, M = map(int, sys.stdin.readline().split())
visited = [False] * N
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
out = []

def nine(depth, n, m):
    if depth == m:
        print(*out)
        return

    check = 0
    for i in range(n):
        if not visited[i] and check != lst[i]:
            out.append(lst[i])
            visited[i] = True
            check = lst[i]
            nine(depth+1, n, m)
            out.pop()
            visited[i] = False

nine(0, N, M)
