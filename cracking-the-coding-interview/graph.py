# --------------------------------------------------
# Graph Node
# --------------------------------------------------
class GraphNode:
  value = 0
  adjancies = list()

  def __init__(self, value):
    self.value = value
    self.adjancies = list()

  def __str__(self):
     return str(self.value)


# --------------------------------------------------
# Graph
# --------------------------------------------------
class Graph:
  nodes = list()
  directed = True
  
  def __init__(self, total_nodes, directed):
    self.directed = directed
    i = 0
    while i < total_nodes:
      node = GraphNode(i)
      self.nodes.append(node)
      i += 1
      

  def dumpGraph(self):
    for node in self.nodes:
      adjancies = []
      for adj_node in node.adjancies:
        adjancies.append(adj_node.value)
      print(node.value, adjancies)


  def addConnection(self, node_index1, node_index2):
    if node_index1 >= len(self.nodes) or node_index2 >= len(self.nodes):
      message = "there are no node with input index: {} - {}".format(node_index1, node_index2)
      print(message)
      assert(False)
    else:
      node1 = self.nodes[node_index1]
      node2 = self.nodes[node_index2]
      if self.directed:
        node1.adjancies.append(node2)
      else:
        node1.adjancies.append(node2)
        node2.adjancies.append(node1)
    

# Test
# graph = Graph(4, True)
# graph.addConnection(0,1)
# graph.addConnection(0,2)
# graph.addConnection(1,2)
# graph.dumpGraph()