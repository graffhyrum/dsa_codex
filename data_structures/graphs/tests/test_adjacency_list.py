import unittest

from data_structures.graphs.graph_adjacency_list import Graph


class TestAdjacencyList(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()

    def test_add_edge_directed(self):
        self.graph.add_edge(0, 1, True)
        self.graph.add_edge(0, 4, True)
        self.graph.add_edge(1, 2, True)
        self.graph.add_edge(1, 3, True)
        self.graph.add_edge(1, 4, True)
        self.graph.add_edge(2, 3, True)
        self.graph.add_edge(3, 4, True)

        self.assertEqual(self.graph.graph, {
            0: [1, 4],
            1: [2, 3, 4],
            2: [3],
            3: [4],
            4: []
        })

    def test_add_edge_undirected(self):
        self.graph.add_edge(0, 1, False)
        self.graph.add_edge(0, 4, False)
        self.graph.add_edge(1, 2, False)
        self.graph.add_edge(1, 3, False)
        self.graph.add_edge(1, 4, False)
        self.graph.add_edge(2, 3, False)
        self.graph.add_edge(3, 4, False)

        self.assertEqual(self.graph.graph, {
            0: [1, 4],
            1: [0, 2, 3, 4],
            2: [1, 3],
            3: [1, 2, 4],
            4: [0, 1, 3]
        })

    def test_add_vertex(self):
        self.graph.add_vertex(0)
        self.graph.add_vertex(1)
        self.graph.add_vertex(2)
        self.graph.add_vertex(3)
        self.graph.add_vertex(4)

        self.assertEqual(self.graph.graph, {
            0: [],
            1: [],
            2: [],
            3: [],
            4: []
        })

    def test_get_neighbors(self):
        self.graph.add_edge(0, 1, True)
        self.graph.add_edge(0, 4, True)
        self.graph.add_edge(1, 2, True)
        self.graph.add_edge(1, 3, True)
        self.graph.add_edge(1, 4, True)
        self.graph.add_edge(2, 3, True)
        self.graph.add_edge(3, 4, True)

        self.assertEqual(self.graph.get_neighbors(0), [1, 4])
        self.assertEqual(self.graph.get_neighbors(1), [2, 3, 4])
        self.assertEqual(self.graph.get_neighbors(2), [3])
        self.assertEqual(self.graph.get_neighbors(3), [4])
        self.assertEqual(self.graph.get_neighbors(4), [])


if __name__ == "__main__":
    unittest.main()
