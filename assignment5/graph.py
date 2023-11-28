class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, person):
        if person not in self.adjacency_list:
            self.adjacency_list[person] = []

    def add_edge(self, person1, person2, relationship):
        if person1 in self.adjacency_list and person2 in self.adjacency_list:
            self.adjacency_list[person1].append((person2, relationship))
            self.adjacency_list[person2].append((person1, relationship))