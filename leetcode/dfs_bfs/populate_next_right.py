from typing import Optional


class Node:
	def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
		self.val = val
		self.left = left
		self.right = right
		self.next = next


'''
convert tree into array, next right node is the next node in array
'''
class Solution:
	def connect(self, root: Optional[Node]) -> Optional[Node]:
		if root is None:
			return root

		queue = [root]
		nodes = []
		
		while len(queue) > 0:
			node = queue.pop()
			nodes.append(node)
			if node.left is not None:
				nodes.insert(0, node.left)
			if node.right is not None:
				nodes.insert(0, node.right)
		
		for i in range(0, len(nodes)-1):
			nodes[i].next = nodes[i+1]

		for i in range(1, len(nodes)):
			ii = pow(2, i) - 2
			if ii >= len(nodes):
				break
			nodes[ii].next = None

