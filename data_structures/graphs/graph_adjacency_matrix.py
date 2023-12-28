class Graph:
    """
    A class to represent a graph using an adjacency matrix.

    ...

    Attributes
    ----------
    n : int
        the number of nodes in the graph
    graph : list of  int
        a 2D list to store the graph where the element at index [i][j] is 1 if there is an edge from node i to node j and 0 otherwise

    Methods
    -------
    add_node(value):
        Adds a node with the given value to the graph.
    add_edge(node1, node2, is_directed):
        Adds an edge from node1 to node2. If is_directed is False, an edge is also added from node2 to node1.
    get_neighbors(n):
        Returns a list of nodes that are adjacent to the node n.
    print_graph():
        Prints the graph.
    """

    def __init__(self, n):
        """
        Constructs a graph with n nodes and no edges.

        Parameters:
        n (int): The number of nodes in the graph.
        """
        self.n = n
        self.graph = [[0 for _ in range(n)] for _ in range(n)]

    def add_node(self, value):
        """
        Adds a node with the given value to the graph.

        Parameters:
        value (int): The value of the node to be added.
        """
        if value >= self.n:
            return
        self.graph[value] = [0 for _ in range(self.n)]

    def add_edge(self, node1, node2, is_directed):
        """
        Adds an edge from node1 to node2. If is_directed is False, an edge is also added from node2 to node1.

        Parameters:
        node1 (int): The first node of the edge.
        node2 (int): The second node of the edge.
        is_directed (bool): If True, the edge is directed from node1 to node2. If False, an additional edge is added from node2 to node1.
        """
        if node1 >= self.n or node2 >= self.n:
            return
        self.graph[node1][node2] = 1
        if not is_directed:
            self.graph[node2][node1] = 1

    def get_neighbors(self, n):
        """
        Returns a list of nodes that are adjacent to the node n.

        Parameters:
        n (int): The node whose neighbors are to be returned.

        Returns:
        list: A list of nodes that are adjacent to the node n.
        """
        if n >= self.n:
            return []
        return [v for v in range(self.n) if self.graph[n][v] == 1]

    def print_graph(self):
        """
        Prints the graph.
        """
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