class InvalidNeighborError(Exception):
    pass


class SelfLoopError(Exception):
    pass


class RepeatedEdgeError(Exception):
    pass


class MissingEdgeError(Exception):
    pass


class GraphList:
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
        self.graph: dict[int, list[tuple[int, int]]] = {}
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
        Adds an edge between node1 and node2. If directed is False, an
        edge is also added from node2 to node1.

        Parameters:
        node1 (int): The first node of the edge.
        node2 (int): The second node of the edge.
        directed (bool): If True, the edge is directed from node1 to node2.
        If False, an additional edge is added from node2 to node1.
        weight (int): The weight of the edge. Defaults to 1.
        """
        self.add_node(node1)
        self.add_node(node2)
        self.graph[node1].append((node2, weight))
        if not is_directed:
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
        return [neighbor[0] for neighbor in self.graph[n]]

    def print_graph(self):
        """
        Prints the graph.
        """
        for vertex in self.graph:
            print(vertex, "->", self.graph[vertex])

    def get_matrix(self):
        """
        Returns the graph as an adjacency matrix.
        """
        from data_structures.graphs.graph_adjacency_matrix import GraphMatrix
        matrix = GraphMatrix(self.n)
        for edge in self.graph:
            for neighbor in self.graph[edge]:
                # if graph is undirected, entries will already be duplicated, so assume directed
                matrix.add_edge(edge, neighbor[0], True, neighbor[1])
        return matrix

    def get_neighbors_of_vip_nodes(self, vip_nodes: list[int]):
        is_neighbor = [False for _ in range(self.n)]
        for vip in vip_nodes:
            for nbr in self.graph[vip]:
                is_neighbor[nbr[0]] = True
        return [i for i in range(self.n) if is_neighbor[i]]

    @staticmethod
    def is_well_formed_undirected(graph: dict[int, list[tuple[int, int]]]) -> bool:
        """
        Returns True if the given graph is well-formed.

        Parameters:
        graph (dict[int, list[tuple[int, int]]]): The graph to be checked.

        Returns:
        bool: True if the given graph is well-formed.
        """
        n = len(graph)
        nbr_sets = [set(graph[node]) for node in range(n)]

        for node in range(n):
            # all neighbors are valid, no self loops, no repeated edges, all edges in both endpoints
            for nbr, weight in graph[node]:
                if nbr < 0 or nbr >= n:
                    raise InvalidNeighborError(f"Invalid neighbor {nbr} for node {node}")
                if node == nbr:
                    raise SelfLoopError(f"Self loop detected at node {node}")
                if graph[node].count((nbr, weight)) > 1:
                    raise RepeatedEdgeError(f"Repeated edges detected at node {node}")
                if (node, weight) not in nbr_sets[nbr]:
                    raise MissingEdgeError(f"Missing edge detected at node {node}")
        return True
