# N과 M (1)

import sys

N, M = map(int, sys.stdin.readline().split())

visited = [False] * N
out = []

def backtracking(depth, n, m):
    if depth == m:  # 탈출 조건
        print(*out)
        return

    for i in range(N): # check 하면서 탐사
        if visited[i]: # visited가 False이면, 즉, 탐사 안했다면
            continue
        visited[i] = True # 탐사 내용 얻데이트
        out.append(i+1) # 탐사 내용 (출력용)

        backtracking(depth+1, n, m) # 다음 깊이 탐색
        visited[i] = False # 탐사완료 후 빠꾸하기 위해
        out.pop() # 재귀함수 내에서 depth == m 이라는 조건을 만족하고 출력하고 나옴


backtracking(0, N, M)
