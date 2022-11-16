class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        if self.head is None:
            print(None)
        else:
            node = self.head
            while node is not None:
                print(node.value, end = " => ")
                node = node.next
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.head is None:
            return None
        elif self.head is self.tail:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        else:
            pre = self.head
            temp = self.head
            while True:
                temp = temp.next
                if temp.next is None:
                    break
                pre = pre.next
            self.tail = pre
            self.tail.next = None
            self.length -= 1
            return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length +=1
        return True

    def pop_first(self):
        if self.head is None:
            return None
        elif self.head is self.tail:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
            return temp
    
    def get(self, index):
        if index < 0 or index > self.length - 1:
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp :
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        """
        this method will shift the previous index node to right
        """
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
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
        prev = self.get(index - 1)
        prev.next = temp.next
        temp.next = None
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after