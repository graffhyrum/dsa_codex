class Graph:
    """
    A class to represent a graph using an adjacency list.

    ...

    Attributes
    ----------
    n : int
        the number of nodes in the graph
    graph : dict[int, tuple[int, int]]
        a dictionary to store the graph where the keys are the nodes and
        the values are lists of adjacent nodes, with weights

    Methods
    -------
    add_node(value):
        Adds a node with the given value to the graph.
    add_edge(node1, node2, directed):
        Adds an edge between node1 and node2. If directed is False, an edge is also added from node2 to node1.
    get_neighbors(n):
        Returns a list of nodes that are adjacent to the node n.
    print_graph():
        Prints the graph.
    """

    def __init__(self, n: int = 0):
        """
        Constructs a graph with n nodes and no edges.

        Parameters:
        n (int): The number of nodes in the graph.
        """
        self.n = n
        self.graph: dict[int, tuple[int, int]] = {}
        for i in range(n):
            self.add_node(i)

    def add_node(self, value: int):
        """
        Adds a node with the given value to the graph.

        Parameters:
        value (int): The value of the node to be added.
        """
        if value not in self.graph:
            self.graph[value] = []

    def add_edge(self, node1: int, node2: int, is_directed: bool, weight: int = 1):
        """
        Adds an edge between node1 and node2. If directed is False, an edge is also added from node2 to node1.

        Parameters:
        node1 (int): The first node of the edge.
        node2 (int): The second node of the edge.
        directed (bool): If True, the edge is directed from node1 to node2. If False, an additional edge is added from node2 to node1.
        weight (int): The weight of the edge. Defaults to 1.
        """
        self.add_node(node1)
        self.add_node(node2)
        self.graph[node1].append((node2, weight))
        if not is_directed:
            if node2 not in self.graph:
                self.graph[node2] = []
            self.graph[node2].append((node1, weight))

    def get_neighbors(self, n: int) -> list:
        """
        Returns a list of nodes that are adjacent to the node n.

        Parameters:
        n (int): The node whose neighbors are to be returned.

        Returns:
        list: A list of nodes that are adjacent to the node n.
        """
        if n not in self.graph:
            return []
        return self.graph[n]

    def print_graph(self):
        """
        Prints the graph.
        """
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
