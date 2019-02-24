import os
import sys
import math

from binary_tree import BinaryTreeNode, BinaryTree, BinarySearchTree
from graph import GraphNode, Graph

# 4.1 check route between 2 nodes in a directed graph
# -> how the graph was structure? adjancy vertices or adjancy matrix
# -> using bfs from node1 to node2
def isRouteExits(graph, node1_index, node2_index):
  
  isExists = False
  node1 = graph.nodes[node1_index]
  node2 = graph.nodes[node2_index]
  
  queue = list()
  queue.append(node1)
  node = None

  while len(queue) > 0:
    node = queue.pop()
    if node == node2:
      isExists = True
      break
    else:
      for adj_node in node.adjancies:
        queue.insert(0, adj_node)

  return isExists
        

# Test
# graph = Graph(4, True)
# graph.addConnection(0,1)
# graph.addConnection(0,2)
# graph.addConnection(1,3)
# t = isRouteExits(graph, 1, 2)
# print(t)

# 4.2 create a minimal binary search tree with minimal height from a sorted list
def createBinarySearchTreeFromArray(array):
  tree = BinarySearchTree()
  appendNodeFromArray(tree, array, 0, len(array)-1)
  return tree

def appendNodeFromArray(tree, array, low, high):
  if low > high:
    return
  if low == high:
    tree.append(array[low])
  else:
    mid = int((high-low)/2) + low
    tree.append(array[mid])
    appendNodeFromArray(tree, array, low, mid-1)
    appendNodeFromArray(tree, array, mid+1, high)


# Test
# array = [4,5,6,10,12,15,20]

# btree = BinarySearchTree()
# for v in array:
#   btree.append(v)
# btree.preOrderTravelsal()

# bstree = createBinarySearchTreeFromArray(array)
# bstree.preOrderTravelsal()


# 4.3 form linked list at each depth
# -> using bfs to travel the tree, combine with a queue_depth to know what linked list should be put
def getDepthLinkedListOfTree(tree):
  if tree.root == None:
    return []

  depths = list()
  depth = tree.getDepth()
  for i in range(0, depth):
    depths.append(list())
  
  queue = list()
  queue_depth = list()
  queue.insert(0, tree.root)
  queue_depth.insert(0, 0)
  
  while len(queue) > 0:
    node = queue.pop()
    depth = queue_depth.pop()
    lst = depths[depth]
    lst.insert(0, node.value)
    if node.left != None:
      queue.insert(0, node.left)
      queue_depth.insert(0, depth+1)
    if node.right != None:
      queue.insert(0, node.right)
      queue_depth.insert(0, depth+1)
  
  return depths


# Test
# array = [1,2,3,4,5,6]
# tree = BinaryTree()
# for v in array:
#   tree.append(v)
# depths = getDepthLinkedListOfTree(tree)
# for lst in depths:
#   print(lst)


# 4.4 check balance - which 2 branch of node not diff more than 1
def isTreeBalanced(tree):
  if tree.root == None:
    return True
  d_left = getDepth(tree.root.left)
  d_right = getDepth(tree.root.right)
  if abs(d_left - d_right) >= 2:
    return False
  return True

def getDepth(node):
  if node == None:
    return 0
  d_left = getDepth(node.left)
  d_right = getDepth(node.right)
  return max(d_left, d_right)+1

# Test
# array = [5,2,3,1,7]
# tree = BinarySearchTree()
# for v in array:
#   tree.append(v)
# t = isTreeBalanced(tree)
# print(t)


# 4.5 check binary search tree - which left <= node <= right
def isBinarySearchTree(tree):
  if tree.root == None:
    return True
  
  queue = list()
  queue.insert(0, tree.root)
  
  while len(queue) > 0:
    node = queue.pop()
    
    if node.left != None:
      if node.left.value > node.value:
        return False
      else:
        queue.insert(0, node.left)

    if node.right != None:
      if node.right.value < node.value:
        return False
      else:
        queue.insert(0, node.right)

  return True
      
      
# Test
# array = [5, 3, 7, 2, 4, 6, 8]
# tree = BinaryTree()
# for v in array:
#   tree.append(v)
# depths = getDepthLinkedListOfTree(tree)
# for lst in depths:
#   print(lst)
# t = isBinarySearchTree(tree)
# print(t)