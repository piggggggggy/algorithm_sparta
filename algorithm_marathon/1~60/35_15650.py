# N과 M(2)_중_백트래킹

import sys

N, M = map(int, sys.stdin.readline().split())

visited = [False] * N
out = []

def backtracking(depth, n, m):
    if depth == m:
        print(*out)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            out.append(i+1)
            backtracking(depth+1, n, m)
            out.pop()
 
            for j in range(i+1, n):
                visited[j] = False

backtracking(0, N, M) # N = 4, M = 2
# 1 2
# 1 3
# 1 4
# 2 3
# 2 4
# 3 4
