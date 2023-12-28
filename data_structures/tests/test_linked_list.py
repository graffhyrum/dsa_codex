import unittest

from data_structures.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedList()

    def test_append(self):
        self.linked_list.append("A")
        self.assertEqual(self.linked_list.head.data, "A")
        self.linked_list.append("B")
        self.assertEqual(self.linked_list.head.next.data, "B")

    def test_prepend(self):
        self.linked_list.prepend("A")
        self.assertEqual(self.linked_list.head.data, "A")
        self.linked_list.prepend("B")
        self.assertEqual(self.linked_list.head.data, "B")

    def test_insert_after_node(self):
        self.linked_list.append("A")
        self.linked_list.append("B")
        self.linked_list.insert_after_node(self.linked_list.head, "C")
        self.assertEqual(self.linked_list.head.next.data, "C")

    def test_delete_node(self):
        self.linked_list.append("A")
        self.linked_list.append("B")
        self.linked_list.append("C")
        self.linked_list.append("D")
        self.linked_list.delete_node("B")
        self.assertEqual(self.linked_list.head.next.data, "C")
        self.linked_list.delete_node("A")
        self.assertEqual(self.linked_list.head.data, "C")
        self.linked_list.delete_node("D")
        self.assertEqual(self.linked_list.head.next, None)

    def test_delete_node_with_one_node(self):
        self.linked_list.append("A")
        self.linked_list.delete_node("A")
        self.assertEqual(self.linked_list.head, None)

    def test_delete_node_with_no_nodes(self):
        self.linked_list.delete_node("A")
        self.assertEqual(self.linked_list.head, None)

    def test_swap_nodes(self):
        self.linked_list.append("A")
        self.linked_list.append("B")
        self.linked_list.append("C")
        self.linked_list.append("D")
        self.linked_list.swap_nodes("B", "C")
        self.assertEqual(self.linked_list.head.next.data, "C")
        self.linked_list.swap_nodes("A", "D")
        self.assertEqual(self.linked_list.head.data, "D")
        self.linked_list.swap_nodes("B", "B")
        self.assertEqual(self.linked_list.head.next.data, "C")

    def test_reverse_iterative(self):
        self.linked_list.append("A")
        self.linked_list.append("B")
        self.linked_list.append("C")
        self.linked_list.append("D")
        self.linked_list.reverse_iterative()
        self.assertEqual(self.linked_list.head.data, "D")
        self.assertEqual(self.linked_list.head.next.data, "C")
        self.assertEqual(self.linked_list.head.next.next.data, "B")
        self.assertEqual(self.linked_list.head.next.next.next.data, "A")

    def test_reverse_recursive(self):
        self.linked_list.append("A")
        self.linked_list.append("B")
        self.linked_list.append("C")
        self.linked_list.append("D")
        self.linked_list.reverse_recursive()
        self.assertEqual(self.linked_list.head.data, "D")
        self.assertEqual(self.linked_list.head.next.data, "C")
        self.assertEqual(self.linked_list.head.next.next.data, "B")
        self.assertEqual(self.linked_list.head.next.next.next.data, "A")

    def test_merge_sorted(self):
        llist_1 = LinkedList()
        llist_1.append(1)
        llist_1.append(5)
        llist_1.append(7)
        llist_1.append(9)

        llist_2 = LinkedList()
        llist_2.append(2)
        llist_2.append(3)
        llist_2.append(4)
        llist_2.append(6)
        llist_2.append(8)

        llist_1.merge_sorted(llist_2)
        self.assertEqual(llist_1.head.data, 1)
        self.assertEqual(llist_1.head.next.data, 2)
        self.assertEqual(llist_1.head.next.next.data, 3)
        self.assertEqual(llist_1.head.next.next.next.data, 4)
        self.assertEqual(llist_1.head.next.next.next.next.data, 5)
        self.assertEqual(llist_1.head.next.next.next.next.next.data, 6)
        self.assertEqual(llist_1.head.next.next.next.next.next.next.data, 7)
        self.assertEqual(llist_1.head.next.next.next.next.next.next.next.data, 8)
        self.assertEqual(llist_1.head.next.next.next.next.next.next.next.next.data, 9)

    def test_remove_duplicates(self):
        llist_3 = LinkedList()
        llist_3.append(1)
        llist_3.append(6)
        llist_3.append(1)
        llist_3.append(4)
        llist_3.append(2)
        llist_3.append(2)
        llist_3.append(4)

        llist_3.remove_duplicates()
        self.assertEqual(llist_3.head.data, 1)
        self.assertEqual(llist_3.head.next.data, 6)
        self.assertEqual(llist_3.head.next.next.data, 4)
        self.assertEqual(llist_3.head.next.next.next.data, 2)

    def test_get_nth_from_last(self):
        self.linked_list.append("A")
        self.linked_list.append("B")
        self.linked_list.append("C")
        self.linked_list.append("D")
        self.assertEqual(self.linked_list.get_nth_from_last(2), "C")
        self.assertEqual(self.linked_list.get_nth_from_last(4), "A")

    def test_get_nth_from_last_two_ptrs(self):
        self.linked_list.append("A")
        self.linked_list.append("B")
        self.linked_list.append("C")
        self.linked_list.append("D")
        self.assertEqual(self.linked_list.get_nth_from_last_2pointer(2), "C")
        self.assertEqual(self.linked_list.get_nth_from_last_2pointer(4), "A")
