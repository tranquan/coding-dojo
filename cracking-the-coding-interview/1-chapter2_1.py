import os
import sys
import math

from linked_list import Node, LinkedList

# 2.6 check if linked list is palindrome
# -> 1: using a stack and travel to half of list, then begin compare
# -> 2: using a nother linked list
def is_palindrome(linked_list):
  if linked_list.head == None or linked_list.head.p_next == None:
    return True
  
  length = linked_list.length()
  if length % 2 == 1:
    should_skip_middle = True
  else:
    should_skip_middle = False
  
  n = length / 2
  cur = linked_list.head
  first_half = LinkedList()
  first_half_cur = None
  
  while cur != None:
    if n > 0:
      first_half.insert_at_head(Node(cur.data))
      n -= 1
      cur = cur.p_next
    else:
      if should_skip_middle:
        cur = cur.p_next
        should_skip_middle = False
      else:
        if first_half_cur == None:
          first_half.dump()
          first_half_cur = first_half.head
        if cur.data != first_half_cur.data:
          return False
        cur = cur.p_next
        first_half_cur = first_half_cur.p_next
    
  return True

def is_palindrome1(linked_list):
  if linked_list.head == None or linked_list.head.p_next == None:
    return True
  
  reversed_list = linked_list.reverse()
  length = linked_list.length()
  n = length/2
  p1 = linked_list.head
  p2 = reversed_list.head
  while n > 0:
    if p1.data != p2.data:
      return False
    n -= 1
    p1 = p1.p_next
    p2 = p2.p_next
    
  return True


# l1 = LinkedList.init_from_arr([1,2,3,4,3,2,1])
# t = is_palindrome1(l1)
# print(t)


# 2.7 intersection 
# -> put node address in a check list and compare
# ? cannot put the same node in two list since the p_next will be affect
def get_intersection(linked_list1, linked_list2):
  
  check = {}
  cur = linked_list1.head
  while cur != None:
    check[id(cur)] = True
    cur = cur.p_next
  
  intersect = LinkedList()

  cur = linked_list2.head
  while cur != None:
    if id(cur) in check:
      intersect.append(cur)
    cur = cur.p_next

  return intersect

# n1 = Node(1)
# n2 = Node(2)
# n3 = Node(3)
# n4 = Node(4)
# n5 = Node(5)
# n6 = Node(6)

# l1 = LinkedList()
# l1.append(n1)
# l1.append(n2)
# l1.append(n4)
# l1.append(n5)
# l1.dump()

# l2 = LinkedList()
# l2.append(n3)
# l2.append(n6)
# l2.dump()

# l3 = get_intersection(l1, l2)
# l3.dump()

# 2.8 loop detection
def find_loop(linked_list):
  if linked_list.head == None or linked_list.head.p_next == None:
    return None
  
  loop_data = None
  check = {}
  cur = linked_list.head
  while cur != None:
    if cur.data in check:
      loop_data = cur.data
      break
    else:
      check[cur.data] = True
    cur = cur.p_next

  if loop_data != None:
    cur = linked_list.head
    while cur != None:
      if cur.data == loop_data:
        return cur
      cur = cur.p_next

  return None


l1 = LinkedList.init_from_arr([1,2,3,4,5,6,3])
node = find_loop(l1)
print(node.data)