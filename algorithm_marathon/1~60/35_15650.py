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
            # print('i:',i)
            # print('visit:', visited)
            # print('out1:', out)
            backtracking(depth+1, n, m)
            out.pop()
            # print('out2:', out)
            # print('i2:', i)

            for j in range(i+1, n):
                visited[j] = False
            # print('last visit:', visited)
backtracking(0, N, M) # N = 4, M = 2
# 1 2
# 1 3
# 1 4
# 2 3
# 2 4
# 3 4

# def two(depth, idx, n, m):
#     if depth == m:
#         print(*out)
#         return
#
#     for i in (idx, n):   # 달라진 부분
#         out.append(i+1)
#         two(depth, i, n, m)
#         out.pop()
#
        # 이렇게 풀면 visited를 만들지 않아도 되고 매우 간단히 풀 수 잇따..