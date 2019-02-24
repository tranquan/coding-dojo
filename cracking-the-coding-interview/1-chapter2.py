import os
import sys
import math

from linked_list import Node, LinkedList

# --------------------------------------------------
# WORKS
# --------------------------------------------------
# 2.1 remove dup
def remove_dup(linked_list):
  check = {}
  prev = None
  cur = linked_list.head
  while cur != None:
    if cur.data in check:
      next_node = cur.p_next
      linked_list.remove_node(prev, cur)
      cur = next_node
    else:
      check[cur.data] = True
      prev = cur
      cur = cur.p_next

# l1 = LinkedList.init_from_arr([1,2,3,4,5,2,5])
# l1.dump()
# remove_dup(l1)
# l1.dump()

# 2.2 remove dup without temp memory
def remove_dup_without_temp(linked_list):
  if linked_list.head == None or linked_list.head.p_next == None:
    return
  
  node = linked_list.head
  while node.p_next != None:
    prev = node
    cur = node.p_next
    
    while cur != None:
      if cur.data == node.data:
        cur_next = cur.p_next
        linked_list.remove_node(prev, cur)
        cur = cur_next        
      else:
        prev = cur
        cur = cur.p_next
    
    node = node.p_next
    if node == None:
      break

# l1 = LinkedList.init_from_arr([1,2,3,4,5,2,5])
# l1.dump()
# remove_dup_without_temp(l1)
# l1.dump()

# 2.3 get kth last
def get_node_from_backward(linked_list, kth):
  if linked_list.head == None: return None
  
  n = 0
  cur = linked_list.head
  while cur != None:
    n+=1
    cur = cur.p_next

  nth = n - 1 - kth
  if nth < 0: return None

  cur = linked_list.head
  nth -= 1
  while nth >= 0:
    nth -= 1
    cur = cur.p_next
  
  return cur

# l1 = LinkedList.init_from_arr([1,2,3,4,5,2,5])
# node = get_node_from_backward(l1, 3)
# print(node.data)

# 2.3 delete middle node
def remove_middle_node(linked_list, node):
  prev = None
  cur = linked_list.head
  while cur != None and cur != node:
    prev = cur
    cur = cur.p_next
  if cur != None:
    linked_list.remove_node(prev, cur)

# l1 = LinkedList.init_from_arr([1,2,3,4,5,2,5])
# node = get_node_from_backward(l1, 3)
# remove_middle_node(l1, node)
# l1.dump()

# 2.4 partition, modify the list so that all nodes less then medium is on the left of medium

def partition_list(linked_list, medium):
  if linked_list.head == None or linked_list.head.p_next == None: 
    return
  
  prev = None
  cur = linked_list.head

  while cur != None:
    if cur.data < medium:
      cur_next = cur.p_next
      linked_list.remove_node(prev, cur)
      linked_list.insert_at_head(cur)
      cur = cur_next
    else:
      prev = cur
      cur = cur.p_next

# l1 = LinkedList.init_from_arr([3,5,8,5,10,2,1])
# partition_list(l1, 5)
# l1.dump()

# 2.5 sum simulator
def sum_linked_list(linked_list1, linked_list2):
  if linked_list1.head == None and linked_list2.head == None:
    return LinkedList.init_from_arr[0]
  if linked_list1.head == None:
    return linked_list2
  if linked_list2.head == None:
    return linked_list1
    
  result = LinkedList()
  p1 = linked_list1.head
  p2 = linked_list2.head
  
  redundance = 0
  while p1 != None or p2 != None:
    s1 = 0
    s2 = 0
    
    if p1 != None:
      s1 = p1.data
      p1 = p1.p_next
    
    if p2 != None:
      s2 = p2.data
      p2 = p2.p_next
    
    ss = s1 + s2 + redundance
    redundance = 0
    if ss >= 10:
      redundance = ss / 10
      ss = ss % 10
    result.append(Node(ss))
  
  if redundance > 0:
    result.append(Node(redundance))
  
  return result
  
# l1 = LinkedList.init_from_arr([7,1,6,2])
# l2 = LinkedList.init_from_arr([5,9,2])
# l3 = sum_linked_list(l1, l2)
# l3.dump()


