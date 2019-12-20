import time

class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None

    def add_to_head(self, value):
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False
        # get a reference to the node we're currently at; update this as we traverse the list
        current = self.head
        # check to see if we're at a valid node 
        while current:
            # return True if the current value we're looking at matches our target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def reverse_list(self):
        # TO BE COMPLETED
        prev = None
        curr = self.head
        while curr is not None:
            next = curr.next_node
            curr.next_node = prev
            prev = curr
            curr = next
        self.head = prev

    def printLL(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next


start_time = time.time()

names_1 = LinkedList()
names_2 = LinkedList()

f = open('names_1.txt', 'r')
# names_1 = f.read().split("\n")  # List containing 10000 names
names_1.add_to_head(f.read())
f.close()

f = open('names_2.txt', 'r')
# names_2 = f.read().split("\n")  # List containing 10000 names
names_2.add_to_head(f.read())
f.close()

duplicates = LinkedList()
while names_1.head is not None:
    if names_1.contains(names_2.head):
        duplicates.add_to_head(names_2.head)
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
