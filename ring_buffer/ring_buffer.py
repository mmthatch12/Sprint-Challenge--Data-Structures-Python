from doubly_linked_list import DoublyLinkedList
from doubly_linked_list import ListNode


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length >= self.capacity:
            self.storage.remove_from_head()
            self.storage.add_to_head(item)
        elif self.storage.length < self.capacity:
            self.storage.add_to_tail(item)



    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        temp = self.storage.head
        # TODO: Your code here
        while temp:
            list_buffer_contents.append(temp.value)
            temp = temp.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
