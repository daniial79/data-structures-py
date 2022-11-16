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
            print(temp.value, end = " => ")
            temp = temp.next


    def dequeue(self):
        if self.first is None:
            return None
        temp = self.first
        if self.first is self.last:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
        self.length -= 1
        return temp

    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True