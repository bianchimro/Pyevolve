"""

:mod:`crossovers` -- crossover methods module
=====================================================================

In this module we have the genetic operators of crossover (or recombination) for each chromosome representation.

"""

from random import randint as rand_randint, choice as rand_choice
from random import random as rand_random
import math
import utils
#import constants


# SBX Crossover defaults
# Crossover distribution index for SBX
# Larger Etac = similar to parents
# Smaller Etac = far away from parents
CDefG1DListSBXEtac  = 10
CDefG1DListSBXEPS   = 1.0e-14


#############################
##     1D Binary String    ##
#############################

def G1DBinaryStringXSinglePoint(genome, **args):
   """ The crossover of 1D Binary String, Single Point

   .. warning:: You can't use this crossover method for binary strings with length of 1.

   """
   sister = None
   brother = None
   gMom = args["mom"]
   gDad = args["dad"]

   if len(gMom) == 1:
      utils.raise_exception("The Binary String have one element, can't use the Single Point Crossover method !", TypeError)

   cut = rand_randint(1, len(gMom)-1)

   if args["count"] >= 1:
      sister = gMom.clone()
      sister.reset_stats()
      sister[cut:] = gDad[cut:]

   if args["count"] == 2:
      brother = gDad.clone()
      brother.reset_stats()
      brother[cut:] = gMom[cut:]

   return (sister, brother)

def G1DBinaryStringXTwoPoint(genome, **args):
   """ The 1D Binary String crossover, Two Point

   .. warning:: You can't use this crossover method for binary strings with length of 1.

   """
   sister = None
   brother = None
   gMom = args["mom"]
   gDad = args["dad"]
   
   if len(gMom) == 1:
      utils.raise_exception("The Binary String have one element, can't use the Two Point Crossover method !", TypeError)

   cuts = [rand_randint(1, len(gMom)-1), rand_randint(1, len(gMom)-1)]

   if cuts[0] > cuts[1]:
      utils.list_swap_element(cuts, 0, 1)

   if args["count"] >= 1:
      sister = gMom.clone()
      sister.reset_stats()
      sister[cuts[0]:cuts[1]] = gDad[cuts[0]:cuts[1]]

   if args["count"] == 2:
      brother = gDad.clone()
      brother.reset_stats()
      brother[cuts[0]:cuts[1]] = gMom[cuts[0]:cuts[1]]

   return (sister, brother)

def G1DBinaryStringXUniform(genome, **args):
   """ The G1DList Uniform Crossover """
   sister = None
   brother = None
   gMom = args["mom"]
   gDad = args["dad"]

   sister = gMom.clone()
   brother = gDad.clone()
   sister.reset_stats()
   brother.reset_stats()

   for i in xrange(len(gMom)):
      if utils.random_flip_coin(CDefG1DBinaryStringUniformProb):
         temp = sister[i]
         sister[i] = brother[i]
         brother[i] = temp
            
   return (sister, brother)

####################
##     1D List    ##
####################
     
def G1DListCrossoverSinglePoint(genome, **args):
   """ The crossover of G1DList, Single Point

   .. warning:: You can't use this crossover method for lists with just one element.

   """
   sister = None
   brother = None
   gMom = args["mom"]
   gDad = args["dad"]
   
   if len(gMom) == 1:
      utils.raise_exception("The 1D List have one element, can't use the Single Point Crossover method !", TypeError)
      
   cut = rand_randint(1, len(gMom)-1)

   if args["count"] >= 1:
      sister = gMom.clone()
      sister.reset_stats()
      sister[cut:] = gDad[cut:]

   if args["count"] == 2:
      brother = gDad.clone()
      brother.reset_stats()
      brother[cut:] = gMom[cut:]

   return (sister, brother)

def G1DListCrossoverTwoPoint(genome, **args):
   """ The G1DList crossover, Two Point

   .. warning:: You can't use this crossover method for lists with just one element.

   """
   sister = None
   brother = None
   gMom = args["mom"]
   gDad = args["dad"]
   
   if len(gMom) == 1:
      utils.raise_exception("The 1D List have one element, can't use the Two Point Crossover method !", TypeError)

   cuts = [rand_randint(1, len(gMom)-1), rand_randint(1, len(gMom)-1)]

   if cuts[0] > cuts[1]:
      utils.list_swap_element(cuts, 0, 1)

   if args["count"] >= 1:
      sister = gMom.clone()
      sister.reset_stats()
      sister[cuts[0]:cuts[1]] = gDad[cuts[0]:cuts[1]]

   if args["count"] == 2:
      brother = gDad.clone()
      brother.reset_stats()
      brother[cuts[0]:cuts[1]] = gMom[cuts[0]:cuts[1]]

   return (sister, brother)

def G1DListCrossoverUniform(genome, **args):
   """ The G1DList Uniform Crossover 
   
   Each gene has a 50% chance of being swapped between mom and dad
   
   """
   sister = None
   brother = None
   gMom = args["mom"]
   gDad = args["dad"]

   sister = gMom.clone()
   brother = gDad.clone()
   sister.reset_stats()
   brother.reset_stats()

   for i in xrange(len(gMom)):
      if utils.random_flip_coin(CDefG1DListCrossUniformProb):
         temp = sister[i]
         sister[i] = brother[i]
         brother[i] = temp
            
   return (sister, brother)

def G1DListCrossoverOX(genome, **args):
   """ The OX Crossover for G1DList  (order crossover) """
   sister = None
   brother = None
   gMom = args["mom"]
   gDad = args["dad"]
   listSize = len(gMom)

   c1, c2 = [rand_randint(1, len(gMom)-1), rand_randint(1, len(gMom)-1)]

   while c1 == c2:
      c2 = rand_randint(1, len(gMom)-1)

   if c1 > c2:
      h = c1
      c1 = c2
      c2 = h

   if args["count"] >= 1:
      sister = gMom.clone()
      sister.reset_stats()
      P1 = [ c for c in gMom[c2:] + gMom[:c2] if c not in gDad[c1:c2] ]
      sister.genomeList = P1[listSize - c2:] + gDad[c1:c2] + P1[:listSize-c2]
    
   if args["count"] == 2:
      brother = gDad.clone()
      brother.reset_stats()
      P2 = [ c for c in gDad[c2:] + gDad[:c2] if c not in gMom[c1:c2] ]
      brother.genomeList = P2[listSize - c2:] + gMom[c1:c2] + P2[:listSize-c2]

   assert listSize == len(sister)
   assert listSize == len(brother)

   return (sister, brother)

def G1DListCrossoverEdge(genome, **args):
   """ THe Edge Recombination crossover for G1DList (widely used for TSP problem)

   See more information in the `Edge Recombination Operator <http://en.wikipedia.org/wiki/Edge_recombination_operator>`_
   Wikipedia entry.
   """
   gMom, sisterl  = args["mom"], []
   gDad, brotherl = args["dad"], []

   mom_edges, dad_edges, merge_edges = utils.G1DListGetEdgesComposite(gMom, gDad)

   for c, u in (sisterl, set(gMom)), (brotherl, set(gDad)):
      curr = None
      for i in xrange(len(gMom)):
         curr = rand_choice(tuple(u)) if not curr else curr         
         c.append(curr)
         u.remove(curr)
         d = [v for v in merge_edges.get(curr, []) if v in u]
         if d: curr = rand_choice(d)
         else:
            s  = [v for v in mom_edges.get(curr, []) if v in u]
            s += [v for v in dad_edges.get(curr, []) if v in u]
            curr = rand_choice(s) if s else None

   sister = gMom.clone()
   brother = gDad.clone()
   sister.reset_stats()
   brother.reset_stats()

   sister.genomeList  = sisterl
   brother.genomeList = brotherl

   return (sister, brother)

def G1DListCrossoverCutCrossfill(genome, **args):
   """ The crossover of G1DList, Cut and crossfill, for permutations
   """
   sister = None
   brother = None
   gMom = args["mom"]
   gDad = args["dad"]
   
   if len(gMom) == 1:
      utils.raise_exception("The 1D List have one element, can't use the Single Point Crossover method !", TypeError)
      
   cut = rand_randint(1, len(gMom)-1)

   if args["count"] >= 1:
      sister = gMom.clone()
      mother_part = gMom[0:cut]
      sister.reset_stats()
      i = (len(sister) - cut)
      x = 0
      for v in gDad:
         if v in mother_part: continue
         if x >= i: break
         sister[cut+x] = v
         x += 1
      
   if args["count"] == 2:
      brother = gDad.clone()
      father_part = gDad[0:cut]
      brother.reset_stats()
      i = (len(brother) - cut) 
      x = 0
      for v in gMom:
         if v in father_part: continue
         if x >= i: break
         brother[cut+x] = v
         x += 1
      
   return (sister, brother)

def G1DListCrossoverRealSBX(genome, **args):
   """ Experimental SBX Implementation - Follows the implementation in NSGA-II (Deb, et.al)

   Some implementation `reference <http://vision.ucsd.edu/~sagarwal/icannga.pdf>`_.
   And another reference to the `Simulated Binary Crossover <http://www.mitpressjournals.org/doi/abs/10.1162/106365601750190406>`_.

   .. warning:: This crossover method is Data Type Dependent, which means that
                must be used for 1D genome of real values.
   """
   EPS = CDefG1DListSBXEPS
   # Crossover distribution index
   eta_c = CDefG1DListSBXEtac  

   gMom = args["mom"]
   gDad = args["dad"]

   # Get the variable bounds ('gDad' could have been used; but I love Mom:-))
   lb = gMom.get_param("rangemin", CDefRangeMin)
   ub = gMom.get_param("rangemax", CDefRangeMax)

   sister = gMom.clone()
   brother = gDad.clone()

   sister.reset_stats()
   brother.reset_stats()

   for i in range(0,len(gMom)):
      if math.fabs(gMom[i]-gDad[i]) > EPS:
         if gMom[i] > gDad[i]:
            #swap
            temp = gMom[i]
            gMom[i] = gDad[i]
            gDad[i] = temp

         #random number betwn. 0 & 1
         u = rand_random() 
      
         beta = 1.0 + 2*(gMom[i] - lb)/(1.0*(gDad[i]-gMom[i]))
         alpha = 2.0 - beta**(-(eta_c+1.0))

         if u <= (1.0/alpha):
            beta_q = (u*alpha)**(1.0/((eta_c + 1.0)*1.0))
         else:
            beta_q = (1.0/(2.0-u*alpha))**(1.0/(1.0*(eta_c + 1.0)))

         brother[i] = 0.5*((gMom[i] + gDad[i]) - beta_q*(gDad[i]-gMom[i]))

         beta = 1.0 + 2.0*(ub - gDad[i])/(1.0*(gDad[i]-gMom[i]))
         alpha = 2.0 - beta**(-(eta_c+1.0))

         if u <= (1.0/alpha):
            beta_q = (u*alpha)**(1.0/((eta_c + 1)*1.0))
         else:
            beta_q = (1.0/(2.0-u*alpha))**(1.0/(1.0*(eta_c + 1.0)))

         sister[i] = 0.5*((gMom[i] + gDad[i]) + beta_q*(gDad[i]-gMom[i]))


         if brother[i] > ub: brother[i] = ub
         if brother[i] < lb: brother[i] = lb

         if sister[i] > ub: sister[i] = ub
         if sister[i] < lb: sister[i] = lb

         if rand_random() > 0.5:
            # Swap
            temp = sister[i]
            sister[i] = brother[i]
            brother[i] = temp
      else:
         sister[i] = gMom[i]
         brother[i] = gDad[i]

   return (sister, brother)
        

####################
##     2D List    ##
####################

def G2DListCrossoverUniform(genome, **args):
   """ The G2DList Uniform Crossover """
   sister = None
   brother = None
   gMom = args["mom"]
   gDad = args["dad"]

   sister = gMom.clone()
   brother = gDad.clone()
   sister.reset_stats()
   brother.reset_stats()
   
   h, w = gMom.get_size()
   
   for i in xrange(h):
      for j in xrange(w):
         if utils.random_flip_coin(CDefG2DListCrossUniformProb):
            temp = sister.get_item(i, j)
            sister.set_item(i, j, brother.get_item(i, j))
            brother.set_item(i, j, temp)

   return (sister, brother)


def G2DListCrossoverSingleVPoint(genome, **args):
   """ The crossover of G2DList, Single Vertical Point """
   sister = None
   brother = None
   gMom = args["mom"]
   gDad = args["dad"]

   cut = rand_randint(1, gMom.get_width()-1)

   if args["count"] >= 1:
      sister = gMom.clone()
      sister.reset_stats()
      for i in xrange(sister.get_height()):
         sister[i][cut:] = gDad[i][cut:]

   if args["count"] == 2:
      brother = gDad.clone()
      brother.reset_stats()
      for i in xrange(brother.get_height()):
         brother[i][cut:] = gMom[i][cut:]

   return (sister, brother)

def G2DListCrossoverSingleHPoint(genome, **args):
   """ The crossover of G2DList, Single Horizontal Point """
   sister = None
   brother = None
   gMom = args["mom"]
   gDad = args["dad"]

   cut = rand_randint(1, gMom.get_height()-1)

   if args["count"] >= 1:
      sister = gMom.clone()
      sister.reset_stats()
      for i in xrange(cut, sister.get_height()):
         sister[i][:] = gDad[i][:]

   if args["count"] == 2:
      brother = gDad.clone()
      brother.reset_stats()
      for i in xrange(brother.get_height()):
         brother[i][:] = gMom[i][:]

   return (sister, brother)


#############################
##     2D Binary String    ##
#############################


def G2DBinaryStringXUniform(genome, **args):
   """ The G2DBinaryString Uniform Crossover
   
   .. versionadded:: 0.6
      The *G2DBinaryStringXUniform* function
   """
   sister = None
   brother = None
   gMom = args["mom"]
   gDad = args["dad"]

   sister = gMom.clone()
   brother = gDad.clone()
   sister.reset_stats()
   brother.reset_stats()
   
   h, w = gMom.get_size()
   
   for i in xrange(h):
      for j in xrange(w):
         if utils.random_flip_coin(CDefG2DBinaryStringUniformProb):
            temp = sister.get_item(i, j)
            sister.set_item(i, j, brother.get_item(i, j))
            brother.set_item(i, j, temp)

   return (sister, brother)


def G2DBinaryStringXSingleVPoint(genome, **args):
   """ The crossover of G2DBinaryString, Single Vertical Point
   
   .. versionadded:: 0.6
      The *G2DBinaryStringXSingleVPoint* function
   """
   sister = None
   brother = None
   gMom = args["mom"]
   gDad = args["dad"]

   cut = rand_randint(1, gMom.get_width()-1)

   if args["count"] >= 1:
      sister = gMom.clone()
      sister.reset_stats()
      for i in xrange(sister.get_height()):
         sister[i][cut:] = gDad[i][cut:]

   if args["count"] == 2:
      brother = gDad.clone()
      brother.reset_stats()
      for i in xrange(brother.get_height()):
         brother[i][cut:] = gMom[i][cut:]

   return (sister, brother)

def G2DBinaryStringXSingleHPoint(genome, **args):
   """ The crossover of G2DBinaryString, Single Horizontal Point
   
   .. versionadded:: 0.6
      The *G2DBinaryStringXSingleHPoint* function
  
   """
   sister = None
   brother = None
   gMom = args["mom"]
   gDad = args["dad"]

   cut = rand_randint(1, gMom.get_height()-1)

   if args["count"] >= 1:
      sister = gMom.clone()
      sister.reset_stats()
      for i in xrange(cut, sister.get_height()):
         sister[i][:] = gDad[i][:]

   if args["count"] == 2:
      brother = gDad.clone()
      brother.reset_stats()
      for i in xrange(brother.get_height()):
         brother[i][:] = gMom[i][:]

   return (sister, brother)

#############################
##          Tree           ##
#############################


def GTreeCrossoverSinglePoint(genome, **args):
   """ The crossover for GTree, Single Point """
   sister = None
   brother = None
   gMom = args["mom"].clone()
   gDad = args["dad"].clone()

   gMom.reset_stats()
   gDad.reset_stats()

   node_mom_stack = []
   all_mom_nodes  = []
   node_mom_tmp   = None

   node_dad_stack = []
   all_dad_nodes  = []
   node_dad_tmp   = None

   node_mom_stack.append(gMom.getRoot())
   node_dad_stack.append(gDad.getRoot())

   while (len(node_mom_stack) > 0) and  (len(node_dad_stack) > 0):
      node_mom_tmp = node_mom_stack.pop()
      node_dad_tmp = node_dad_stack.pop()

      if node_mom_tmp != gMom.getRoot():
         all_mom_nodes.append(node_mom_tmp)
         all_dad_nodes.append(node_dad_tmp)

      node_mom_stack.extend(node_mom_tmp.getChilds())
      node_dad_stack.extend(node_dad_tmp.getChilds())

   if len(all_mom_nodes)==0 or len(all_dad_nodes)==0:
      return (gMom, gDad)

   if len(all_dad_nodes) == 1: nodeDad = all_dad_nodes[0]
   else: nodeDad = rand_choice(all_dad_nodes)

   if len(all_mom_nodes) == 1: nodeMom = all_mom_nodes[0]
   else: nodeMom = rand_choice(all_mom_nodes)

   nodeMom_parent = nodeMom.getParent()
   nodeDad_parent = nodeDad.getParent()

   # Sister
   if args["count"] >= 1:
      sister = gMom
      nodeDad.setParent(nodeMom_parent)
      nodeMom_parent.replaceChild(nodeMom, nodeDad)
      sister.processNodes()

   # Brother
   if args["count"] == 2:
      brother = gDad
      nodeMom.setParent(nodeDad_parent)
      nodeDad_parent.replaceChild(nodeDad, nodeMom)
      brother.processNodes()

   return (sister, brother)

def GTreeCrossoverSinglePointStrict(genome, **args):
   """ The crossover of Tree, Strict Single Point

   ..note:: This crossover method creates offspring with restriction of the
            *max_depth* parameter.
   
   Accepts the *max_attempt* parameter, *max_depth* (required), and
   the distr_leaft (>= 0.0 and <= 1.0), which represents the probability
   of leaf selection when findin random nodes for crossover.
   
   """
   sister = None
   brother = None

   gMom = args["mom"].clone()
   gDad = args["dad"].clone()

   gMom.reset_stats()
   gDad.reset_stats()

   max_depth   = gMom.get_param("max_depth", None)
   max_attempt = gMom.get_param("max_attempt", 10)
   distr_leaf =  gMom.get_param("distr_leaf", None)

   if max_depth is None:
      utils.raise_exception("You must specify the max_depth genome parameter !", ValueError)
      
   if max_depth < 0:
      utils.raise_exception("The max_depth must be >= 1, if you want to use GTreeCrossoverSinglePointStrict crossover !", ValueError)

   momRandom = None
   dadRandom = None
   
   for i in xrange(max_attempt):

      if distr_leaf is None:
         dadRandom = gDad.getRandomNode()
         momRandom = gMom.getRandomNode()
      else:
         if utils.random_flip_coin(distr_leaf):
            momRandom = gMom.getRandomNode(1)
         else: 
            momRandom = gMom.getRandomNode(2)

         if utils.random_flip_coin(distr_leaf):
            dadRandom = gDad.getRandomNode(1)
         else:
            dadRandom = gDad.getRandomNode(2)

      assert momRandom is not None
      assert dadRandom is not None

      # Optimize here
      mH = gMom.getNodeHeight(momRandom)
      dH = gDad.getNodeHeight(dadRandom)

      mD = gMom.getNodeDepth(momRandom)
      dD = gDad.getNodeDepth(dadRandom)

      # The depth of the crossover is greater than the max_depth
      if (dD+mH <= max_depth) and (mD+dH <= max_depth):
         break

   if i == (max_attempt-1):
      assert gMom.get_height() <= max_depth
      return (gMom, gDad)
   else:
      nodeMom, nodeDad = momRandom, dadRandom

   nodeMom_parent = nodeMom.getParent()
   nodeDad_parent = nodeDad.getParent()

   # Sister
   if args["count"] >= 1:
      sister = gMom
      nodeDad.setParent(nodeMom_parent)

      if nodeMom_parent is None:
         sister.setRoot(nodeDad)
      else:
         nodeMom_parent.replaceChild(nodeMom, nodeDad)
      sister.processNodes()
      assert sister.get_height() <= max_depth

   # Brother
   if args["count"] == 2:
      brother = gDad
      nodeMom.setParent(nodeDad_parent)

      if nodeDad_parent is None:
         brother.setRoot(nodeMom)
      else:
         nodeDad_parent.replaceChild(nodeDad, nodeMom)
      brother.processNodes()
      assert brother.get_height() <= max_depth

   return (sister, brother)

#############################################################################
#################  GTreeGP crossovers  ######################################
#############################################################################

def GTreeGPCrossoverSinglePoint(genome, **args):
   """ The crossover of the GTreeGP, Single Point for Genetic Programming

   ..note:: This crossover method creates offspring with restriction of the
            *max_depth* parameter.
   
   Accepts the *max_attempt* parameter, *max_depth* (required).   
   """
   sister = None
   brother = None

   gMom = args["mom"].clone()
   gDad = args["dad"].clone()

   gMom.reset_stats()
   gDad.reset_stats()

   max_depth   = gMom.get_param("max_depth", None)
   max_attempt = gMom.get_param("max_attempt", 15)

   if max_depth is None:
      utils.raise_exception("You must specify the max_depth genome parameter !", ValueError)
      
   if max_depth < 0:
      utils.raise_exception("The max_depth must be >= 1, if you want to use GTreeCrossoverSinglePointStrict crossover !", ValueError)

   momRandom = None
   dadRandom = None
   
   for i in xrange(max_attempt):

      dadRandom = gDad.getRandomNode()

      if   dadRandom.getType() == nodeType["TERMINAL"]:
         momRandom = gMom.getRandomNode(1)
      elif dadRandom.getType() == nodeType["NONTERMINAL"]:
         momRandom = gMom.getRandomNode(2)

      mD = gMom.getNodeDepth(momRandom)
      dD = gDad.getNodeDepth(dadRandom)

      # Two nodes are root
      if mD==0 and dD==0: continue
      
      mH = gMom.getNodeHeight(momRandom)
      if dD+mH > max_depth: continue

      dH = gDad.getNodeHeight(dadRandom)
      if mD+dH > max_depth: continue

      break

   if i==(max_attempt-1):
      assert gMom.get_height() <= max_depth
      return (gMom, gDad)
   else:
      nodeMom, nodeDad = momRandom, dadRandom

   nodeMom_parent = nodeMom.getParent()
   nodeDad_parent = nodeDad.getParent()

   # Sister
   if args["count"] >= 1:
      sister = gMom
      nodeDad.setParent(nodeMom_parent)

      if nodeMom_parent is None:
         sister.setRoot(nodeDad)
      else:
         nodeMom_parent.replaceChild(nodeMom, nodeDad)
      sister.processNodes()
      assert sister.get_height() <= max_depth

   # Brother
   if args["count"] == 2:
      brother = gDad
      nodeMom.setParent(nodeDad_parent)

      if nodeDad_parent is None:
         brother.setRoot(nodeMom)
      else:
         nodeDad_parent.replaceChild(nodeDad, nodeMom)
      brother.processNodes()
      assert brother.get_height() <= max_depth

   return (sister, brother)



