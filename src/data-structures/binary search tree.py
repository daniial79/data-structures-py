class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        temp = self.root
        while True:
            if temp.value == new_node.value:
                return False
            elif new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            elif new_node.value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right


    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        while temp is not None:
            if value == temp.value:
                return True
            elif value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
        return False
    
    def bfs(self):
        current_node = self.root
        queue, result = [], []
        queue.append(current_node)

        while len(queue) != 0:
            current_node = queue.pop(0)
            result.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        
        return result

    
    def pre_order_dfs(self):
        result = []

        def traverse(current_node):
            result.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        
        traverse(self.root)

        return result

    def in_order_dfs(self):
        result = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            result.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)

        return result

    def post_order_dfs(self):
        result = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            result.append(current_node.value)

        traverse(self.root)

        return result