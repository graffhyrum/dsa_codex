import unittest

from data_structures.graphs.graph_adjacency_list import GraphList
from data_structures.graphs.graph_adjacency_matrix import GraphMatrix


class TestAdjacencyList(unittest.TestCase):
    def setUp(self):
        self.list = GraphList(3)
        self.directed_graph = {
            0: [(1, 1)],
            1: [(2, 1)],
            2: []
        }
        self.undirected_graph = {
            0: [(1, 1)],
            1: [(0, 1)],
            2: []
        }

    def test_add_edge_directed(self):
        self.list.add_edge(0, 1, True, 1)
        self.list.add_edge(1, 2, True, 1)

        self.assertEqual(self.directed_graph, self.list.graph)

    def test_add_edge_undirected(self):
        self.list.add_edge(0, 1, False, 1)

        self.assertEqual(self.undirected_graph, self.list.graph)

    def test_add_node(self):
        for i in range(5):
            self.list.add_node(i)

        self.assertEqual({i: [] for i in range(5)}, self.list.graph, )

    def test_get_neighbors(self):
        self.get_directed_graph()
        self.assertEqual([1,4], self.list.get_neighbors(0))
        self.assertEqual([2,3,4], self.list.get_neighbors(1))
        self.assertEqual([3], self.list.get_neighbors(2))
        self.assertEqual([4], self.list.get_neighbors(3))
        self.assertEqual([], self.list.get_neighbors(4))

    def test_get_directed_matrix(self):
        g = GraphMatrix(3)
        self.list.add_edge(0, 1, True, 1)
        g.add_edge(0, 1, True, 1)
        m = self.list.get_matrix()

        self.assertEqual(g.graph, m.graph)

    def test_get_undirected_matrix(self):
        g = GraphMatrix(3)
        self.list.add_edge(0, 1, False, 1)
        g.add_edge(0, 1, False, 1)
        m = self.list.get_matrix()

        self.assertEqual(g.graph, m.graph)

    def get_directed_graph(self):
        self.list.add_edge(0, 1, True, 1)
        self.list.add_edge(0, 4, True, 1)
        self.list.add_edge(1, 2, True, 1)
        self.list.add_edge(1, 3, True, 1)
        self.list.add_edge(1, 4, True, 1)
        self.list.add_edge(2, 3, True, 1)
        self.list.add_edge(3, 4, True, 1)


if __name__ == "__main__":
    unittest.main()
