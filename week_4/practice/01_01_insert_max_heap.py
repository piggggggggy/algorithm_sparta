class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        # 구현해보세요!
        self.items.append(value)
        i = len(self.items)-1
        while i > 1 :
            if self.items[i] > self.items[i//2]:
                self.items[i],self.items[i//2] = self.items[i//2],self.items[i]
                i = i //2
            else:
                break

max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)
# [None, 9, 4, 2, 3] 가 출력되어야 합니다!