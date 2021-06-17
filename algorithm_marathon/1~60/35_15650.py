# N과 M(2)_중_백트래킹

import sys

N, M = map(int, sys.stdin.readline().split())

lst = [i+1 for i in range(N)]

dict = {}
for i in lst:
    dict[i] = lst

