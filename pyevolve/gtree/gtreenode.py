from gtreebase import GTreeNodeBase

class GTreeNode(GTreeNodeBase):

   """ The GTreeNode class - The node representation

   Inheritance diagram for :class:`GTree.GTreeNode`:

   .. inheritance-diagram:: GTree.GTreeNode

   :param data: the root node of the tree
   :param parent: the parent node, if root, this
                  must be *None*
   """

   def __init__(self, data, parent=None):
      super(GTreeNode, self).__init__(parent)
      self.node_data = data

   def __repr__(self):
      str_repr  = GTreeNodeBase.__repr__(self)
      str_repr += " - [%s]" % self.node_data
      return str_repr     

   def setData(self, data):
      """ Sets the data of the node

      :param data: the data of the node
      """
      self.node_data = data

   def getData(self):
      """ Return the data of the node

      :rtype: the data of the node
      """
      return self.node_data

   def newNode(self, data):
      """ Created a new child node

      :param data: the data of the new created node
      """
      node = GTreeNode(data, self)
      self.addChild(node)
      return node

   def swapNodeData(self, node):
      """ Swaps the node data with another node
      
      :param node: the node to do the data swap
      """
      tmp_data = self.node_data
      self.setData(node.getData())
      node.setData(tmp_data)

   def copy(self, g):
      """ Copy the contents to the destination g
      
      :param g: the GTreeNode genome destination
      """
      super(GTreeNode, self).copy(g)
      g.node_data = self.node_data

   def clone(self):
      """ Return a new instance of the genome
      
      :rtype: new GTree instance
      """
      newcopy = GTreeNode(None)
      self.copy(newcopy)
      return newcopy



      
      
class GTreeNodeGP(GTreeNodeBase):
   """ The GTreeNodeGP Class - The Genetic Programming Node representation
   
   Inheritance diagram for :class:`GTree.GTreeNodeGP`:

   .. inheritance-diagram:: GTree.GTreeNodeGP

   :param data: the node data
   :param type: the node type
   :param parent: the node parent
   
   """
   def __init__(self, data, node_type=0, parent=None):
      super(GTreeNodeGP, self) .__init__(parent)
      self.node_type = node_type
      self.node_data = data

   def __repr__(self):
      str_repr  = GTreeNodeBase.__repr__(self)
      str_repr += " - [%s]" % self.node_data
      return str_repr     

   def compare(self, other):
      """ Compare this node with other 
      
      :param other: the other GTreeNodeGP
      """
      if not isinstance(other, GTreeNodeGP):
         utils.raise_exception("The other node used to compare is not a GTreeNodeGP class", TypeError)

      if other.node_type == self.node_type:
         if other.node_data == self.node_data:
            return 0
      return -1

   def setData(self, data):
      """Sets the node internal data
      
      :param data: the internal data
      """
      self.node_data = data

   def getData(self):
      """Gets the node internal data
      
      :rtype: the internal data
      """
      return self.node_data

   def setType(self, node_type):
      """Sets the node type 
      
      :param node_type: the node type is type of constants.nodeType
      """
      self.node_type = node_type

   def getType(self):
      """Get the node type 
      
      :rtype: the node type is type of constants.nodeType
      """
      return self.node_type

   def newNode(self, data):
      """Creates a new node and adds this
      node as children of current node

      :param data: the internal node data
      """
      node = GTreeNodeGP(data, self)
      self.addChild(node)
      return node

   def swapNodeData(self, node):
      """Swaps the node data and type with another node

      :param node: the node
      """
      tmp_data = self.node_data
      tmp_type = self.node_type
      self.setData(node.getData())
      self.setType(node.getType())
      node.setData(tmp_data)
      node.setType(tmp_type)

   def copy(self, g):
      """ Copy the contents to the destination g
      
      :param g: the GTreeNodeGP genome destination
      """
      super(GTreeNodeGP, self).copy(g)
      g.node_data = self.node_data
      g.node_type = self.node_type

   def clone(self):
      """ Return a new copy of the node

      :rtype: the new GTreeNodeGP instance
      """
      newcopy = GTreeNodeGP(None)
      self.copy(newcopy)
      return newcopy
