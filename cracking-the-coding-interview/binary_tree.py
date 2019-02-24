import math

# --------------------------------------------------
# Binary Tree Node
# --------------------------------------------------
class BinaryTreeNode:
  value = 0
  left = None
  right = None
  parent = None

  def __init__(self, value):
    self.value = value

# --------------------------------------------------
# Binary Tree
# --------------------------------------------------
class BinaryTree:
  root = None

  def __init__(self):
    self.root = None

  
  def inOrderTravelsal(self):
    if self.root == None:
      print("tree is empty")
    else:
      self._inOrderTravelsal(self.root)

  def _inOrderTravelsal(self, node):
    if node == None: 
      return
    self._inOrderTravelsal(node.left)
    print(node.value)
    self._inOrderTravelsal(node.right)

  
  def preOrderTravelsal(self):
    if self.root == None:
      print("tree is empty")
    else:
      self._preOrderTravelsal(self.root)

  def _preOrderTravelsal(self, node):
    if node == None: 
      return
    print(node.value)
    self._preOrderTravelsal(node.left)
    self._preOrderTravelsal(node.right)


  def findNonFullNode(self):
    if self.root == None:
      return None
    else:
      queue = list()
      queue.insert(0, self.root)
      parent = None
      while len(queue) > 0:
        node = queue.pop()
        if node.left == None or node.right == None:
          parent = node
          break
        else:
          if node.left != None:
            queue.insert(0, node.left)
          if node.right != None:
            queue.insert(0, node.right)
      return parent


  def getDepth(self):
    return self._getDepth(self.root)

  def _getDepth(self, node):
    if node == None:
      return 0
    if node.left == None and node.right == None:
      return 1
    d_left = self._getDepth(node.left)
    d_right = self._getDepth(node.right)
    return max(d_left, d_right) + 1


  def append(self, value):
    node = BinaryTreeNode(value)
    parent = self.findNonFullNode()
    if parent == None:
      self.root = node
    else:
      node.parent = parent
      if parent.left == None:
        parent.left = node
      else:
        parent.right = node
      

# --------------------------------------------------
# Binary Search Tree
# --------------------------------------------------
class BinarySearchTree(BinaryTree):
  root = None

  def __init__(self):
    self.root = None

  
  def append(self, value):
    parent = None
    node = self.root
    direction = 0
    while node != None:
      parent = node
      if value < node.value:
        node = node.left
        direction = -1
      else:
        node = node.right
        direction = 1
    
    node = BinaryTreeNode(value)
    if parent == None:
      self.root = node
    else:
      node.parent = parent
      if direction == -1:
        parent.left = node
      else:
        parent.right = node


# Test
# array = [10, 5, 4, 6, 15, 12, 20]
# tree = BinarySearchTree()
# for v in array:
#   tree.append(v)
# tree.inOrderTravelsal()