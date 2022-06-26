# Definition for singly-linked list.
from typing import Optional


class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


'''
Problem:
Given the head of a singly linked list, reverse the list, and return the reversed list.

Solution:
- using two pointer
'''
class Solution:
	def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
		cur = head
		next = None
		if cur is not None:
			next = cur.next
			cur.next = None
		while next is not None:
			next_next = next.next
			next.next = cur
			cur = next
			next = next_next
		return cur
