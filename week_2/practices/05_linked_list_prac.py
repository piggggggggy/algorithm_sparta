#스파르타 알고리즘 강의 1주차 1번문제
# Q. 다음과 같은 두 링크드 리스트를 입력받았을 때, 합산한 값을 반환하시오.
# 예를 들어 아래와 같은 링크드 리스트를 입력받았다면,
# 각각 678, 354 이므로 두개의 총합
# 678+354 = 1032 를 반환해야 한다.
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


def get_linked_list_sum(linked_list_1, linked_list_2):
    # 구현해보세요!
    num_1 = linked_list_1.head
    num_2 = linked_list_2.head
    res_1 = ''
    res_2 = ''
    while num_1 is not None:
        res_1 += str(num_1.data)
        num_1 = num_1.next
    while num_2 != None:
        res_2 += str(num_2.data)
        num_2 = num_2.next
    return int(res_1)+int(res_2)
# 잘 풀었지만 반복되는 부분은 새로운 사용자정의 함수를 만들어 간단하게!!

linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)
linked_list_1.append(1)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)
linked_list_2.append(1)

print(get_linked_list_sum(linked_list_1, linked_list_2))