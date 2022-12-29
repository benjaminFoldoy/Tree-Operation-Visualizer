from PIL import Image, ImageDraw, ImageFont
import random as r

class TreeImage:
  def __init__(self, tree, color = (255, 255, 255), backgroundColor = (40, 36, 35)):
    self.tree = tree
    self.color = color
    self.backgroundColor = backgroundColor
    self.margin = 100
    self.cellSize = (50, 100)
    self.graphSize = (
      self.cellSize[0] * (self.tree.getSize()[0]),
      self.cellSize[1] * (self.tree.getSize()[1])
      )
    self.img = Image.new(
      "RGB",
      (self.graphSize[0] + self.margin*2, self.graphSize[1] + self.margin*2),
      backgroundColor)
    self.imgDraw = ImageDraw.Draw(self.img)
  
  def drawEdges(self, node = None, start_crd = None):
    if node == None:
      node = self.tree
    if start_crd == None:
      start_crd = (self.graphSize[0]/2 + self.margin, self.margin)
    
    if node.leftChild is not None:
      newCrd = (
        start_crd[0] - self.graphSize[0]/(2**(node.getDepth() + 2)),
        start_crd[1] + self.cellSize[1]
        )
      self.imgDraw.line(
        [start_crd, newCrd], 
        fill = (self.color), width = 2
        )
      self.drawEdges(node.leftChild, (start_crd[0] - self.graphSize[0]/(2**(node.getDepth() + 2)), start_crd[1] + self.cellSize[1]))
    if node.rightChild is not None:
      newCrd = (
        start_crd[0] + self.graphSize[0]/(2**(node.getDepth() + 2)),
        start_crd[1] + self.cellSize[1]
        )
      self.imgDraw.line(
        [start_crd, newCrd], 
        fill = (self.color), width = 2
        )
      self.drawEdges(node.rightChild, (start_crd[0] + self.graphSize[0]/(2**(node.getDepth() + 2)), start_crd[1] + self.cellSize[1]))
  
  def drawAllVerticies(self, node = None, start_crd = None):
    if node == None:
      node = self.tree
    if start_crd == None:
      start_crd = (self.graphSize[0]/2 + self.margin, self.margin)
    
    self.drawVerticie(node.value, start_crd)
    
    if node.leftChild is not None:
      newCrd = (
        start_crd[0] - self.graphSize[0]/(2**(node.getDepth() + 2)),
        start_crd[1] + self.cellSize[1]
        )
      self.drawAllVerticies(node.leftChild, (start_crd[0] - self.graphSize[0]/(2**(node.getDepth() + 2)), start_crd[1] + self.cellSize[1]))
    if node.rightChild is not None:
      newCrd = (
        start_crd[0] + self.graphSize[0]/(2**(node.getDepth() + 2)),
        start_crd[1] + self.cellSize[1]
        )
      self.drawAllVerticies(node.rightChild, (start_crd[0] + self.graphSize[0]/(2**(node.getDepth() + 2)), start_crd[1] + self.cellSize[1]))
  
  def drawVerticie(self, value, crd):
    offset = self.cellSize[0]*1.4 / 2
    
    font = ImageFont.truetype("Assets/Fonts/Lato-Regular.ttf", 20) 
    self.imgDraw.ellipse((crd[0] - offset, crd[1] - offset, crd[0] + self.cellSize[0]*1.4 - offset, crd[1] + self.cellSize[0]*1.4 - offset), fill = self.backgroundColor, outline = self.color, width= 2)
    _, _, text_width, text_height = self.imgDraw.textbbox((0,0), str(value), font)
    
    text_pos = (
      crd[0] - text_width/2, #x crd of top left corner of text
      crd[1] - text_height/2, #y crd of top left corner of text
    )
    
    self.imgDraw.text(
      text_pos, 
      str(value), 
      font = font, 
      fill ="red", 
      align ="right"
    ) 

    
  def save(self, name = "untitled"):
    self.img.save(f"Assets/Images/{name}.png")
  
  #draws spesific node on spesific position
  def drawNode(self, pos, size):
    self.img

class Node:
  def __init__(self, value):
    self.value = value
    self.parent = None
    self.leftChild = None
    self.rightChild = None

  def __repr__(self):
    return str(self.value)

  def __str__(self):
    return str(self.value)

  def getSize(self):
    height = self.getHeight()
    width = self.n_horizontal_cells(height)
    return (width, height)

  def n_horizontal_cells(self, n):
    if n <= 0:
      return 1
    return self.n_horizontal_cells(n-1)*2 + 1

  def printTree(self):
    print("-"*self.getDepth() + str(self))
    if self.leftChild:
      self.leftChild.printTree()
    if self.rightChild:
      self.rightChild.printTree()

  def setLeftChild(self, node):
    self.leftChild = node
    self.leftChild.parent = self

  def setRightChild(self, node):
    self.rightChild = node
    self.rightChild.parent = self

  def getDepth(self, c = 0):
    if self.parent == None:
      return c
    return self.parent.getDepth(c + 1)
  
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
  node = Node(10)
  node.setLeftChild(Node(2))
  node.setRightChild(Node(5))
  node.leftChild.setLeftChild(Node(6))
  node.leftChild.setRightChild(Node(69))
  node.leftChild.leftChild.setRightChild(Node(4))
  node.leftChild.rightChild.setLeftChild(Node(55))
  node.leftChild.rightChild.setRightChild(Node(35))
  node.leftChild.rightChild.rightChild.setRightChild(Node(15))
  node.leftChild.rightChild.rightChild.rightChild.setRightChild(Node(53))
  ti = TreeImage(node)
  print(ti.tree.getSize())
  ti.drawEdges()
  ti.drawAllVerticies()
  ti.save()