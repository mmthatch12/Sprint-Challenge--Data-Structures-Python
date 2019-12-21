import time

class BinarySearchTree:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value >= self.value and self.right is None:
            self.right = BinarySearchTree(value)
        elif value >= self.value and self.right is not None:
            self.right.insert(value)
        elif value < self.value and self.left is None:
            self.left = BinarySearchTree(value)
        elif value < self.value and self.left is not None:
            self.left.insert(value)

    def contains(self, target, new_bst=None):
        if target is self.value:
            new_bst.insert(target)
            return True
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        elif target >= self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    def in_order_print(self, node):
        if self is None:
            return
        if self is not None:
            if self.left:
                self.left.in_order_print(self)
            if self.right:
                self.right.in_order_print(self)

start_time = time.time()

names_1 = BinarySearchTree('start')
names_2 = BinarySearchTree('start1')

f = open('names_1.txt', 'r')
names_1.insert(f.read()) #f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2.insert(f.read())  #.split("\n")  # List containing 10000 names
f.close()

duplicates = BinarySearchTree('st')

names_1.contains(names_2.in_order_print(names_2))
duplicates = []
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
