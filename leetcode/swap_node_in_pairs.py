# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
		first = head
		second = first.next
		head = second
		prev = None
		while first is not None and second is not None:
			#print(f"{first.val}, {second.val}")
			third = second.next
			second.next = first
			first.next = third
			if prev is not None:
				prev.next = second
			prev = first
			first = third
			if third is not None:
				second = first.next
		return head


def createList(nums: List[int]) -> ListNode:
	head = None
	items = reversed(nums)
	for i in items:
		node = ListNode(i, None)
		if head is None:
			head = node
		else:
			node.next = head
			head = node
	return head


def printList(head: Optional[ListNode]):
	if head is None:
		print("None")
	else:
		node = head
		while node != None:
			print(f"{node.val}", end="->")
			node = node.next
		print("end")


def test():
	l = createList([1,2,3,4,5,6])
	# head = l
	# first = l
	# second = l.next
	# print(f"{first.val}, {second.val}, {third.val}")
	# third = second.next
	# second.next = first
	# first.next = third
	# first = third
	# second = first.next
	# print(f"{first.val}, {second.val}, {third.val}")
	s = Solution()
	r = s.swapPairs(l)
	printList(r)

test()
