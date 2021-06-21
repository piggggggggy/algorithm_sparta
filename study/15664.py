# N과 M (10)

import sys

N, M = map(int, sys.stdin.readline().split())
visited = [False] * N
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
out = []

def ten(depth, idx, n, m):
    if depth == m:
        print(*out)
        return

    check = 0
    for i in range(idx, n):
        if not visited[i] and check != lst[i]:
            out.append(lst[i])
            visited[i] = True
            check = lst[i]
            ten(depth+1, i+1, n, m)
            out.pop()
            visited[i] = False

ten(0,0, N, M)