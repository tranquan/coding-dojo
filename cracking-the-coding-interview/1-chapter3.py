import os
import sys
import math


# 3.1 using single array to implement 3 stacks
# 1) - using 3 indexes to for each stack pointers, and 3 size to set maximum of stack
# 2) - using 3 indexes, 1 begin at the first index and increase, 1 begin at the bottom and decrease, 1 at the bottom and re-balanced every time
class ArrayStack:
  array = []
  stack_size = 0
  i1 = 0; i2 = 0; i3 = 0

  def __init__(self, size):
    self.stack_size = size
    self.i1 = 0
    self.i2 = 0 #self.stack_size
    self.i3 = 0 #self.stack_size * 2
    self.array = [0] * (self.stack_size * 3)

  def dump(self):
    print(self.array)

  def get_stack_index(self, stack):
    if stack == 0:
      return self.i1
    elif stack == 1:
      return self.i2
    elif stack == 2:
      return self.i3
    return -1

  def move_stack_pointer(self, stack, offset):
    if stack == 0:
      self.i1 += offset
    elif stack == 1:
      self.i2 += offset
    elif stack == 2:
      self.i3 += offset

  def push(self, stack, value):
    if stack < 0 or stack > 2: 
      return False

    index = self.get_stack_index(stack)
    if index < 0 or index >= self.stack_size:
      return False
    
    array_index = stack * self.stack_size + index
    self.array[array_index] = value
    self.move_stack_pointer(stack, 1)

  def pop(self, stack):
    if stack < 0 or stack > 2: 
      return False

    index = self.get_stack_index(stack)
    if index < 0 or index >= self.stack_size:
      return False
    
    array_index = stack * self.stack_size + index
    value = array[index]
    self.move_stack_pointer(stack, -1)

    return value

# Test
# stack = ArrayStack(10)
# stack.push(1, 10)
# stack.dump()

# 3.2 implement stack that support get min in O(1)
# -> stack still operate normally, 
# -> every node will have a next_min to point to another min when it removed
class MinNode:
  value = 0
  next_node = None
  next_min_node = None

  def __init__(self, value):
    self.value = value
    self.next_node = None
    self.next_min_node = None


class MinStack:
  root = None
  min_node = None

  def __init__(self):  
    self.root = None
  
  def push(self, value):
    if self.root == None:
      self.root = MinNode(value)
      self.min_node = self.root
    else:
      node = MinNode(value)
      node.next_node = self.root
      self.root = node
      if node.value < self.min_node.value:
        node.next_min_node = self.min_node
        self.min_node = node

  def pop(self):
    if self.root != None:
      node = self.root
      self.root = self.root.next_node
      if node == self.min_node:
        self.min_node = self.min_node.next_min_node
      return node.value

  def min(self):
    return self.min_node.value


# Test
# min_stack = MinStack()
# min_stack.push(10)
# min_stack.push(5)
# min_stack.push(12)
# min_stack.push(1)
# print(min_stack.min())
# min_stack.pop()
# print(min_stack.min())


# 3.3 Stack of Plates: combine many stack to create unlimitted stack
class SetStack:
  stacks = list()
  stack = None
  stack_size = 0

  def __init__(self, stack_size):
    self.stacks = list()
    self.stack_size = stack_size
    self.stack = list()
    self.stacks.append(self.stack)

  def dumpStack(self):
    for stack in self.stacks:
      print(stack)
  
  def push(self, value):
    if len(self.stack) >= self.stack_size:
      self.stack = list()
      self.stacks.append(self.stack)
    self.stack.append(value)

  def pop(self):
    if len(self.stack) == 0:
      if len(self.stacks) == 0:
        return None
      else:
        self.stack = self.stacks.pop()
        return self.stack.pop()
    else:
      return self.stack.pop()

  def popAt(self, stack_index):
    if stack_index < len(self.stacks):
      stack = self.stacks[stack_index]
      return stack.pop()
    else:
      return None


# Test
# stack = SetStack(3)
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)
# stack.push(5)
# stack.dumpStack()
# t = stack.popAt(0)
# print(t)


# 3.4 Using two queue to create a stack
# -> using list1 to push and list2 to pop
# -> when list2 is empty, get all data from list1 and push to iter
class MyQueue:
  lst1 = None
  lst2 = None

  def __init__(self):
    self.lst1 = list()
    self.lst2 = list()

  def add(self, value):
    self.lst1.append(value)

  def remove(self):
    if len(self.lst2) > 0:
      return self.lst2.pop()
    else:
      while len(self.lst1) > 0:
        value = self.lst1.pop()
        self.lst2.append(value)
      if len(self.lst2) > 0:
        return self.lst2.pop()
      else:
        return None 


# Test
# queue = MyQueue()
# queue.add(1)
# queue.add(2)
# queue.add(3)
# print(queue.remove())
# print(queue.remove())
# queue.add(4)
# queue.add(5)
# print(queue.remove())
# print(queue.remove())