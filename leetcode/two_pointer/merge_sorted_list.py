# Definition for singly-linked list.
from heapq import merge
from typing import Optional


class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


'''
Problem: 
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Solution:
- Create two pointes, which smaller will go first
- Do it till both lists are None
'''
class Solution:
	def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
		merged = None
		r = merged
		p1 = list1
		p2 = list2
		while p1 is not None or (p2 is not None and p1.val > p2.val):
			node = p1
			if p1 is None or p1.val > p2.val:
				node = p2
				p2 = p2.next
			else:
				p1 = p1.next
			if merged is None:
				merged = node
				r = merged
			else:
				merged.next = node
				merged = merged.next
		return r
