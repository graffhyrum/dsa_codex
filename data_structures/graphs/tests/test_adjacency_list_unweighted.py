import unittest

from data_structures.graphs.graph_adjacency_list import UnweightedGraphList
from data_structures.graphs.graph_errors import InvalidNeighborError, SelfLoopError, RepeatedEdgeError, MissingEdgeError
from data_structures.graphs.graph_adjacency_matrix import UnweightedGraphMatrix


class TestAdjacencyList(unittest.TestCase):
    def get_directed_graph(self):
        self.list.add_edge(0, 1, True)
        self.list.add_edge(1, 2, True)

    def get_undirected_graph(self):
        self.list.add_edge(0, 1, False)

    def setUp(self):
        self.list = UnweightedGraphList(3)
        self.directed_graph = {
            0: [1],
            1: [2],
            2: []
        }
        self.undirected_graph = {
            0: [1],
            1: [0],
            2: []
        }

    def test_add_edge_directed(self):
        self.get_directed_graph()
        self.assertEqual(self.directed_graph, self.list.graph)

    def test_add_edge_undirected(self):
        self.list.add_edge(0, 1, False)

        self.assertEqual(self.undirected_graph, self.list.graph)

    def test_add_node(self):
        for i in range(5):
            self.list.add_node(i)

        self.assertEqual({i: [] for i in range(5)}, self.list.graph, )

    def test_get_neighbors(self):
        self.get_directed_graph()

        self.assertEqual([1], self.list.get_neighbors(0))
        self.assertEqual([2], self.list.get_neighbors(1))

    def test_get_directed_matrix(self):
        g = UnweightedGraphMatrix(3)
        self.list.add_edge(0, 1, True)
        g.add_edge(0, 1, True)
        m = self.list.get_matrix()

        self.assertEqual(g.graph, m.graph)

    def test_get_undirected_matrix(self):
        g = UnweightedGraphMatrix(3)
        self.list.add_edge(0, 1, False)
        g.add_edge(0, 1, False)
        m = self.list.get_matrix()

        self.assertEqual(g.graph, m.graph)

    def test_vip(self):
        self.get_directed_graph()
        vips = [1]

        self.assertEqual([2], self.list.get_neighbors_of_vip_nodes(vips))

    def test_is_well_formed_undirected(self):
        self.get_undirected_graph()
        self.assertTrue(self.list.is_well_formed_undirected(self.list.graph))

    def test_not_well_formed_undirected(self):
        invalid_neighbor = {0: [1], 1: [0], 2: [3]}
        self.assertRaises(InvalidNeighborError, self.list.is_well_formed_undirected, invalid_neighbor)

        self_looping = {0: [0, 1], 1: [0]}
        self.assertRaises(SelfLoopError, self.list.is_well_formed_undirected, self_looping)

        repeated_edge = {0: [1, 1], 1: [0]}
        self.assertRaises(RepeatedEdgeError, self.list.is_well_formed_undirected, repeated_edge)

        missing_edge = {0: [1], 1: []}
        self.assertRaises(MissingEdgeError, self.list.is_well_formed_undirected, missing_edge)


if __name__ == "__main__":
    unittest.main()
