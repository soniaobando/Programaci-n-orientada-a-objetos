class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def count_elements(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
