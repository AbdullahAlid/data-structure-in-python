class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def enque(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def deque(self):
        if self.length == 0:
            return None
        temp = self.first
        self.first = self.first.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.last = None
        return temp


my_queue = Queue(6)
my_queue.enque(4)
my_queue.enque(9)
my_queue.deque()
my_queue.deque()
my_queue.deque()
my_queue.print_queue()
print(my_queue.first)
print(my_queue.last)
