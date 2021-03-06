#  N과 M (4)
import sys

N, M = map(int, sys.stdin.readline().split())
visited = [False] * N
out = []

def four(depth, n, m):
    if depth == m:
        print(*out)
        return

    for i in range(n):
        if not visited[i]:
            out.append(i+1)
            four(depth+1, n, m)
            out.pop()
            visited[i] = True

            for j in range(i+1, n):
                visited[j] = False

four(0, N, M)


import sys
N, M = map(int, sys.stdin.readline().split())
out = []

def four(depth, idx, n, m):
    if depth == m:
        print(*out)
        return

    for i in range(idx, n):
        out.append(i+1)
        four(depth+1, i, n, m)
        out.pop()

four(0, 0, N, M)