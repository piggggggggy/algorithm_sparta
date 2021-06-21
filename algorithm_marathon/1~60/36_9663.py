# N-Queen_중_백트래킹

import sys

N = int(sys.stdin.readline())
# visited = [1] * N 깊은 복사/얕은 복사
visited_array = [[1] * N for i in range(N)]
print(visited_array)

cnt = 0
def queen(depth, idx, n):
    global cnt
    if depth == n:
        print('result :',visited_array)
        res = 1
        for l in visited_array:
            res *= sum(l)
        cnt += res
        return cnt

    for i in range(idx, n):
        if visited_array[depth][i] == 1:
            for j in range(n):
                visited_array[depth][j] = 0
            visited_array[depth][i] = 1
            print('i :',i,'dpth :',depth)
            print('1 :', visited_array)


            col = depth +1  #2
            row = i +1      #3
            while col < n or row < n:
                if visited_array[col][row] == 1:
                    visited_array[col][row] = 0
                col += 1
                row += 1

            col = depth + 1
            while col < n:
                if visited_array[col][i]:
                    visited_array[col][i] = 0
                col += 1

            _col = depth
            _row = i
            while _col < n-1 or _row > 0:
                _col += 1
                _row -= 1
                if visited_array[_col][_row]:
                    visited_array[_col][_row] = 0


            print('depth :',depth,'-',visited_array)
            queen(depth+1, i, n)


print(queen(0, 0, N))