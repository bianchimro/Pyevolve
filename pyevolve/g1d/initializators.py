from random import randint as rand_randint, uniform as rand_uniform, choice as rand_choice
from .. import utils

#############################
##     1D Binary String    ##
#############################

def G1DBinaryStringInitializator(genome, **args):
   """ 1D Binary String initializator """
   genome.genomeList = [ rand_choice((0,1)) for i in xrange(genome.get_list_size()) ]



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
