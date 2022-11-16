class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])
    
    def add_vertex(self, ver):
        if ver not in self.adj_list:
            self.adj_list[ver] = []
            return True
        return False

    def add_edge(self, ver1, ver2):
        if ver1 in self.adj_list and ver2 in self.adj_list:
            if ver2 not in self.adj_list[ver1]:
                self.adj_list[ver1].append(ver2)
            if ver1 not in self.adj_list[ver2]:
                self.adj_list[ver2].append(ver1)
        return False

    def remove_edge(self, ver1, ver2):
        if ver1 in self.adj_list[ver2] or ver2 in self.adj_list[ver1]:
            if ver1 in self.adj_list[ver2]:
                self.adj_list[ver2].remove(ver1)
            if ver2 in self.adj_list[ver1]:
                self.adj_list[ver1].remove(ver2)
            return True 
        return False

    def remove_vertex(self, ver):
        if ver in self.adj_list:
            for other_ver in self.adj_list[ver]:
                self.adj_list[other_ver].remove(ver)
            del self.adj_list[ver]
            return True
        return False