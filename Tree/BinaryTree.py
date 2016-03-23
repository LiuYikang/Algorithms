#Python Binary Tree
class BinaryTree(object):
    #init Binary Tree Node
    def __init__(self, item):
        self.key = item
        self.leftChild = None
        self.rightChild = None

    #Insert left child node
    def insertLeft(self, item):
        if not self.leftChild:
            self.leftChild = BinaryTree(item)
        else:
            tmp = self.BinaryTree(item)
            tmp.leftChild, self.leftChild = self.leftChild, tmp

    #Insert right child node
    def insertRight(self, item):
        if not self.rightChild:
            self.rightChild = BinaryTree(item)
        else:
            tmp = self.BinaryTree(item)
            tmp.rightChild, self.rightChild = self.rightChild, tmp
