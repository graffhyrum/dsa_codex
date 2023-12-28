import unittest

from data_structures.graphs.graph_adjacency_list import Graph


class TestAdjacencyList(unittest.TestCase):
    def setUp(self):
        self.graph = Graph(5)
        self.directed_graph = {
            0: [1, 4],
            1: [2, 3, 4],
            2: [3],
            3: [4],
            4: []
        }
        self.undirected_graph = {
            0: [1, 4],
            1: [0, 2, 3, 4],
            2: [1, 3],
            3: [1, 2, 4],
            4: [0, 1, 3]
        }

    def test_add_edge_directed(self):
        self.get_directed_graph()
        self.assertEqual(self.graph.graph, self.directed_graph)

    def test_add_edge_undirected(self):
        self.graph.add_edge(0, 1, False)
        self.graph.add_edge(0, 4, False)
        self.graph.add_edge(1, 2, False)
        self.graph.add_edge(1, 3, False)
        self.graph.add_edge(1, 4, False)
        self.graph.add_edge(2, 3, False)
        self.graph.add_edge(3, 4, False)

        self.assertEqual(self.graph.graph, self.undirected_graph)

    def test_add_node(self):
        for i in range(5):
            self.graph.add_node(i)

        self.assertEqual(self.graph.graph, {i: [] for i in range(5)})

    def test_get_neighbors(self):
        self.get_directed_graph()
        self.assertEqual(self.graph.get_neighbors(0), [1, 4])
        self.assertEqual(self.graph.get_neighbors(1), [2, 3, 4])
        self.assertEqual(self.graph.get_neighbors(2), [3])
        self.assertEqual(self.graph.get_neighbors(3), [4])
        self.assertEqual(self.graph.get_neighbors(4), [])

    def get_directed_graph(self):
        self.graph.add_edge(0, 1, True)
        self.graph.add_edge(0, 4, True)
        self.graph.add_edge(1, 2, True)
        self.graph.add_edge(1, 3, True)
        self.graph.add_edge(1, 4, True)
        self.graph.add_edge(2, 3, True)
        self.graph.add_edge(3, 4, True)


if __name__ == "__main__":
    unittest.main()
