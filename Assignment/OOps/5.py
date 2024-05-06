# Write a Python program to create a class representing a binary 
# search tree. Include methods for inserting and searching for 
# elements in the binary tree.

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursively(self.root, key)

    def _insert_recursively(self, root, key):
        if root is None:
            return TreeNode(key)
        if key < root.key:
            root.left = self._insert_recursively(root.left, key)
        elif key > root.key:
            root.right = self._insert_recursively(root.right, key)
        return root

    def search(self, key):
        return self._search_recursively(self.root, key)

    def _search_recursively(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._search_recursively(root.left, key)
        return self._search_recursively(root.right, key)


bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

print("Searching for 5:", bst.search(5) is not None)
print("Searching for 9:", bst.search(9) is not None)
