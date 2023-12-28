import unittest

from data_structures.graphs.graph_adjacency_list import Graph


class TestAdjacencyList(unittest.TestCase):
    def setUp(self):
        self.graph = Graph(5)
        self.directed_graph = {
            0: [(1, 1), (4, 1)],
            1: [(2, 1), (3, 1), (4, 1)],
            2: [(3, 1)],
            3: [(4, 1)],
            4: []
        }
        self.undirected_graph = {
            0: [(1, 1), (4, 1)],
            1: [(0, 1), (2, 1), (3, 1), (4, 1)],
            2: [(1, 1), (3, 1)],
            3: [(1, 1), (2, 1), (4, 1)],
            4: [(0, 1), (1, 1), (3, 1)]
        }

    def test_add_edge_directed(self):
        self.get_directed_graph()
        self.assertEqual(self.directed_graph, self.graph.graph)

    def test_add_edge_undirected(self):
        self.graph.add_edge(0, 1, False)
        self.graph.add_edge(0, 4, False)
        self.graph.add_edge(1, 2, False)
        self.graph.add_edge(1, 3, False)
        self.graph.add_edge(1, 4, False)
        self.graph.add_edge(2, 3, False)
        self.graph.add_edge(3, 4, False)

        self.assertEqual(self.undirected_graph, self.graph.graph)

    def test_add_node(self):
        for i in range(5):
            self.graph.add_node(i)

        self.assertEqual({i: [] for i in range(5)}, self.graph.graph, )

    def test_get_neighbors(self):
        self.get_directed_graph()
        self.assertEqual([(1, 1), (4, 1)], self.graph.get_neighbors(0))
        self.assertEqual([(2, 1), (3, 1), (4, 1)], self.graph.get_neighbors(1))
        self.assertEqual([(3, 1)], self.graph.get_neighbors(2))
        self.assertEqual([(4, 1)], self.graph.get_neighbors(3))
        self.assertEqual([], self.graph.get_neighbors(4))

    def get_directed_graph(self):
        self.graph.add_edge(0, 1, True, 1)
        self.graph.add_edge(0, 4, True, 1)
        self.graph.add_edge(1, 2, True, 1)
        self.graph.add_edge(1, 3, True, 1)
        self.graph.add_edge(1, 4, True, 1)
        self.graph.add_edge(2, 3, True, 1)
        self.graph.add_edge(3, 4, True, 1)


if __name__ == "__main__":
    unittest.main()
