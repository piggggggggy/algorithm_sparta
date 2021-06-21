# N과 M (6)

import sys

N,M = map(int, sys.stdin.readline().split())
visited = [False] * N
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
out = []

def six(depth, n, m):
    if depth == m:
        print(*out)
        return

    for i in range(n):
        if not visited[i]:
            out.append(lst[i])
            visited[i] = True
            six(depth+1, n, m)
            out.pop()

            for j in range(i+1, n):
                visited[j] = False

six(0, N, M)