class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        # 어떻게 하면 될까요?
        new = Node(value)
        if self.is_empty():
            self.head = new
            self.tail = new
            return
        self.tail.next = Node(value)
        self.tail = Node(value)

    def dequeue(self):
        # 어떻게 하면 될까요?
        if self.is_empty():
            return "Queue is Empty"
        delete_head = self.head
        self.head = self.head.next
        return delete_head.data

    def peek(self):
        # 어떻게 하면 될까요?
        if self.is_empty():
            return "Queue is Empty"
        return self.head.data

    def is_empty(self):
        # 어떻게 하면 될까요?
        return self.head is None

qq = Queue()
qq.enqueue(2)
qq.enqueue(6)
qq.enqueue(7)
print(qq.head.data)
qq.dequeue()
print(qq.peek())
print(qq.is_empty())