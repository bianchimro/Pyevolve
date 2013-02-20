from .. import utils
from random import randint as rand_randint, gauss as rand_gauss, uniform as rand_uniform
from random import choice as rand_choice
import gtree_utils
from .. constants import CDefRangeMin, CDefRangeMax


#################
##     Tree    ##
#################
def GTreeMutatorSwap(genome, **args):
   """ The mutator of GTree, Swap Mutator
   
   .. versionadded:: 0.6
      The *GTreeMutatorSwap* function
   """
   if args["pmut"] <= 0.0: return 0
   elements = len(genome)
   mutations = args["pmut"] * elements

   if mutations < 1.0:
      mutations = 0
      for i in xrange(len(genome)):
         if utils.random_flip_coin(args["pmut"]):
            mutations += 1
            nodeOne = genome.getRandomNode()
            nodeTwo = genome.getRandomNode()
            nodeOne.swapNodeData(nodeTwo)
   else: 
      for it in xrange(int(round(mutations))):
         nodeOne = genome.getRandomNode()
         nodeTwo = genome.getRandomNode()
         nodeOne.swapNodeData(nodeTwo)

   return int(mutations)


def GTreeMutatorIntegerRange(genome, **args):
   """ The mutator of GTree, Integer Range Mutator
   
   Accepts the *rangemin* and *rangemax* genome parameters, both optional.

   .. versionadded:: 0.6
      The *GTreeMutatorIntegerRange* function
   """
   if args["pmut"] <= 0.0: return 0
   elements = len(genome)
   mutations = args["pmut"] * elements

   range_min = genome.get_param("rangemin", CDefRangeMin)
   range_max = genome.get_param("rangemax", CDefRangeMax)

   if mutations < 1.0:
      mutations = 0
      for i in xrange(len(genome)):
         if utils.random_flip_coin(args["pmut"]):
            mutations += 1
            rand_node = genome.getRandomNode()
            random_int = rand_randint(range_min, range_max)
            rand_node.setData(random_int)

   else: 
      for it in xrange(int(round(mutations))):
         rand_node = genome.getRandomNode()
         random_int = rand_randint(range_min, range_max)
         rand_node.setData(random_int)

   return int(mutations)


def GTreeMutatorRealRange(genome, **args):
   """ The mutator of GTree, Real Range Mutator
   
   Accepts the *rangemin* and *rangemax* genome parameters, both optional.

   .. versionadded:: 0.6
      The *GTreeMutatorRealRange* function
   """
   if args["pmut"] <= 0.0: return 0
   elements = len(genome)
   mutations = args["pmut"] * elements

   range_min = genome.get_param("rangemin", CDefRangeMin)
   range_max = genome.get_param("rangemax", CDefRangeMax)

   if mutations < 1.0:
      mutations = 0
      for i in xrange(len(genome)):
         if utils.random_flip_coin(args["pmut"]):
            mutations += 1
            rand_node = genome.getRandomNode()
            random_real = rand_uniform(range_min, range_max)
            rand_node.setData(random_real)

   else: 
      for it in xrange(int(round(mutations))):
         rand_node = genome.getRandomNode()
         random_real = rand_uniform(range_min, range_max)
         rand_node.setData(random_real)

   return int(mutations)


def GTreeMutatorIntegerGaussian(genome, **args):
   """ A gaussian mutator for GTree of Integers

   Accepts the *rangemin* and *rangemax* genome parameters, both optional. Also
   accepts the parameter *gauss_mu* and the *gauss_sigma* which respectively
   represents the mean and the std. dev. of the random distribution.

   """
   if args["pmut"] <= 0.0: return 0
   elements = len(genome)
   mutations = args["pmut"] * elements

   mu = genome.get_param("gauss_mu", CDefG1DListMutIntMU)
   sigma = genome.get_param("gauss_sigma", CDefG1DListMutIntSIGMA)

   if mutations < 1.0:
      mutations = 0
      for i in xrange(len(genome)):
         if utils.random_flip_coin(args["pmut"]):
            mutations += 1
            rand_node = genome.getRandomNode()
            final_value = rand_node.getData() + int(rand_gauss(mu, sigma))
            final_value = min(final_value, genome.get_param("rangemax", CDefRangeMax))
            final_value = max(final_value, genome.get_param("rangemin", CDefRangeMin))
            rand_node.setData(final_value)
   else: 
      for it in xrange(int(round(mutations))):
         rand_node = genome.getRandomNode()
         final_value = rand_node.getData() + int(rand_gauss(mu, sigma))
         final_value = min(final_value, genome.get_param("rangemax", CDefRangeMax))
         final_value = max(final_value, genome.get_param("rangemin", CDefRangeMin))
         rand_node.setData(final_value)

   return int(mutations)


def GTreeMutatorRealGaussian(genome, **args):
   """ A gaussian mutator for GTree of Real numbers

   Accepts the *rangemin* and *rangemax* genome parameters, both optional. Also
   accepts the parameter *gauss_mu* and the *gauss_sigma* which respectively
   represents the mean and the std. dev. of the random distribution.

   """
   if args["pmut"] <= 0.0: return 0
   elements = len(genome)
   mutations = args["pmut"] * elements

   mu = genome.get_param("gauss_mu", CDefG1DListMutRealMU)
   sigma = genome.get_param("gauss_sigma", CDefG1DListMutRealSIGMA)

   if mutations < 1.0:
      mutations = 0
      for i in xrange(len(genome)):
         if utils.random_flip_coin(args["pmut"]):
            mutations += 1
            rand_node = genome.getRandomNode()
            final_value = rand_node.getData() + rand_gauss(mu, sigma)
            final_value = min(final_value, genome.get_param("rangemax", CDefRangeMax))
            final_value = max(final_value, genome.get_param("rangemin", CDefRangeMin))
            rand_node.setData(final_value)
   else: 
      for it in xrange(int(round(mutations))):
         rand_node = genome.getRandomNode()
         final_value = rand_node.getData() + rand_gauss(mu, sigma)
         final_value = min(final_value, genome.get_param("rangemax", CDefRangeMax))
         final_value = max(final_value, genome.get_param("rangemin", CDefRangeMin))
         rand_node.setData(final_value)

   return int(mutations)



###################
##     Tree GP   ##
###################

def GTreeGPMutatorOperation(genome, **args):
   """ The mutator of GTreeGP, Operation Mutator
   
   .. versionadded:: 0.6
      The *GTreeGPMutatorOperation* function
   """

   if args["pmut"] <= 0.0: return 0
   elements = len(genome)
   mutations = args["pmut"] * elements
   ga_engine = args["ga_engine"]


   gp_terminals = ga_engine.get_param("gp_terminals")
   assert gp_terminals is not None

   gp_function_set = ga_engine.get_param("gp_function_set")
   assert gp_function_set is not None

   if mutations < 1.0:
      mutations = 0
      for i in xrange(len(genome)):
         if utils.random_flip_coin(args["pmut"]):
            mutations += 1
            rand_node = genome.getRandomNode()
            assert rand_node is not None
            if rand_node.getType() == nodeType["TERMINAL"]:
               term_operator = rand_choice(gp_terminals)
            else:
               op_len = gp_function_set[rand_node.getData()]
               fun_candidates = []
               for o, l in gp_function_set.items():
                  if l==op_len:
                     fun_candidates.append(o)

               if len(fun_candidates) <= 0:
                  continue

               term_operator = rand_choice(fun_candidates)
            rand_node.setData(term_operator)
   else: 
      for it in xrange(int(round(mutations))):
         rand_node = genome.getRandomNode()
         assert rand_node is not None
         if rand_node.getType() == nodeType["TERMINAL"]:
            term_operator = rand_choice(gp_terminals)
         else:
            op_len = gp_function_set[rand_node.getData()]
            fun_candidates = []
            for o, l in gp_function_set.items():
               if l==op_len:
                  fun_candidates.append(o)

            if len(fun_candidates) <= 0:
               continue
            
            term_operator = rand_choice(fun_candidates)
         rand_node.setData(term_operator)

   return int(mutations)


def GTreeGPMutatorSubtree(genome, **args):
   """ The mutator of GTreeGP, Subtree Mutator

   This mutator will recreate random subtree of the tree using the grow algorithm.
   
   .. versionadded:: 0.6
      The *GTreeGPMutatorSubtree* function
   """

   if args["pmut"] <= 0.0: return 0
   ga_engine = args["ga_engine"]
   max_depth = genome.get_param("max_depth", None)
   mutations = 0

   if max_depth is None:
      utils.raise_exception("You must specify the max_depth genome parameter !", ValueError)
      
   if max_depth < 0:
      utils.raise_exception("The max_depth must be >= 1, if you want to use GTreeGPMutatorSubtree crossover !", ValueError)

   branch_list = genome.nodes_branch
   elements = len(branch_list)
   
   for i in xrange(elements):

      node = branch_list[i]
      assert node is not None

      if utils.random_flip_coin(args["pmut"]):
         depth = genome.getNodeDepth(node)
         mutations += 1

         root_subtree = gtree_utils.buildGTreeGPGrow(ga_engine, 0, max_depth-depth)
         node_parent = node.getParent()

         if node_parent is None:
            genome.setRoot(root_subtree)
            genome.processNodes()
            return mutations
         else:
            root_subtree.setParent(node_parent)
            node_parent.replaceChild(node, root_subtree)
         genome.processNodes()
   
   return int(mutations)


