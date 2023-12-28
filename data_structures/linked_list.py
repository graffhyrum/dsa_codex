# A Linked List implementation in Python


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node is not in the list")
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        current_node = self.head

        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return

        prev_node = None
        while current_node and current_node.data != key:
            prev_node = current_node
            current_node = current_node.next

        if current_node is None:
            return

        prev_node.next = current_node.next
        current_node = None

    def delete_node_at_pos(self, pos):
        current_node = self.head

        if pos == 0:
            self.head = current_node.next
            current_node = None
            return

        prev_node = None
        count = 1
        while current_node and count != pos:
            prev_node = current_node
            current_node = current_node.next
            count += 1

        if current_node is None:
            return

        prev_node.next = current_node.next
        current_node = None

    def len_iterative(self):
        count = 0
        current_node = self.head

        while current_node:
            count += 1
            current_node = current_node.next

        return count

    def len_recursive(self, node):
        if node is None:
            return 0

        return 1 + self.len_recursive(node.next)

    def swap_nodes(self, key_1, key_2):
        if key_1 == key_2:
            return

        prev_1 = None
        current_1 = self.head
        while current_1 and current_1.data != key_1:
            prev_1 = current_1
            current_1 = current_1.next

        prev_2 = None
        current_2 = self.head
        while current_2 and current_2.data != key_2:
            prev_2 = current_2
            current_2 = current_2.next

        if not current_1 or not current_2:
            return

        if prev_1:
            prev_1.next = current_2
        else:
            self.head = current_2

        if prev_2:
            prev_2.next = current_1
        else:
            self.head = current_1

        current_1.next, current_2.next = current_2.next, current_1.next

    def reverse_iterative(self):
        prev_node = None
        current_node = self.head
        while current_node:
            nxt = current_node.next
            current_node.next = prev_node

            prev_node = current_node
            current_node = nxt

        self.head = prev_node

    def reverse_recursive(self):
        def _reverse_recursive(current_node, prev_node):
            if not current_node:
                return prev_node

            nxt = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = nxt

            return _reverse_recursive(current_node, prev_node)

        self.head = _reverse_recursive(current_node=self.head, prev_node=None)

    def merge_sorted(self, llist):
        p = self.head
        q = llist.head
        s = None

        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next

            new_head = s

        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next

        if not p:
            s.next = q
        if not q:
            s.next = p

        return new_head

    def remove_duplicates(self):
        current_node = self.head
        prev_node = None

        dup_values = dict()

        while current_node:
            if current_node.data in dup_values:
                prev_node.next = current_node.next
                current_node = None
            else:
                dup_values[current_node.data] = 1
                prev_node = current_node

            current_node = prev_node.next

    def get_nth_from_last(self, n):
        total_len = self.len_iterative()

        current_node = self.head
        while current_node:
            if total_len == n:
                return current_node.data

            total_len -= 1
            current_node = current_node.next

        if current_node is None:
            return

    def get_nth_from_last_2pointer(self, n):
        p = self.head
        q = self.head

        count = 0
        while q:
            count += 1
            if count >= n:
                break
            q = q.next

        if not q:
            print(str(n) + " is greater than the number of nodes in the list.")
            return

        while p and q.next:
            p = p.next
            q = q.next

        return p.data


if __name__ == '__main__':
    llist = LinkedList()
    llist.append("A")
    llist.append("B")
    llist.append("C")
    llist.append("D")

    print(llist.get_nth_from_last(4))
    print(llist.get_nth_from_last_2pointer(4))
