# Adjacency list representation of a graph


class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, u):
        if u not in self.graph:
            self.graph[u] = []

    def add_edge(self, u, v, d):
        if u not in self.graph:
            self.add_vertex(u)
        if v not in self.graph:
            self.add_vertex(v)
        self.graph[u].append(v)
        if not d:
            if v not in self.graph:
                self.graph[v] = []
            self.graph[v].append(u)

    def get_neighbors(self, u):
        if u not in self.graph:
            return []
        return self.graph[u]

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
