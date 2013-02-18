import random
from gtreenode import GTreeNode
from gtreenode import GTreeNodeGP

#################################
#    Tree utilsity Functions     # 
#################################


def buildGTreeGrow(depth, value_callback, max_siblings, max_depth):
   """ Random generates a Tree structure using the value_callback
   for data generation and the method "Grow"

   :param depth: the initial depth, zero
   :param value_callback: the function which generates the random
                          values for nodes
   :param max_siblings: the maximum number of sisters of a node
   :param max_depth: the maximum depth of the tree   

   :rtype: the root node of created tree
   """

   random_value = value_callback()
   n = GTreeNode(random_value)

   if depth == max_depth: return n

   for i in xrange(random.randint(0, abs(max_siblings))):
      child = buildGTreeGrow(depth+1, value_callback, max_siblings, max_depth)
      child.setParent(n)
      n.addChild(child)
   return n

def buildGTreeFull(depth, value_callback, max_siblings, max_depth):
   """ Random generates a Tree structure using the value_callback
   for data generation and the method "Full"

   :param depth: the initial depth, zero
   :param value_callback: the function which generates the random
                          values for nodes
   :param max_siblings: the maximum number of sisters of a node
   :param max_depth: the maximum depth of the tree   

   :rtype: the root node of created tree
   """

   random_value = value_callback()
   n = GTreeNode(random_value)

   if depth == max_depth: return n

   if max_siblings < 0: range_val = abs(max_siblings)
   else:                range_val = random.randint(1, abs(max_siblings))
 
   for i in xrange(range_val):
      child = buildGTreeFull(depth+1, value_callback, max_siblings, max_depth)
      child.setParent(n)
      n.addChild(child)
   return n
   
   
#################################
#    Tree GP utilsity Functions  # 
#################################

def gpdec(**kwds):
   """ This is a decorator to use with genetic programming non-terminals
   
   It currently accepts the attributes: shape, color and representation.
   """
   def decorate(f):
      for k in kwds:
            setattr(f, k, kwds[k])
      return f
   return decorate

def checkTerminal(terminal):
   """ Do some check on the terminal, to evaluate ephemeral constants

   :param terminal: the terminal string
   """
   if terminal.startswith("ephemeral:"):
      splited = terminal.split(":")
      ephemeral_constant = eval(splited[1])
      return str(ephemeral_constant)
   else:
      return terminal

def buildGTreeGPGrow(ga_engine, depth, max_depth):
   """ Creates a new random GTreeGP root node with subtrees using
   the "Grow" method.
   
   :param ga_engine: the GA Core
   :param depth: the initial depth
   :max_depth: the maximum depth of the tree
   :rtype: the root node
   """

   gp_terminals = ga_engine.get_param("gp_terminals")
   assert gp_terminals is not None

   gp_function_set = ga_engine.get_param("gp_function_set")
   assert gp_function_set is not None

   if depth == max_depth:
      random_terminal = checkTerminal(random.choice(gp_terminals))
      n = GTreeNodeGP(random_terminal, constants.nodeType["TERMINAL"])
      return n
   else:
      # Do not generate degenerative trees 
      if depth == 0:
         random_node = random.choice(gp_function_set.keys())
      else:
         fchoice = random.choice([gp_function_set.keys(), gp_terminals])
         random_node = random.choice(fchoice)

      if random_node in gp_terminals:
         n = GTreeNodeGP(checkTerminal(random_node), constants.nodeType["TERMINAL"])
      else:
         n = GTreeNodeGP(random_node, constants.nodeType["NONTERMINAL"])

   if n.getType() == constants.nodeType["NONTERMINAL"]:
      for i in xrange(gp_function_set[n.getData()]):
         child = buildGTreeGPGrow(ga_engine, depth+1, max_depth)
         child.setParent(n)
         n.addChild(child)

   return n

def buildGTreeGPFull(ga_engine, depth, max_depth):
   """ Creates a new random GTreeGP root node with subtrees using
   the "Full" method.
   
   :param ga_engine: the GA Core
   :param depth: the initial depth
   :max_depth: the maximum depth of the tree
   :rtype: the root node
   """
   gp_terminals = ga_engine.get_param("gp_terminals")
   assert gp_terminals is not None

   gp_function_set = ga_engine.get_param("gp_function_set")
   assert gp_function_set is not None

   if depth == max_depth:
      random_terminal = checkTerminal(random.choice(gp_terminals))
      n = GTreeNodeGP(random_terminal, constants.nodeType["TERMINAL"])
      return n
   else:
      random_oper = random.choice(gp_function_set.keys())
      n = GTreeNodeGP(random_oper, constants.nodeType["NONTERMINAL"])

   if n.getType() == constants.nodeType["NONTERMINAL"]:
      for i in xrange(gp_function_set[n.getData()]):
         child = buildGTreeGPFull(ga_engine, depth+1, max_depth)
         child.setParent(n)
         n.addChild(child)

   return n

