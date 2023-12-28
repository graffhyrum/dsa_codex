# Adjacency list representation of a graph


class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, n):
        if n not in self.graph:
            self.graph[n] = []

    def add_edge(self, node1, node2, directed):
        if node1 not in self.graph:
            self.add_node(node1)
        if node2 not in self.graph:
            self.add_node(node2)
        self.graph[node1].append(node2)
        if not directed:
            if node2 not in self.graph:
                self.graph[node2] = []
            self.graph[node2].append(node1)

    def get_neighbors(self, n):
        if n not in self.graph:
            return []
        return self.graph[n]

    def print_graph(self):
        for vertex in self.graph:
            print(vertex, "->", self.graph[vertex])


# Driver code
if __name__ == "__main__":
    graph = Graph()
    graph.add_edge(0, 1, True)
    graph.add_edge(0, 4, True)
    graph.add_edge(1, 2, True)
    graph.add_edge(1, 3, True)
    graph.add_edge(1, 4, True)
    graph.add_edge(2, 3, True)
    graph.add_edge(3, 4, True)
    graph.print_graph()
