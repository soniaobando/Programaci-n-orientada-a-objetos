class LinkedListComparator:
    def __init__(self):
        self.head = None

    def add_number(self, number):
        new_node = Node(number)
        new_node.next = self.head
        self.head = new_node

    def compare_lists(self, other_list):
        current1 = self.head
        current2 = other_list.head

        while current1 and current2:
            if current1.data != current2.data:
                return "Las listas son iguales en tamaño, pero no en contenido."
            current1 = current1.next
            current2 = current2.next

        if current1 or current2:
            return "Las listas no tienen el mismo tamaño ni contenido."
        return "Las listas son iguales en tamaño y contenido."
