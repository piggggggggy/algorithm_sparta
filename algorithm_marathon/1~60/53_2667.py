# 단지번호붙이기_중

import sys

n = int(sys.stdin.readline())

lst = [[int(j) for j in sys.stdin.readline().strip()] for i in range(n)]

cnt = 0

def apart(a, b):
    global cnt
    if a >= 0 and a < n and b >= 0 and b < n:
        if lst[a][b] == 1:
            lst[a][b] = 2
            cnt +=1
            apart(a-1, b)
            apart(a+1, b)
            apart(a, b-1)
            apart(a, b+1)
        return
    else:
        return

cnt_list = []
for i in range(n):
    for j in range(n):
        if lst[i][j] == 1:
            apart(i, j)
            cnt_list.append(cnt)
            cnt = 0

cnt_list.sort()
print(len(cnt_list))
for k in cnt_list:
    print(k)





# try2

# visited = [[0]*n for i in range(n)]
#
# xx = [-1,1,0,0]
# yy = [0,0,-1,1]
#
# def move(x,y):
#     visited[y][x] = 1
#     global cnt
#     if lst[y][x] == 1:
#         cnt += 1
#
#     for i in range(4):
#         nx = x+xx[i]
#         ny = y+yy[i]
#         if 0 <= nx < n and 0 <= ny < n:
#             if visited[ny][nx] == 0 and lst[ny][nx] == 0:
#                 move(nx, ny)
#
# cnt = 0
# nums = 0
# cnt_list = []
# for i in range(n):
#     for j in range(n):
#         if visited[i][j] == 0 and lst[i][j] == 1:
#             move(i,j)
#             cnt_list.append(cnt)
#             cnt = 0
#             print(visited)
# cnt_list.sort()
# print(len(cnt_list))
# for k in cnt_list:
#     print(k)



# try1

# print(lst)
#
# a = 0
# b = 0
# cnt = 0
#
# def find(a, b):
#     global cnt
#     while True:
#         if lst[a][b] == 1:
#             lst[a][b] = 0
#             cnt += 1
#             if lst[a][b+1] == 1:
#                 find(a, b+1)
#             if lst[a+1][b] == 1:
#                 find(a+1, b)
#             if b > 0:
#                 if lst[a][b-1] == 1:
#                     find(a,b-1)
#             if a > 0:
#                 if lst[a-1][b] == 1:
#                     find(a-1,b)
#         elif lst[a][b] == 0: