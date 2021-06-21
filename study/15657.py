# N과 M (8)
import sys

N, M = map(int, sys.stdin.readline().split())
visited = [False] * N
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
out = []

def eight(depth, n, m):
    if depth == m:
        print(*out)
        return

    for i in range(n):
        if not visited[i]:
            out.append(lst[i])
            eight(depth+1, n, m)
            out.pop()
            visited[i] = True

            for j in range(i+1, n):
                visited[j] = False

eight(0, N, M)

def eight(depth, idx, n, m):
    if depth == m:
        print(*out)
        return

    for i in range(idx, n):
        if not visited[i]:
            out.append(lst[i])
            eight(depth+1, i, n, m)
            out.pop()

eight(0, 0, N, M)