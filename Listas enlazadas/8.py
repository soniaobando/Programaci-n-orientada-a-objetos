class RealNumberList:
    def __init__(self):
        self.head = None

    def add_number(self, number):
        new_node = Node(number)
        new_node.next = self.head
        self.head = new_node

    def calculate_average(self):
        total, count = 0, 0
        current = self.head
        while current:
            total += current.data
            count += 1
            current = current.next
        return total / count if count > 0 else 0

    def divide_by_average(self, average):
        less_or_equal = LinkedList()
        greater = LinkedList()
        current = self.head
        while current:
            if current.data <= average:
                less_or_equal.add_number(current.data)
            else:
                greater.add_number(current.data)
            current = current.next
        return less_or_equal, greater
