"""

:mod:`initializators` -- initialization methods module
===================================================================

In this module we have the genetic operators of initialization for each
chromosome representation, the most part of initialization is done by
choosing random data.

.. note:: In Pyevolve, the Initializator defines the data type that will
          be used on the chromosome, for example, the :func:`G1DListInitializatorInteger`
          will initialize the G1DList with Integers.
          

"""

from random import randint as rand_randint, uniform as rand_uniform, choice as rand_choice
from gtree import gtree_utils
import utils

#############################
##     1D Binary String    ##
#############################

def G1DBinaryStringInitializator(genome, **args):
   """ 1D Binary String initializator """
   genome.genomeList = [ rand_choice((0,1)) for i in xrange(genome.get_list_size()) ]

#############################
##     2D Binary String    ##
#############################

def G2DBinaryStringInitializator(genome, **args):
   """ Integer initialization function of 2D Binary String
   
   .. versionadded:: 0.6
      The *G2DBinaryStringInitializator* function
   """
   genome.clear_string()
   
   for i in xrange(genome.get_height()):
      for j in xrange(genome.get_width()):
         random_gene = rand_choice((0,1))
         genome.set_item(i, j, random_gene)


####################
##     1D List    ##
####################

def G1DListInitializatorAllele(genome, **args):
   """ Allele initialization function of G1DList

   To use this initializator, you must specify the *allele* genome parameter with the
   :class:`GAllele.GAlleles` instance.

   """

   allele = genome.get_param("allele", None)
   if allele is None:
      utils.raise_exception("to use the G1DListInitializatorAllele, you must specify the 'allele' parameter")

   genome.genomeList = [ allele[i].getRandomAllele() for i in xrange(genome.get_list_size())  ]

def G1DListInitializatorInteger(genome, **args):
   """ Integer initialization function of G1DList

   This initializator accepts the *rangemin* and *rangemax* genome parameters.

   """
   range_min = genome.get_param("rangemin", 0)
   range_max = genome.get_param("rangemax", 100)

   genome.genomeList = [rand_randint(range_min, range_max) for i in xrange(genome.get_list_size())]

def G1DListInitializatorReal(genome, **args):
   """ Real initialization function of G1DList

   This initializator accepts the *rangemin* and *rangemax* genome parameters.

   """
   range_min = genome.get_param("rangemin", 0)
   range_max = genome.get_param("rangemax", 100)

   genome.genomeList = [rand_uniform(range_min, range_max) for i in xrange(genome.get_list_size())]


####################
##     2D List    ##
####################

def G2DListInitializatorInteger(genome, **args):
   """ Integer initialization function of G2DList

   This initializator accepts the *rangemin* and *rangemax* genome parameters.
   
   """
   genome.clear_list()
   
   for i in xrange(genome.get_height()):
      for j in xrange(genome.get_width()):
         randomInteger = rand_randint(genome.get_param("rangemin", 0),
                                      genome.get_param("rangemax", 100))
         genome.set_item(i, j, randomInteger)


def G2DListInitializatorReal(genome, **args):
   """ Integer initialization function of G2DList

   This initializator accepts the *rangemin* and *rangemax* genome parameters.

   """
   genome.clear_list()
   
   for i in xrange(genome.get_height()):
      for j in xrange(genome.get_width()):
         randomReal = rand_uniform(genome.get_param("rangemin", 0),
                                   genome.get_param("rangemax", 100))
         genome.set_item(i, j, randomReal)

def G2DListInitializatorAllele(genome, **args):
   """ Allele initialization function of G2DList

   To use this initializator, you must specify the *allele* genome parameter with the
   :class:`GAllele.GAlleles` instance.

   .. warning:: the :class:`GAllele.GAlleles` instance must have the homogeneous flag enabled

   """

   allele = genome.get_param("allele", None)
   if allele is None:
      utils.raise_exception("to use the G2DListInitializatorAllele, you must specify the 'allele' parameter")

   if allele.homogeneous == False:
      utils.raise_exception("to use the G2DListInitializatorAllele, the 'allele' must be homogeneous")

   genome.clear_list()
   
   for i in xrange(genome.get_height()):
      for j in xrange(genome.get_width()):
         random_allele = allele[0].getRandomAllele()
         genome.set_item(i, j, random_allele)

####################
##      Tree      ##
####################

def GTreeInitializatorInteger(genome, **args):
   """ Integer initialization function of GTree

   This initializator accepts the *rangemin* and *rangemax* genome parameters.
   It accepts the following parameters too:
      
   *max_depth*
      The max depth of the tree

   *max_siblings*
      The number of maximum siblings of an node

   *method*
      The method, accepts "grow", "full" or "ramped".

   .. versionadded:: 0.6
      The *GTreeInitializatorInteger* function.
   """
   max_depth = genome.get_param("max_depth", 5)
   max_siblings = genome.get_param("max_siblings", 2)

   range_min = genome.get_param("rangemin", 0)
   range_max = genome.get_param("rangemax", 100)

   lambda_generator = lambda: rand_randint(range_min, range_max)

   method = genome.get_param("method", "grow")

   if method == "grow":
      root = gtree_utils.buildGTreeGrow(0, lambda_generator, max_siblings, max_depth)
   elif method == "full":
      root = gtree_utils.buildGTreeFull(0, lambda_generator, max_siblings, max_depth)
   elif method == "ramped":
      if utils.random_flip_coin(0.5):
         root = gtree_utils.buildGTreeGrow(0, lambda_generator, max_siblings, max_depth)
      else:
         root = gtree_utils.buildGTreeFull(0, lambda_generator, max_siblings, max_depth)
   else:
      utils.raise_exception("Unknown tree initialization method [%s] !" % method)

   genome.setRoot(root)
   genome.processNodes()
   assert genome.get_height() <= max_depth

def GTreeInitializatorAllele(genome, **args):
   """ Allele initialization function of GTree

   To use this initializator, you must specify the *allele* genome parameter with the
   :class:`GAllele.GAlleles` instance.

   .. warning:: the :class:`GAllele.GAlleles` instance **must** have the homogeneous flag enabled

   .. versionadded:: 0.6
      The *GTreeInitializatorAllele* function.
   """
   max_depth    = genome.get_param("max_depth", 5)
   max_siblings = genome.get_param("max_siblings", 2)
   method       = genome.get_param("method", "grow")

   allele = genome.get_param("allele", None)
   if allele is None:
      utils.raise_exception("to use the GTreeInitializatorAllele, you must specify the 'allele' parameter")

   if allele.homogeneous == False:
      utils.raise_exception("to use the GTreeInitializatorAllele, the 'allele' must be homogeneous")

   if method == "grow":
      root = gtree_utils.buildGTreeGrow(0, allele[0].getRandomAllele, max_siblings, max_depth)
   elif method == "full":
      root = gtree_utils.buildGTreeFull(0, allele[0].getRandomAllele, max_siblings, max_depth)
   elif method == "ramped":
      if utils.random_flip_coin(0.5):
         root = gtree_utils.buildGTreeGrow(0, allele[0].getRandomAllele, max_siblings, max_depth)
      else:
         root = gtree_utils.buildGTreeFull(0, allele[0].getRandomAllele, max_siblings, max_depth)
   else:
      utils.raise_exception("Unknown tree initialization method [%s] !" % method)


   genome.setRoot(root)
   genome.processNodes()
   assert genome.get_height() <= max_depth

####################
##      Tree GP   ##
####################

def GTreeGPInitializator(genome, **args):
   """This initializator accepts the follow parameters:
      
   *max_depth*
      The max depth of the tree

   *method*
      The method, accepts "grow", "full" or "ramped"

   .. versionadded:: 0.6
      The *GTreeGPInitializator* function.
   """

   max_depth = genome.get_param("max_depth", 5)
   method    = genome.get_param("method", "grow")
   ga_engine = args["ga_engine"]

   if method == "grow":
      root = gtree_utils.buildGTreeGPGrow(ga_engine, 0, max_depth)
   elif method == "full":
      root = gtree_utils.buildGTreeGPFull(ga_engine, 0, max_depth)
   elif method == "ramped":
      if utils.random_flip_coin(0.5):
         root = gtree_utils.buildGTreeGPFull(ga_engine, 0, max_depth)
      else:
         root = gtree_utils.buildGTreeGPGrow(ga_engine, 0, max_depth)
   else:
      utils.raise_exception("Unknown tree initialization method [%s] !" % method)

   genome.setRoot(root)
   genome.processNodes()
   assert genome.get_height() <= max_depth
