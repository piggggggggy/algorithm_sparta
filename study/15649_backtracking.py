# N과 M (1)

import sys

N, M = map(int, sys.stdin.readline().split())
# 4 2
visited = [False] * N
out = []

def backtracking(depth, n, m):
    if depth == m:  # 탈출 조건
        print(*out)
        return

    for i in range(N)    i = 1, depth = 1, [ftff], out = [2]
        if visited[i]:
            continue
        visited[i] = True
        out.append(i+1)

        backtracking(depth+1, n, m)
        visited[i] = False
        out.pop()


backtracking(0, N, M)
