class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            if self.head is self.tail:
                print(f"<= {temp.value} =>")
            elif temp is self.head:
                print("<=", temp.value, end = " <=> ")
            elif temp is self.tail:
                print(temp.value, "=>\n")
            else:
                print(temp.value, end = " <=> ")
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.head is None:
            return None
        if self.head is self.tail:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        temp = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.head is None:
            return None
        if self.head is self.tail:
            temp = self.head
            self.head = None
            self.tail = None
            self.length-= 1
            return temp
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.head.prev = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index > self.length - 1:
            return None
        else:
            if index < self.length / 2:
                temp = self.head
                for _ in range(index):
                    temp = temp.next
            else:
                temp = self.tail
                for _ in range(self.length - 1, index, -1):
                    temp = temp.prev
            return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index >= self.length - 1:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length - 1:
            return self.append(value)
        new_node = Node(value)
        before = self.get(index - 1)
        new_node.next = before.next
        new_node.prev = before
        before.next.prev = new_node
        before.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index > self.length - 1:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        temp = self.get(index)
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp

