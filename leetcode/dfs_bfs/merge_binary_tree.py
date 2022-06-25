# Definition for a binary tree node.
from turtle import right
from typing import List, Optional


class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

		
class Solution:
	def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
		if root1 is None:
			return root2
		elif root2 is None:
			return root1
		else:
			left = self.mergeTrees(root1=root1.left, root2=root2.left)
			right = self.mergeTrees(root1=root1.right, root2=root2.right)
			node = TreeNode(root1.val + root2.val, left, right)
			return node
