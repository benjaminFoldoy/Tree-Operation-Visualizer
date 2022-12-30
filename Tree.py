from PIL import Image, ImageDraw, ImageFont
import random as r


###################################################################
#                   CLASS: TREE IMAGE
#
#   Objects of this class will be able to create an image
#   visualizing a binary tree. 
# 
#   To initialize a TreeImage-object, needs a Node-object 
#   as agrument.
#
#   To 
###################################################################

class TreeImage:
  def __init__(self, root, color = (255, 255, 255), backgroundColor = (40, 36, 35)):
    ###################################################################
    #                   COLORS OF THE IMAGE
    #
    #   Colors is a tuple: (R, G, B)
    #   where R, G and B is of type int between 0-255.
    #       
    #   The image produced is composed of two colors:
    #     self.color 
    #       - the format of self.color is a tuple: (R, G, B)
    #         where R, G and B is of type int between 0-255.
    #       - this color applies to the node's value color, 
    #         outline color and the color that connects each node.
    #
    #     self.backgroundColor
    #       - this color applies to the node's value color, 
    #         outline color and the color that connects each node
    #
    ###################################################################

    self.color = color                       #rgb format: (int, int, int)
    self.backgroundColor = backgroundColor   #rgb format: (int, int, int)
    
    ###################################################################
    #                              ROOT
    #
    #   Root refers to the top branch of the tree.
    #
    #   self.root is an object of the class Node.
    #
    ###################################################################
    
    self.root = root                         #root of tree
    
    ###################################################################
    #             IMAGE CREATION AND CONFIGURATION
    #
    #   As an abstraction, the tree will be devided into a grid.
    #
    #   A full tree would look like this (height of 2)
    #   ---O---     "O" is a cell filled with a node
    #   -O---O-     "-"" is an emty cell
    #   O-O-O-O
    #   
    #   With the abstraction in mind:
    #     
    #     self.cellSize:
    #       - Format: (width, height) where width and height 
    #         are both of type int.
    #       - The width and height of each cell in pixles.
    #
    #     self.graphSize:
    #       - Format: (width, height) where width and height 
    #         are both of type int.
    #       - The width and height of the whole tree, in pixles.
    #
    #     self.margin:
    #       - Of type int.
    #       - The margin of pixles on each side of the graph. 
    #         Without this margin, the top of the tree would 
    #         begin at the top first pixel, which looks shit.
    #
    #     self.img:
    #       - Of type Image
    #       - The image object to be drawn and saved.
    #
    #     self.imgDraw:
    #       - An object that uses self.img and draws on it.
    #
    ###################################################################
    
    self.cellSize = (100, 200)               #tree is devided into 
    self.graphSize = (
      self.cellSize[0] * (self.getGridSize(root)[0]),
      self.cellSize[1] * (self.getGridSize(root)[1])
      )
    self.margin = self.cellSize[1] * 1
    self.img = Image.new(
      "RGB",
      (self.graphSize[0] + self.margin*2, self.graphSize[1] + self.margin*2),
      backgroundColor)
    self.imgDraw = ImageDraw.Draw(self.img)
  
  ###################################################################
  #                         SAVE IMAGE
  #
  #   Function to construct- and save image of tree. 
  #
  #   Will be saved in the Assets/Images folder as *NAME*.png
  #   where name is an argument.
  #
  #   If no name is supplied, will be called untitled.png.
  #
  ###################################################################

  def save(self, name = "untitled"):
    self.drawEdges()
    self.drawAllNodes()
    self.img.save(f"Assets/Images/{name}.png") #saving image
  
  ###################################################################
  #                       SHOW IMAGE
  #
  #   Function co construct- and show image of tree.
  #
  ###################################################################
  def show(self):
    self.drawEdges()
    self.drawAllNodes()
    self.img.show()
  
  ###################################################################
  #                       DRAW EDGES FUNCTION
  #
  #   Draws the lines between the nodes.
  #
  #   Function is recursive. Going from the root node, and downward
  #   first on the left side, and then on the right.
  #
  #   Parameters:
  #
  #     node:
  #       - Object of class Node.
  #       - The first time this recursive function is called 
  #         (without arguments), node will become 
  #         the root of self.tree.
  #
  #     start_crd:
  #       - Format: (x_crd, y_crd) where 
  #         x_crd and y_crd are of type int.
  #       - The first time this recursive function is called
  #         (without arguments), start_crd becomes the top 
  #         center of the image.
  #
  ###################################################################
  
  def drawEdges(self, node = None, start_crd = None):
    if node == None:
      node = self.root
    if start_crd == None:
      start_crd = (self.graphSize[0]/2 + self.margin, self.margin)
    
    if node.leftChild is not None: #ABS: if node has left child.
      newCrd = ( #tthe endpoint of the line to be drawn.
        start_crd[0] - self.graphSize[0]/(2**(node.getDepth() + 2)),
        start_crd[1] + self.cellSize[1]
        )
      self.imgDraw.line(
        [start_crd, newCrd],  #draw line from start_crd to newCrd.
        fill = (self.color),  #color of line.
        width = 2             #width of line.
        )
      self.drawEdges( #function is calling itself.
        node.leftChild, #with its left child as the node argument.
        (
          #new x_crd is half of the width of the left child's tree.
          start_crd[0] - self.graphSize[0]/(2**(node.getDepth() + 2)),
          #new y_crd is one cellheight down from current y_crd.
          start_crd[1] + self.cellSize[1]
        )
      )
    if node.rightChild is not None: #ABS: if node has right child.
      newCrd = ( #the endpoint of the line to be drawn.
        start_crd[0] + self.graphSize[0]/(2**(node.getDepth() + 2)),
        start_crd[1] + self.cellSize[1]
        )
      self.imgDraw.line(
        [start_crd, newCrd],  #draw line from start_crd to newCrd.
        fill = (self.color),  #color of line.
        width = 2             #width of line
        )
      self.drawEdges( #function is calling it self...
        node.rightChild,  #with its right child as the node argument
        (
          #new x_crd is half of the width of the right child's tree.
          start_crd[0] + self.graphSize[0]/(2**(node.getDepth() + 2)), 
          #new y_crd is one cellheight down from current y_crd.
          start_crd[1] + self.cellSize[1]
        )
      )
  
  ###################################################################
  #                       DRAW ALL NODES
  #
  #   Draws all nodes of the graph recurcivly, as circles with their 
  #   corresponding value in the center of the circle.
  #
  #   
  ###################################################################
  
  def drawAllNodes(self, node = None, crd = None):
    if node == None:
      node = self.root
    if crd == None:
      crd = (self.graphSize[0]/2 + self.margin, self.margin)
    
    #draws node with it's value at it's crd.
    self.drawNode(node.value, crd)
    
    if node.leftChild is not None:  #ABS: if node has left child...
      self.drawAllNodes(        #...calls itself...
        node.leftChild,             #...with it's left child as node argument...
        (
          #...and new x_crd, half of the with of its childrends trees...
          crd[0] - self.graphSize[0]/(2**(node.getDepth() + 2)),
          #...and y_crd is one cellheight down from its current y_crd.
          crd[1] + self.cellSize[1]
        )
      )
    if node.rightChild is not None: #ABS: if node has right child...
      self.drawAllNodes(        #...calls itself...
        node.rightChild,            #...with it's right child as node argument...
        (
          #...and new x_crd, half of the with of its childrends trees...
          crd[0] + self.graphSize[0]/(2**(node.getDepth() + 2)), 
          #...and y_crd is one cellheight down from its current y_crd.
          crd[1] + self.cellSize[1]
        )
      )
  
  ###################################################################
  #                          DRAW NODE
  #
  #   Draws a circle at specific crd, with a value 
  #   in the center of circle.
  #
  ###################################################################

  def drawNode(self, value, crd):
    offset = self.cellSize[0]*1.4 / 2 #crd - offset  = center of circle on crd
    
    font = ImageFont.truetype("Assets/Fonts/Lato-Regular.ttf", int(self.cellSize[0]*0.6)) #load font
    #draw circle
    self.imgDraw.ellipse(
      (
        crd[0] - offset,                          #top left corner x_crd
        crd[1] - offset,                          #top left corner y_crd
        crd[0] + self.cellSize[0]*1.4 - offset,   #bottom right corner x_crd
        crd[1] + self.cellSize[0]*1.4 - offset    #bottom right corner y_crd
      ), 
      fill = self.backgroundColor,                #fill color
      outline = self.color,                       #outline color
      width= 2                                    #outline width
    )
    
    #find width and height of node's value to be drawn
    _, _, text_width, text_height = self.imgDraw.textbbox((0,0), str(value), font)
    
    #position of text to be drawn, taking offset into account
    text_pos = (
      crd[0] - text_width/2,      #x crd of text
      crd[1] - text_height/1.75,  #y crd of text
    )
    
    #actually drawing the text...
    self.imgDraw.text(
      text_pos,           #...at position...
      str(value),         #...with the node's value...
      font = font,        #...with the font object as font...
      fill = self.color,  #...with line color...
      align ="center"     #...and with center allignment.
    )
  
  ###################################################################
  #                       GET GRID SIZE
  #
  #   Returns the a tuple with the height and the number of 
  #   nodes in the tree if it was full.
  #
  ###################################################################
  
  def getGridSize(self, node):
    height = node.getHeight()
    width = self.n_horizontal_cells(height)
    return (width, height)
  
  ###################################################################
  #                 NUMBER OF HORIZONTAL CELLS
  ###################################################################
  
  def n_horizontal_cells(self, n):
    if n <= 0:
      return 1
    return self.n_horizontal_cells(n-1)*2 + 1


###################################################################
#                         CLASS: NODE
#
#   Node has a value, a possible parent (of class Node), 
#   and two possible children (also of class Node)
#
###################################################################

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
  node = Node(10)
  node.setLeftChild(Node(2))
  node.setRightChild(Node(5))
  node.leftChild.setLeftChild(Node(6))
  node.leftChild.setRightChild(Node(69))
  node.leftChild.leftChild.setRightChild(Node(4))
  node.leftChild.leftChild.setLeftChild(Node(7))
  node.leftChild.leftChild.leftChild.setLeftChild(Node(29))
  node.leftChild.leftChild.rightChild.setRightChild(Node(55))
  node.leftChild.rightChild.setRightChild(Node(35))
  node.leftChild.rightChild.rightChild.setRightChild(Node(15))
  node.leftChild.rightChild.rightChild.rightChild.setRightChild(Node(53))
  
  node.printTree()
  
  ti = TreeImage(node)
  ti.show()