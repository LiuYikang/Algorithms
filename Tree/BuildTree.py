import BinaryTree

#创建二叉树
def CreateBinaryTree(root):
	a = row_input("enter a key: ")
	#如果输入的是#，则创建空节点
	if a is '#':
		root = None
