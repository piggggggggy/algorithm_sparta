#
#
import heapq

heap = []

heapq.heappush(heap, 1)
heapq.heappush(heap, 5)
heapq.heappush(heap, 7)
heapq.heappush(heap, 2)
print(heap) # [1, 2, 7, 5]

heapq.heappop(heap)
print(heap) # [2, 5, 7]


a = [5, 9, 8, 4, 2]

heapq.heapify(a)
print(a) # [2, 4, 8, 5, 9]




 #
 #       8          level 0  [None, 8]
 #   6       3      level 1  [None, 8, 6, 3]
 # 4   2   5        level 2  [None, 8, 6, 3, 4, 2, 5]
 #
 #                => [None, 8, 6, 3, 4, 2, 5]
 #                의 구조를 갖는다.
 #    이 때,
 #    현재 인덱스(n)를 기준으로
 #    왼쪽 자식의 인덱스는  2 * n
 #    오른쪽 자식의 인덱스  2 * n + 1
 #    를 갖고
 #    부모의 인덱스는      n // 2
 #    를 갖는다.