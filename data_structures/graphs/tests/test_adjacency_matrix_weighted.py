import unittest

from data_structures.graphs.graph_adjacency_matrix_weighted import WeightedGraphMatrix


class TestAdjacencyMatrix(unittest.TestCase):

    def test_get_directed_list(self):
        from data_structures.graphs.graph_adjacency_list_weighed import WeightedGraphList
        test_list = WeightedGraphList(3)
        self.matrix.add_edge(0, 1, True)
        test_list.add_edge(0, 1, True)
        g = self.matrix.get_list()

        self.assertEqual(test_list.graph, g.graph)

    def test_get_undirected_list(self):
        from data_structures.graphs.graph_adjacency_list_weighed import WeightedGraphList
        test_list = WeightedGraphList(3)
        self.matrix.add_edge(0, 1, False)
        test_list.add_edge(0, 1, False)
        g = self.matrix.get_list()

        self.assertEqual(test_list.graph, g.graph)

    def setUp(self):
        self.matrix = WeightedGraphMatrix(3)
        self.directed_graph = [
            [0, 1, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.undirected_graph = [
            [0, 1, 1],
            [1, 0, 0],
            [1, 0, 0]
        ]

    def test_add_edge_directed(self):
        self.matrix.add_edge(0, 1, True)

        self.assertEqual(self.directed_graph, self.matrix.graph, )

    def test_add_edge_undirected(self):
        self.matrix.add_edge(0, 1, False)
        self.matrix.add_edge(0, 2, False)
        self.assertEqual(self.undirected_graph, self.matrix.graph, )

    def test_add_node(self):
        self.matrix.add_node(4)
        self.assertEqual([
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ], self.matrix.graph)

    def test_get_neighbors(self):
        self.matrix.add_edge(0, 1, True)
        self.matrix.add_edge(0, 2, True)
        self.matrix.add_edge(1, 2, True)

        self.assertEqual([1, 2], self.matrix.get_neighbors(0))
        self.assertEqual([2], self.matrix.get_neighbors(1))
        self.assertEqual([], self.matrix.get_neighbors(2))


if __name__ == "__main__":
    unittest.main()
