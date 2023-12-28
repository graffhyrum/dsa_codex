# Adjacency matrix representation of a graph


class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = [[0 for _ in range(n)] for _ in range(n)]

    def add_vertex(self, u):
        if u >= self.n:
            return
        self.graph[u] = [0 for _ in range(self.n)]

    def add_edge(self, u, v, d):
        if u >= self.n or v >= self.n:
            return
        self.graph[u][v] = 1
        if not d:
            self.graph[v][u] = 1

    def get_neighbors(self, u):
        if u >= self.n:
            return []
        return [v for v in range(self.n) if self.graph[u][v] == 1]

    def print_graph(self):
        for row in self.graph:
            print(row)


# Driver code
if __name__ == "__main__":
    graph = Graph(5)
    graph.add_edge(0, 1, True)
    graph.add_edge(0, 4, True)
    graph.add_edge(1, 2, True)
    graph.add_edge(1, 3, True)
    graph.add_edge(1, 4, True)
    graph.add_edge(2, 3, True)
    graph.add_edge(3, 4, True)
    graph.print_graph()
