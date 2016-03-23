#Python二叉树类的实现
class BinaryTree(object):
	#初始化二叉树节点信息
	def __init__(self, item):
		self.key = item
		self.leftChild = None
		self.rightChild = None

	#插入左孩子节点
	def insertLeft(self, item):
		if not self.leftChild:
			self.leftChild = BinaryTree(item)
		else:
			tmp = self.BinaryTree(item)
			tmp.leftChild, self.leftChild = self.leftChild, tmp

	#插入右孩子节点
	def insertRight(self, item):
		if not self.rightChild:
			self.rightChild = BinaryTree(item)
		else:
			tmp = self.BinaryTree(item)
			tmp.rightChild, self.rightChild = self.rightChild, tmp

