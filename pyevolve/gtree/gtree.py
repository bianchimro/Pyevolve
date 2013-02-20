"""

:mod:`GTree` and GTreeGP -- the tree chromosomes
=============================================================

This is the rooted tree representation, this chromosome representation
can carry any data-type.


Default Parameters
-------------------------------------------------------------

*Initializator*

  :func:`initializators.GTreeInitializatorInteger`

   The Integer Initializator for GTree

*Mutator*
   
   :func:`mutators.GTreeMutatorIntegerRange`

   The Integer Range mutator for GTree

*Crossover*

   :func:`crossovers.GTreeCrossoverSinglePointStrict`

   The Strict Single Point crossover for GTree

.. versionadded:: 0.6
   The *GTree* module.

Classes
-------------------------------------------------------------
"""
import random
from ..genome import GenomeBase
from gtreebase import GTreeBase, GTreeNodeBase
from gtreenode import GTreeNode

import initializators
import mutators
import crossovers
from .. import utils

# - GTree defaults
CDefGTreeInit      = initializators.GTreeInitializatorInteger
CDefGGTreeMutator  = mutators.GTreeMutatorIntegerRange
CDefGTreeCrossover = crossovers.GTreeCrossoverSinglePointStrict


# - GTreeGP defaults
CDefGTreeGPInit      = initializators.GTreeGPInitializator
CDefGGTreeGPMutator  = mutators.GTreeGPMutatorSubtree
CDefGTreeGPCrossover = crossovers.GTreeGPCrossoverSinglePoint



try:
   import pydot
   HAVE_PYDOT = True
except ImportError:
   HAVE_PYDOT = False
   
#################################
#             GTree             # 
#################################


class GTree(GenomeBase, GTreeBase):
   """ The GTree class - The tree chromosome representation

   Inheritance diagram for :class:`GTree.GTree`:

   .. inheritance-diagram:: GTree.GTree

   :param root_node: the root node of the tree
   """
   
   evaluator = None
   """ This is the :term:`evaluation function` slot, you can add
   a function with the *set* method: ::

      genome.evaluator.set(eval_func)
   """

   initializator = None
   """ This is the initialization function of the genome, you
   can change the default initializator using the function slot: ::

      genome.initializator.set(initializators.G1DListInitializatorAllele)

   In this example, the initializator :func:`initializators.G1DListInitializatorAllele`
   will be used to create the initial population.
   """

   mutator = None
   """ This is the mutator function slot, you can change the default
   mutator using the slot *set* function: ::

      genome.mutator.set(mutators.G1DListMutatorSwap)

   """

   crossover = None
   """ This is the reproduction function slot, the crossover. You
   can change the default crossover method using: ::

      genome.crossover.set(crossovers.G1DListCrossoverUniform)
   """

   def __init__(self, root_node=None):
      GenomeBase.__init__(self)
      GTreeBase.__init__(self, root_node)
      self.initializator.set(CDefGTreeInit)
      self.mutator.set(CDefGGTreeMutator)
      self.crossover.set(CDefGTreeCrossover)

   def __repr__(self):
      """ Return a string representation of Genome """
      ret  = GenomeBase.__repr__(self)
      ret += GTreeBase.__repr__(self)
      return ret

   def copy(self, g):
      """ Copy the contents to the destination g
      
      :param g: the GTree genome destination
      """
      GenomeBase.copy(self, g)
      GTreeBase.copy(self, g)

   def clone(self):
      """ Return a new instance of the genome
      
      :rtype: new GTree instance
      """
      newcopy = GTree()
      self.copy(newcopy)
      newcopy.processNodes(True)
      return newcopy



#################################
#             GTree   GP        # 
#################################



class GTreeGP(GenomeBase, GTreeBase):
   """ The GTreeGP Class - The Genetic Programming Tree representation
   
   Inheritance diagram for :class:`GTree.GTreeGP`:

   .. inheritance-diagram:: GTree.GTreeGP

   :param root_node: the Root node of the GP Tree
   """
   def __init__(self, root_node=None, cloning=False):
      GenomeBase.__init__(self)
      GTreeBase.__init__(self, root_node)
      if not cloning:
         self.initializator.set(CDefGTreeGPInit)
         self.mutator.set(CDefGGTreeGPMutator)
         self.crossover.set(CDefGTreeGPCrossover)

   def __repr__(self):
      """ Return a string representation of Genome """
      ret  = GenomeBase.__repr__(self)
      ret += GTreeBase.__repr__(self)
      ret += "\n- GTreeGP\n"      
      ret += "\tExpression: %s\n" % self.getPreOrderExpression()
      return ret

   def writeDotImage(self, filename):
      """ Writes a image representation of the individual

      :param filename: the output file image
      """
      if not HAVE_PYDOT:
         utils.raise_exception("You must install Pydot to use this feature !")

      graph = pydot.Dot()
      self.writeDotGraph(graph)
      graph.write_jpeg(filename, prog='dot')

   def writeDotRaw(self, filename):
      """ Writes the raw dot file (text-file used by dot/neato) with the
      representation of the individual

      :param filename: the output file, ex: individual.dot
      """
      if not HAVE_PYDOT:
         utils.raise_exception("You must install Pydot to use this feature !")

      graph = pydot.Dot(graph_type="digraph")
      self.writeDotGraph(graph)
      graph.write(filename, prog='dot', format="raw")

   def writeDotGraph(self, graph, startNode=0):
      """ Write a graph to the pydot Graph instance
      
      :param graph: the pydot Graph instance
      :param startNode: used to plot more than one individual 
      """
      if not HAVE_PYDOT:
         print "You must install Pydot to use this feature !"
         return

      count = startNode
      node_stack = []
      nodes_dict = {}
      tmp = None
      import __main__ as main_module

      for i in xrange(len(self.nodes_list)):
         newnode = pydot.Node(str(count), style="filled")
         count += 1

         if self.nodes_list[i].getType() == nodeType["TERMINAL"]:
            newnode.set_color("lightblue2")
         else:
            newnode.set_color("goldenrod2")

         if self.nodes_list[i].getType() == nodeType["NONTERMINAL"]:
            func = getattr(main_module, self.nodes_list[i].getData())

            if hasattr(func, "shape"):
               newnode.set_shape(func.shape)

            if hasattr(func, "representation"):
               newnode.set_label(func.representation)
            else:
               newnode.set_label(self.nodes_list[i].getData())
            if hasattr(func, "color"): newnode.set_color(func.color)

         else:
            newnode.set_label(self.nodes_list[i].getData())
      
         nodes_dict.update({self.nodes_list[i]: newnode})
         graph.add_node(newnode)

      node_stack.append(self.getRoot())
      while len(node_stack) > 0:
         tmp = node_stack.pop()

         parent = tmp.getParent()
         if parent is not None:
            parent_node = nodes_dict[parent]
            child_node  = nodes_dict[tmp]
           
            newedge = pydot.Edge(parent_node, child_node)
            graph.add_edge(newedge)
   
         rev_childs = tmp.getChilds()[:]
         rev_childs.reverse()
         node_stack.extend(rev_childs)

      return count



   def getSExpression(self, start_node=None):
      """ Returns a tree-formated string (s-expression) of the tree.
      
      :rtype: a S-Expression representing the tree
      """
      str_buff = ""
      if start_node is None:
         start_node = self.getRoot()
         str_buff += "%s " % start_node.getData()

      is_leaf = start_node.isLeaf()
      if not is_leaf:
         str_buff += "( "

      for child_node in start_node.getChilds():
         str_buff += "%s " % child_node.getData()
         str_buff += self.getSExpression(child_node)

      if not is_leaf:
         str_buff += " )"
      return str_buff

   def getPreOrderExpression(self, start_node=None):
      """ Return the pre order expression string of the Tree, used
      to python *eval*.

      :rtype: the expression string
      """
      if start_node is None:
         start_node = self.getRoot()

      str_buff = start_node.getData()

      if not start_node.isLeaf():
         all_childs  = start_node.getChilds()
         str_buff += "(" + self.getPreOrderExpression(all_childs[0])

         for index in xrange(1, len(all_childs)):
            child = all_childs[index]
            str_buff += ", " + self.getPreOrderExpression(child)
         str_buff += ")"
      
      return str_buff

   def getCompiledCode(self):
      """ Get the compiled code for the Tree expression
      After getting the compiled code object, you just need to evaluate it using
      the :func:`eval` native Python method.
      
      :rtype: compiled python code
      """
      expr = self.getPreOrderExpression()
      return compile(expr, "<string>", "eval")

   def copy(self, g):
      """ Copy the contents to the destination g
      
      :param g: the GTreeGP genome destination
      """
      GenomeBase.copy(self, g)
      GTreeBase.copy(self, g)

   def clone(self):
      """ Return a new instance of the genome
      
      :rtype: the new GTreeGP instance
      """
      newcopy = GTreeGP(cloning=True)
      self.copy(newcopy)
      newcopy.processNodes(True)
      return newcopy

   def compare(self, other):
      """ This method will compare the currently tree with another one

      :param other: the other GTreeGP to compare
      """
      if not isinstance(other, GTreeGP):
         utils.raise_exception("The other tree used to compare is not a GTreeGP class", TypeError)

      stack_self  = []
      stack_other = []

      tmp_self  = None
      tmp_other = None

      stack_self.append(self.getRoot())
      stack_other.append(other.getRoot())

      while len(stack_self) > 0:

         if (len(stack_self) <= 0) or (len(stack_other) <= 0):
            return -1
         
         tmp_self, tmp_other = stack_self.pop(), stack_other.pop()
         if tmp_self.compare(tmp_other) <> 0:
            return -1

         stack_self.extend(tmp_self.getChilds())
         stack_other.extend(tmp_other.getChilds())
   
      return 0

   @staticmethod
   def writePopulationDot(ga_engine, filename, format="jpeg", start=0, end=0):
      """ Writes to a graphical file using pydot, the population of trees

      Example:
         >>> GTreeGP.writePopulationDot(ga_engine, "pop.jpg", "jpeg", 0, 10)

      This example will draw the first ten individuals of the population into
      the file called "pop.jpg".

      :param ga_engine: the GA Engine
      :param filename: the filename, ie. population.jpg
      :param start: the start index of individuals
      :param end: the end index of individuals
      """
      if not HAVE_PYDOT:
         utils.raise_exception("You must install Pydot to use this feature !")

      pop = ga_engine.getPopulation()
      graph = pydot.Dot(graph_type="digraph")

      if not isinstance(pop[0], GTreeGP):
         utils.raise_exception("The population must have individuals of the GTreeGP chromosome !")

      n = 0
      end_index = len(pop) if end==0 else end
      for i in xrange(start, end_index):
         ind = pop[i]
         subg = pydot.Cluster("cluster_%d" % i, label="\"Ind. #%d - Score Raw/Fit.: %.4f/%.4f\"" % (i, ind.get_raw_score(), ind.get_fitness_score()))
         n = ind.writeDotGraph(subg, n)
         graph.add_subgraph(subg)

      graph.write(filename, prog='dot', format=format)

   @staticmethod
   def writePopulationDotRaw(ga_engine, filename, start=0, end=0):
      """ Writes to a raw dot file using pydot, the population of trees

      Example:
         >>> GTreeGP.writePopulationDotRaw(ga_engine, "pop.dot", 0, 10)

      This example will draw the first ten individuals of the population into
      the file called "pop.dot".

      :param ga_engine: the GA Engine
      :param filename: the filename, ie. population.dot
      :param start: the start index of individuals
      :param end: the end index of individuals
      """
      if not HAVE_PYDOT:
         utils.raise_exception("You must install Pydot to use this feature !")

      pop = ga_engine.getPopulation()
      graph = pydot.Dot(graph_type="digraph")

      if not isinstance(pop[0], GTreeGP):
         utils.raise_exception("The population must have individuals of the GTreeGP chromosome !")

      n = 0
      end_index = len(pop) if end==0 else end
      for i in xrange(start, end_index):
         ind = pop[i]
         subg = pydot.Cluster("cluster_%d" % i, label="\"Ind. #%d - Score Raw/Fit.: %.4f/%.4f\"" % (i, ind.get_raw_score(), ind.get_fitness_score()))
         n = ind.writeDotGraph(subg, n)
         graph.add_subgraph(subg)

      graph.write(filename, prog='dot', format="raw")


