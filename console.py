from node import Node
from tree import TreeImage
from utilities import is_int


class Console:
  def __init__(self):
    self.root: Node = None
    self.running = True
  
  def run(self):
    while self.running:
      print(">   ", end="")
      value = input()
      
      if value == "exit":
        self.running = False
      
      if value.count("show") > 0:
        tree_image = TreeImage(self.root)
        tree_image.show()
        continue
      if value.count("save") > 0:
        tree_image = TreeImage(self.root)
        tree_image.save(value[4:].strip())
      
      if is_int(string = value): value = int(value)
      else: continue

      if self.root is None: 
        self.root = Node(value)
        continue
      
      current_node = self.root
      traversing = True

      while traversing:
        is_greater = True
        if current_node.value > value:
          is_greater = False
        
        if is_greater:
          if current_node.rightChild is None:
            current_node.setRightChild(Node(value))
            traversing = False
          else:
            current_node = current_node.rightChild
            continue
        else:
          if current_node.leftChild is None:
            current_node.setLeftChild(Node(value))
            traversing = False
          else:
            current_node = current_node.leftChild
            continue