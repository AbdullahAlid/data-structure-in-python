class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        temp = self.root
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return True
        else:
            while temp:
                if value == temp.value:
                    return False
                if value > temp.value:
                    if temp.right:
                        temp = temp.right
                    else:
                        temp.right = new_node
                        return True
                else:
                    if temp.left:
                        temp = temp.left
                    else:
                        temp.left = new_node
                        return True

    def contains(self, value):
        if self.root == None:
            return False
        temp = self.root
        while temp:
            if temp.value == value:
                return True
            temp = temp.left if value < temp.value else temp.right
        return False


bst = BinarySearchTree()
bst.insert(5)
bst.insert(7)
bst.insert(9)
bst.insert(3)
bst.insert(7)
print(bst.root.left.value)
print(bst.contains(3))
