# N과 M (5)

import sys

N, M =map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
visited = [False] * N
out = []

# lst = [1, 7, 8, 9]

def five(depth, n, m):
    if depth == m:
        print(*out)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            out.append(lst[i])
            five(depth+1, n, m)
            out.pop()
            visited[i] = False


five(0, N, M)
