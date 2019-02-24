# --------------------------------------------------
# Linked List
# --------------------------------------------------
class Node:
  data = 0
  p_next = None


  def __init__(self, data=0, p_next=None):
    self.data = data
    self.p_next = p_next


class LinkedList:
  head = None

  def __init__(self, head=None):
    self.head = head

  @classmethod
  def init_from_arr(self, arr):
    self = LinkedList()
    for i in range(0, len(arr)):
      node = Node(arr[i])
      self.append(node)
    return self


  def dump(self):
    if self.head == None:
      print "Empty"

    head = self.head
    dump = ""

    while head != None:
      dump += str(head.data)
      if head.p_next != None:
        dump += "->"
      else:
        dump += "->None"
      head = head.p_next
    print(dump)


  def length(self):
    n = 0
    cur = self.head
    while cur != None:
      n += 1
      cur = cur.p_next
    return n

  def append(self, node):
    if node == None: return

    cur = self.head
    if cur == None:
      self.head = node
    else:
      while cur.p_next != None:
        cur = cur.p_next
      cur.p_next = node
  
  def insert_at_head(self, node):
    if node == None: return

    new_node = Node(node.data)
    cur = self.head
    new_node.p_next = cur
    self.head = new_node

  
  def remove_node(self, prev, node):
    if node == None: return
    
    if node == self.head:
      self.head = node.p_next
    else:
      prev.p_next = node.p_next


  def reverse(self):
    if self.head == None or self.head.p_next == None:
      return self
    
    prev = None
    cur = self.head
    reverse_list = LinkedList()
    
    while cur != None:
      reverse_list.insert_at_head(cur)
      cur = cur.p_next
    
    return reverse_list

  
  def reverse_in_place(self):
    if self.head == None or self.head.p_next == None:
      return
    
    prev = None
    cur = self.head

    while cur.p_next != None:
      cur_next = cur.p_next
      cur.p_next = prev
      prev = cur
      cur = cur_next
    
    cur.p_next = prev
    self.head = cur


# --------------------------------------------------
# TEST
# --------------------------------------------------

# list0 = LinkedList()
# list0.append(Node(0))
# list0.append(Node(1))
# list0.dump()

# list1 = LinkedList.init_from_arr([])
# list1.dump()

# list2 = LinkedList.init_from_arr([1,2,3,4,5])
# list2.dump()
# list3 = list2.reverse()
# list3.dump()

# node2 = list2.head.p_next.p_next
# node3 = list2.head.p_next.p_next.p_next
# list2.remove_node(node2, node3)
# list2.dump()

# list2.reverse_in_place()
# list2.dump()