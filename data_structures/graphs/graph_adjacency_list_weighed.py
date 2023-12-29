import heapq

from data_structures.graphs.graph_errors import (
    InvalidNeighborError,
    SelfLoopError,
    RepeatedEdgeError,
    MissingEdgeError
)
from data_structures.graphs.graph_adjacency_matrix_weighted import WeightedGraphMatrix


class WeightedGraphList:
    """
    A class to represent a graph using an adjacency list.

    ...

    Attributes
    ----------
    n : int
        the number of nodes in the graph
    graph : dict[int, list[tuple[int, int]]]
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
    get_matrix():
        Returns the graph as an adjacency matrix.
    get_neighbors_of_vip_nodes(vip_nodes):
        Returns a list of nodes that are adjacent to the given list of nodes.
    is_well_formed_undirected(graph):
        Returns True if the given graph is well-formed.
    reachable(start):
        Returns a list of nodes that are reachable from the given node.
    shortest_path(start, end):
        Returns the shortest path from the start node to the end node.
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

    def get_matrix(self) -> WeightedGraphMatrix:
        """
        Returns the graph as an adjacency matrix.
        """

        matrix = WeightedGraphMatrix(self.n)
        for edge in self.graph:
            for neighbor in self.graph[edge]:
                # if graph is undirected, entries will already be duplicated, so assume directed
                matrix.add_edge(edge, neighbor[0], True, neighbor[1])
        return matrix

    def get_neighbors_of_vip_nodes(self, vip_nodes: list[int]):
        is_neighbor = self.n * [False]
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

    def reachable(self, start: int) -> list:
        """
        Returns a list of nodes that are reachable from the given node.

        Parameters:
        node (int): The node whose reachable nodes are to be returned.

        Returns:
        list: A list of nodes that are reachable from the given node.
        """
        visited = self.n * [False]
        visited[start] = True
        self._reachable(start, visited)
        return visited

    def _reachable(self, node: int, visited: list[bool]):
        """
        Helper function for reachable.
        """
        for nbr in self.graph[node]:
            if not visited[nbr]:
                visited[nbr] = True
                self._reachable(nbr, visited)

    def shortest_path(self, start: int, end: int) -> list[int]:
        """
        Returns the shortest path from the start node to the end node.
        Uses Djikstra's algorithm.

        Parameters:
        start (int): The node from which the path starts.
        end (int): The node at which the path ends.

        Returns:
        list[int]: A list of nodes that form the shortest path from the start node to the end node.
        """
        visited = self.n * [False]
        prev = self.n * [None]
        Q = [(0, start)]
        while Q:
            (cost, node) = heapq.heappop(Q)
            if visited[node]:
                continue
            visited[node] = True
            if node == end:
                break
            for (next, c) in self.graph[node]:
                if visited[next]:
                    continue
                old_cost = visited[next]
                new_cost = cost + c
                if new_cost < old_cost:
                    visited[next] = new_cost
                    prev[next] = node
                    heapq.heappush(Q, (new_cost, next))
        path = []
        cur_node = end
        while cur_node is not None:
            path.insert(0, cur_node)
            cur_node = prev[cur_node]
        return path
