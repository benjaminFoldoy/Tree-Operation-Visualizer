class Node:
  
  def __init__(self, value):
    self.value = value      #value can be any object, list, dict or type
    self.parent = None      #must be obect of class node
    self.leftChild = None   #must be obect of class node
    self.rightChild = None  #must be obect of class node

  def __repr__(self):
    return str(self.value)

  def __str__(self):
    return str(self.value)

  ###################################################################
  #                          PRINT TREE
  #
  #   Prints a shit string-representation of the tree.
  #   Man it's terrible...
  #
  ###################################################################
  def printTree(self):
    print("-"*self.getDepth() + str(self))
    if self.leftChild:
      self.leftChild.printTree()
    if self.rightChild:
      self.rightChild.printTree()

  ###################################################################
  #                 SET LEFT CHILD
  #
  #   Sets the left child to the given Node-object-argument. 
  #   Also sets that childs parent to self.
  #
  ###################################################################
  def setLeftChild(self, node):
    self.leftChild = node
    self.leftChild.parent = self

  ###################################################################
  #                 SET RIGHT CHILD
  #
  #   Sets the right child to the given Node-object-argument. 
  #   Also sets that childs parent to self.
  #
  ###################################################################
  def setRightChild(self, node):
    self.rightChild = node
    self.rightChild.parent = self

  ###################################################################
  #                      GET DEPTH
  #
  #   Returns the number of edges from the root 
  #   to the node that calls the method.
  #
  ###################################################################
  def getDepth(self, c = 0):
    if self.parent == None:
      return c
    return self.parent.getDepth(c + 1)
  
  ###################################################################
  #                   GET HEIGHT
  #
  #   Returns the number of edges from the node 
  #   to the deepest leaf.
  #
  ###################################################################
  def getHeight(self, highest = 0):
      l, r = 0, 0
      if self.leftChild:
        l = self.leftChild.getHeight(highest + 1)
      if self.rightChild:
        r = self.rightChild.getHeight(highest + 1)
      if l == r == 0:
        return highest
      if l >= r:
        return l
      elif l < r:
        return r



if __name__ == "__main__":
  console = Console()
  console.run()