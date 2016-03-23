import BinaryTree


#create binary tree
def CreateBinaryTree():
    a = raw_input("enter a key: ")
    #if enter '#', create empty node
    root = None
    if a is '#':
        return root
    else:
        root = BinaryTree.BinaryTree(a)
        root.leftChild = CreateBinaryTree()
        root.rightChild = CreateBinaryTree()
    return root
