# N과 M (3)

import sys

N, M = map(int, sys.stdin.readline().split())
# visited = [False] * N
out = []

def threeeee(depth, n, m):
    if depth == m:
        print(*out)
        return

    for i in range(n):
        out.append(i+1)
        threeeee(depth+1, n, m)
        out.pop()


threeeee(0, N, M)