# 스파르타 알고리즘 강의 2주차 숙제1번문제
# Q. 링크드 리스트의 끝에서 K번째 값을 반환하시오.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_kth_node_from_last(self, k):
        # 구현해보세요!
        count = 1
        check = self.head
        while check.next != None:
            check = check.next
            count += 1
        result_count = 0
        result_check = self.head
        while result_count < count - k:
            result_check = result_check.next
            result_count += 1
        return result_check


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(1).data)  # 7이 나와야 합니다!