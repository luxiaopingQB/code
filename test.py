###链表

class Node(): 
##链表节点结构
	def __init__(self,item=None,pos_item=None):
		self._item=item
		self._next=pos_item
	def __repr__(self):
		return str(self._item)