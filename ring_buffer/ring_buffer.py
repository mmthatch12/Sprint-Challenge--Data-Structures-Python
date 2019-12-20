from doubly_linked_list import DoublyLinkedList
from doubly_linked_list import ListNode


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        self.size = 0

    def append(self, item):
        if self.size >= self.capacity:
            self.storage.tail = ListNode(item, None, None)
        elif self.size < self.capacity:
            self.storage.add_to_head(item)
            self.size += 1


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
