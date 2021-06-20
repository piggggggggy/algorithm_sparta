#  N과 M (4)
import sys

N, M = map(int, sys.stdin.readline().split())
visited = [False] * N
out = []

def four(depth, n, m):
    if depth == M:
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