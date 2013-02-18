from random import choice as rand_choice

class GTreeNodeBase(object):
   """ GTreeNodeBase Class - The base class for the node tree genomes
   
   :param parent: the parent node of the node
   :param childs: the childs of the node, must be a list of nodes   

   .. versionadded:: 0.6
      Added te *GTreeNodeBase* class
   """

   def __init__(self, parent, childs=None):
      self.parent = parent
      self.childs = []

      if childs is not None:
         if type(childs) != list:
            utils.raise_exception("Childs must be a list of nodes", TypeError)
         typecheck_list = filter(lambda x: not isinstance(x, GTreeNodeBase), childs)
         if len(typecheck_list) > 0:
            utils.raise_exception("Childs must be a list of nodes", TypeError)
         self.childs += childs

   def isLeaf(self):
      """ Return True if the node is a leaf

      :rtype: True or False
      """
      return len(self.childs)==0
   
   def getChild(self, index):
      """ Returns the index-child of the node
      
      :rtype: child node
      """
      return self.childs[index]

   def getChilds(self):
      """ Return the childs of the node

      .. warning :: use .getChilds()[:] if you'll change the list itself, like using childs.reverse(),
                    otherwise the original genome child order will be changed.

      :rtype: a list of nodes
      """
      return self.childs
   
   def addChild(self, child):
      """ Adds a child to the node
      
      :param child: the node to be added   
      """
      if type(child) == list:
         self.childs.extend(child)
      else:
         if not isinstance(child, GTreeNodeBase):
            utils.raise_exception("The child must be a node", TypeError)
         self.childs.append(child)

   def replaceChild(self, older, newer):
      """ Replaces a child of the node

      :param older: the child to be replaces
      :param newer: the new child which replaces the older
      """
      index = self.childs.index(older)
      self.childs[index] = newer

   def setParent(self, parent):
      """ Sets the parent of the node

      :param parent: the parent node
      """
      #if not isinstance(parent, GTreeNodeBase):
      #   utils.raise_exception("The parent must be a node", TypeError)
      self.parent = parent
   
   def getParent(self):
      """ Get the parent node of the node

      :rtype: the parent node
      """
      return self.parent

   def __repr__(self):
      parent = "None" if self.getParent() is None else "Present"
      str_repr = "GTreeNodeBase [Childs=%d]" % len(self)
      return str_repr

   def __len__(self):
      return len(self.childs)

   def copy(self, g):
      """ Copy the current contents GTreeNodeBase to 'g'

      :param g: the destination node      

      .. note:: If you are planning to create a new chromosome representation, you
                **must** implement this method on your class.
      """
      g.parent = self.parent
      g.childs = self.childs[:]
      
   def clone(self):
      """ Clone this GenomeBase

      :rtype: the clone genome   

      .. note:: If you are planning to create a new chromosome representation, you
                **must** implement this method on your class.
      """
      newcopy = GTreeNodeBase(None)
      self.copy(newcopy)
      return newcopy
   

class GTreeBase:
   """ GTreeBase Class - The base class for the tree genomes
   
   :param root_node: the root node of the tree

   .. versionadded:: 0.6
      Added te *GTreeBase* class
   """

   def __init__(self, root_node):
      self.root_node = root_node
      self.tree_height = None
      self.nodes_list = None

   def processNodes(self, cloning=False):
      """ Creates a *cache* on the tree, this method must be called
      every time you change the shape of the tree. It updates the
      internal nodes list and the internal nodes properties such as
      depth and height.
      """
      if self.root_node is None: return
      self.nodes_list   = self.getAllNodes()
      self.nodes_leaf   = filter(lambda n: n.isLeaf(), self.nodes_list)
      self.nodes_branch = filter(lambda n: n.isLeaf()==False, self.nodes_list)

      if not cloning:
         self.tree_height = self.getNodeHeight(self.getRoot())
   
   def getRoot(self):
      """ Return the tree root node 

      :rtype: the tree root node
      """
      return self.root_node
   
   def setRoot(self, root):
      """ Sets the root of the tree

      :param root: the tree root node
      """
      if not isinstance(root, GTreeNodeBase):
         utils.raise_exception("The root must be a node", TypeError)
      self.root_node = root

   def getNodeDepth(self, node):
      """ Returns the depth of a node

      :rtype: the depth of the node, the depth of root node is 0
      """
      if node==self.getRoot(): return 0
      else:                    return 1 + self.getNodeDepth(node.getParent())

   def getNodeHeight(self, node):
      """ Returns the height of a node

      .. note:: If the node has no childs, the height will be 0.

      :rtype: the height of the node
      """
      height = 0
      if len(node) <= 0:
         return 0
      for child in node.getChilds():
         h_inner = self.getNodeHeight(child)+1
         if h_inner > height:
            height = h_inner
      return height

   def getHeight(self):
      """ Return the tree height
      
      :rtype: the tree height
      """
      return self.tree_height

   def getNodesCount(self, start_node=None):
      """ Return the number of the nodes on the tree
      starting at the *start_node*, if *start_node* is None,
      then the method will count all the tree nodes.

      :rtype: the number of nodes
      """
      count = 1
      if start_node is None:
         start_node = self.getRoot()
      for i in start_node.getChilds():
         count += self.getNodesCount(i)
      return count
   
   def getTraversalString(self, start_node=None, spc=0):
      """ Returns a tree-formated string of the tree. This
      method is used by the __repr__ method of the tree
      
      :rtype: a string representing the tree
      """
      str_buff = ""
      if start_node is None:
         start_node = self.getRoot()
         str_buff += "%s\n" % start_node
      spaces = spc + 2
      for child_node in start_node.getChilds():
         str_buff += "%s%s\n" % (" " * spaces, child_node)
         str_buff += self.getTraversalString(child_node, spaces)
      return str_buff


   def traversal(self, callback, start_node=None):
      """ Traversal the tree, this method will call the
      user-defined callback function for each node on the tree

      :param callback: a function
      :param start_node: the start node to begin the traversal
      """
      if not inspect.isfunction(callback):
         utils.raise_exception("The callback for the tree traversal must be a function", TypeError)

      if start_node is None:
         start_node = self.getRoot()
         callback(start_node)
      for child_node in start_node.getChilds():
         callback(child_node)
         self.traversal(callback, child_node)

   def getRandomNode(self, node_type=0):
      """ Returns a random node from the Tree

      :param node_type: 0 = Any, 1 = Leaf, 2 = Branch
      :rtype: random node
      """
      lists = (self.nodes_list, self.nodes_leaf, self.nodes_branch)
      cho = lists[node_type]
      if len(cho) <= 0:
         return None
      return rand_choice(cho)

   def getAllNodes(self):
      """ Return a new list with all nodes
      
      :rtype: the list with all nodes
      """
      node_stack = []
      all_nodes  = []
      tmp = None

      node_stack.append(self.getRoot())
      while len(node_stack) > 0:
         tmp = node_stack.pop()
         all_nodes.append(tmp)
         childs = tmp.getChilds()
         node_stack.extend(childs)

      return all_nodes 

   def __repr__(self):
      str_buff  = "- GTree\n"
      str_buff += "\tHeight:\t\t\t%d\n" % self.getHeight()
      str_buff += "\tNodes:\t\t\t%d\n" % self.getNodesCount()
      str_buff += "\n" + self.getTraversalString()

      return str_buff

   def __len__(self):
      return len(self.nodes_list)
   
   def __getitem__(self, index):
      return self.nodes_list[index]

   def __iter__(self):
      return iter(self.nodes_list)

   def copy(self, g, node=None, node_parent=None):
      """ Copy the current contents GTreeBase to 'g'

      :param g: the destination GTreeBase tree

      .. note:: If you are planning to create a new chromosome representation, you
                **must** implement this method on your class.
      """
      if node is None:
         g.tree_height = self.tree_height
         node = self.root_node

      if node is None: return None

      newnode = node.clone()

      if node_parent is None:
         g.setRoot(newnode)
      else:
         newnode.setParent(node_parent)
         node_parent.replaceChild(node, newnode)
      
      for ci in xrange(len(newnode)):
         GTreeBase.copy(self, g, newnode.getChild(ci), newnode)

      return newnode
      
   def clone(self):
      """ Clone this GenomeBase

      :rtype: the clone genome   

      .. note:: If you are planning to create a new chromosome representation, you
                **must** implement this method on your class.
      """
      newcopy = GTreeBase(None)
      self.copy(newcopy)
      newcopy.processNodes()
      return newcopy


