class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index > 1:
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break

    def delete(self):
        n = len(self.items)-1
        del_node = self.items[1]
        if n > 2:
            self.items[1], self.items[-1] = self.items[-1], self.items[1]
            self.items = self.items[:-1]
            j = 1
            while n//2 > j:
                if self.items[j*2] > self.items[j*2+1] and self.items[j*2] > self.items[j]:
                    self.items[j], self.items[j*2] = self.items[j*2], self.items[j]
                elif self.items[j*2+1] > self.items[j*2] and self.items[j*2+1] > self.items[j]:
                    self.items[j], self.items[j*2+1] = self.items[j*2+1], self.items[j]
                elif self.items[j] > self.items[j*2] and self.items[j] > self.items[j*2+1]:
                    break
                j += 1

        return del_node


max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(6)
max_heap.insert(7)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)  # [None, 8, 6, 7, 2, 5, 4]
print(max_heap.delete())  # 8
print(max_heap.items)  # [None, 7, 6, 4, 2, 5]

