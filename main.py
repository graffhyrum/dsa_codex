from algorithms.sort import quicksort, mergesort
from data_structures import stack, queue


def main():
    # Demonstrate stack functionality
    s = stack.Stack()
    s.push(1)
    s.push(2)
    print(s.pop())  # Should print 2

    # Demonstrate queue functionality
    q = queue.Queue()
    q.enqueue(1)
    q.enqueue(2)
    print(q.dequeue())  # Should print 1

    # Demonstrate quicksort functionality
    arr = [3, 6, 8, 10, 1, 2, 1]
    sorted_arr = quicksort.quicksort(arr)
    print(sorted_arr)  # Should print [1, 1, 2, 3, 6, 8, 10]

    # Demonstrate mergesort functionality
    arr = [3, 6, 8, 10, 1, 2, 1]
    sorted_arr = mergesort.mergesort(arr)
    print(sorted_arr)  # Should print [1, 1, 2, 3, 6, 8, 10]


if __name__ == "__main__":
    main()
