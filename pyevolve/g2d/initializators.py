from random import randint as rand_randint, uniform as rand_uniform, choice as rand_choice
from .. import utils

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
