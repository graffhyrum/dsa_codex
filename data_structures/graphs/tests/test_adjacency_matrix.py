import unittest

from data_structures.graphs.graph_adjacency_matrix import Graph


class TestAdjacencyMatrix(unittest.TestCase):
    def setUp(self):
        self.graph = Graph(3)

    def test_add_edge_directed(self):
        self.graph.add_edge(0, 1, True)

        self.assertEqual([
            [0, 1, 0],
            [0, 0, 0],
            [0, 0, 0]
        ], self.graph.graph, )

    def test_add_edge_undirected(self):
        self.graph.add_edge(0, 1, False)
        self.graph.add_edge(0, 2, False)
        self.graph.add_edge(1, 2, False)

        self.assertEqual(self.graph.graph, [
            [0, 1, 1],
            [1, 0, 1],
            [1, 1, 0]
        ])

    def test_add_node(self):
        self.graph.add_node(4)
        self.assertEqual([
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ], self.graph.graph)

    def test_get_neighbors(self):
        self.graph.add_edge(0, 1, True)
        self.graph.add_edge(0, 2, True)
        self.graph.add_edge(1, 2, True)

        self.assertEqual([1, 2], self.graph.get_neighbors(0))
        self.assertEqual([2], self.graph.get_neighbors(1))
        self.assertEqual([], self.graph.get_neighbors(2))


if __name__ == "__main__":
    unittest.main()
