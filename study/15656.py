# N과 M (7)

import sys

N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
out = []

def seven(depth, n, m):
    if depth == m:
        print(*out)
        return

    for i in range(n):
        if not visited[i]:
            out.append(lst[i])
            seven(depth+1, n, m)
            out.pop()

seven(0, N, M)