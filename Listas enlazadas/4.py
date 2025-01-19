import random

    def generate_random_list(self, n=50, min_val=1, max_val=999):
        for _ in range(n):
            self.insert_end(random.randint(min_val, max_val))

    def remove_out_of_range(self, min_val, max_val):
        current = self.head
        prev = None
        while current:
            if current.data < min_val or current.data > max_val:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
            else:
                prev = current
            current = current.next
