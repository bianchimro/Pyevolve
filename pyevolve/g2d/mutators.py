from .. import utils
from random import randint as rand_randint, gauss as rand_gauss, uniform as rand_uniform
from random import choice as rand_choice
from .. constants import CDefRangeMin, CDefRangeMax, CDefGaussianGradientMU, CDefGaussianGradientSIGMA


####################
##     2D List    ##
####################

def G2DListMutatorSwap(genome, **args):
   """ The mutator of G1DList, Swap Mutator
   
   .. note:: this mutator is :term:`Data Type Independent`

   """
   
   if args["pmut"] <= 0.0: return 0
   height, width = genome.get_size()
   elements = height * width

   mutations = args["pmut"] * elements

   if mutations < 1.0:
      mutations = 0
      for i in xrange(height):
         for j in xrange(width):
            if utils.random_flip_coin(args["pmut"]):
               index_b = (rand_randint(0, height-1), rand_randint(0, width-1))
               utils.list2D_swap_element(genome.genomeList, (i,j), index_b)
               mutations+=1
   else:
      for it in xrange(int(round(mutations))):
         index_a = (rand_randint(0, height-1), rand_randint(0, width-1))
         index_b = (rand_randint(0, height-1), rand_randint(0, width-1))
         utils.list2D_swap_element(genome.genomeList, index_a, index_b)

   return int(mutations)

def G2DListMutatorIntegerRange(genome, **args):
   """ Simple integer range mutator for G2DList

   Accepts the *rangemin* and *rangemax* genome parameters, both optional.

   """
   if args["pmut"] <= 0.0: return 0
   height, width = genome.get_size()
   elements = height * width

   mutations = args["pmut"] * elements

   range_min = genome.get_param("rangemin", CDefRangeMin)
   range_max = genome.get_param("rangemax", CDefRangeMax)

   if mutations < 1.0:
      mutations = 0
      for i in xrange(genome.get_height()):
         for j in xrange(genome.get_width()):
            if utils.random_flip_coin(args["pmut"]):
               random_int = rand_randint(range_min, range_max)
               genome.set_item(i, j, random_int)
               mutations += 1

   else: 
      for it in xrange(int(round(mutations))):
         which_x = rand_randint(0, genome.get_width()-1)
         which_y = rand_randint(0, genome.get_height()-1)
         random_int = rand_randint(range_min, range_max)
         genome.set_item(which_y, which_x, random_int)

   return int(mutations)


def G2DListMutatorIntegerGaussianGradient(genome, **args):
   """ A gaussian mutator for G2DList of Integers 

   Accepts the *rangemin* and *rangemax* genome parameters, both optional.
   
   This routine generates a gaussian value with mu=1.0 and std=0.0333 and then
   the gene is multiplied by this value. This will cause the gene to drift
   no matter how large it is.

   """
   if args["pmut"] <= 0.0: return 0
   height, width = genome.get_size()
   elements = height * width

   mutations = args["pmut"] * elements

   mu = CDefGaussianGradientMU
   sigma = CDefGaussianGradientSIGMA

   if mutations < 1.0:
      mutations = 0
      
      for i in xrange(genome.get_height()):
         for j in xrange(genome.get_width()):
            if utils.random_flip_coin(args["pmut"]):
               final_value = int(genome[i][j] * abs(rand_gauss(mu, sigma)))

               final_value = min(final_value, genome.get_param("rangemax", CDefRangeMax))
               final_value = max(final_value, genome.get_param("rangemin", CDefRangeMin))

               genome.set_item(i, j, final_value)
               mutations += 1
   else: 

      for it in xrange(int(round(mutations))):
         which_x = rand_randint(0, genome.get_width()-1)
         which_y = rand_randint(0, genome.get_height()-1)

         final_value = int(genome[which_y][which_x] * abs(rand_gauss(mu, sigma)))

         final_value = min(final_value, genome.get_param("rangemax", CDefRangeMax))
         final_value = max(final_value, genome.get_param("rangemin", CDefRangeMin))

         genome.set_item(which_y, which_x, final_value)

   return int(mutations)

def G2DListMutatorIntegerGaussian(genome, **args):
   """ A gaussian mutator for G2DList of Integers 

   Accepts the *rangemin* and *rangemax* genome parameters, both optional. Also
   accepts the parameter *gauss_mu* and the *gauss_sigma* which respectively
   represents the mean and the std. dev. of the random distribution.

   """
   if args["pmut"] <= 0.0: return 0
   height, width = genome.get_size()
   elements = height * width

   mutations = args["pmut"] * elements

   mu = genome.get_param("gauss_mu")
   sigma = genome.get_param("gauss_sigma")

   if mu is None:
      mu = CDefG2DListMutIntMU
   
   if sigma is None:
      sigma = CDefG2DListMutIntSIGMA

   if mutations < 1.0:
      mutations = 0
      
      for i in xrange(genome.get_height()):
         for j in xrange(genome.get_width()):
            if utils.random_flip_coin(args["pmut"]):
               final_value = genome[i][j] + int(rand_gauss(mu, sigma))

               final_value = min(final_value, genome.get_param("rangemax", CDefRangeMax))
               final_value = max(final_value, genome.get_param("rangemin", CDefRangeMin))

               genome.set_item(i, j, final_value)
               mutations += 1
   else: 

      for it in xrange(int(round(mutations))):
         which_x = rand_randint(0, genome.get_width()-1)
         which_y = rand_randint(0, genome.get_height()-1)

         final_value = genome[which_y][which_x] + int(rand_gauss(mu, sigma))

         final_value = min(final_value, genome.get_param("rangemax", CDefRangeMax))
         final_value = max(final_value, genome.get_param("rangemin", CDefRangeMin))

         genome.set_item(which_y, which_x, final_value)

   return int(mutations)


def G2DListMutatorAllele(genome, **args):
   """ The mutator of G2DList, Allele Mutator

   To use this mutator, you must specify the *allele* genome parameter with the
   :class:`GAllele.GAlleles` instance.

   .. warning:: the :class:`GAllele.GAlleles` instance must have the homogeneous flag enabled

   """
   if args["pmut"] <= 0.0: return 0
   listSize = genome.get_height()*genome.get_width() - 1
   mutations = args["pmut"] * (listSize+1)

   allele = genome.get_param("allele", None)
   if allele is None:
      utils.raise_exception("to use the G2DListMutatorAllele, you must specify the 'allele' parameter", TypeError)

   if allele.homogeneous == False:
      utils.raise_exception("to use the G2DListMutatorAllele, the 'allele' must be homogeneous")

   if mutations < 1.0:
      mutations = 0

      for i in xrange(genome.get_height()):
         for j in xrange(genome.get_width()):
            if utils.random_flip_coin(args["pmut"]):
               new_val = allele[0].getRandomAllele()
               genome.set_item(i, j, new_val)
               mutations+=1
   else:
      for it in xrange(int(round(mutations))):
         which_x = rand_randint(0, genome.get_height()-1)
         which_y = rand_randint(0, genome.get_width()-1)

         new_val = allele[0].getRandomAllele()
         genome.set_item(which_x, which_y, new_val)

   return int(mutations)


def G2DListMutatorRealGaussian(genome, **args):
   """ A gaussian mutator for G2DList of Real 

   Accepts the *rangemin* and *rangemax* genome parameters, both optional. Also
   accepts the parameter *gauss_mu* and the *gauss_sigma* which respectively
   represents the mean and the std. dev. of the random distribution.

   """
   if args["pmut"] <= 0.0: return 0
   height, width = genome.get_size()
   elements = height * width

   mutations = args["pmut"] * elements

   mu = genome.get_param("gauss_mu")
   sigma = genome.get_param("gauss_sigma")

   if mu is None:
      mu = CDefG2DListMutRealMU
   
   if sigma is None:
      sigma = CDefG2DListMutRealSIGMA

   if mutations < 1.0:
      mutations = 0
      
      for i in xrange(genome.get_height()):
         for j in xrange(genome.get_width()):
            if utils.random_flip_coin(args["pmut"]):
               final_value = genome[i][j] + rand_gauss(mu, sigma)

               final_value = min(final_value, genome.get_param("rangemax", CDefRangeMax))
               final_value = max(final_value, genome.get_param("rangemin", CDefRangeMin))

               genome.set_item(i, j, final_value)
               mutations += 1
   else: 

      for it in xrange(int(round(mutations))):
         which_x = rand_randint(0, genome.get_width()-1)
         which_y = rand_randint(0, genome.get_height()-1)

         final_value = genome[which_y][which_x] + rand_gauss(mu, sigma)

         final_value = min(final_value, genome.get_param("rangemax", CDefRangeMax))
         final_value = max(final_value, genome.get_param("rangemin", CDefRangeMin))

         genome.set_item(which_y, which_x, final_value)

   return int(mutations)

def G2DListMutatorRealGaussianGradient(genome, **args):
   """ A gaussian gradient mutator for G2DList of Real 

   Accepts the *rangemin* and *rangemax* genome parameters, both optional.
   
   The difference is that this multiplies the gene by gauss(1.0, 0.0333), allowing
   for a smooth gradient drift about the value.

   """
   if args["pmut"] <= 0.0: return 0
   height, width = genome.get_size()
   elements = height * width

   mutations = args["pmut"] * elements

   mu = CDefGaussianGradientMU
   sigma = CDefGaussianGradientSIGMA

   if mutations < 1.0:
      mutations = 0
      
      for i in xrange(genome.get_height()):
         for j in xrange(genome.get_width()):
            if utils.random_flip_coin(args["pmut"]):
               final_value = genome[i][j] * abs(rand_gauss(mu, sigma))

               final_value = min(final_value, genome.get_param("rangemax", CDefRangeMax))
               final_value = max(final_value, genome.get_param("rangemin", CDefRangeMin))

               genome.set_item(i, j, final_value)
               mutations += 1
   else: 

      for it in xrange(int(round(mutations))):
         which_x = rand_randint(0, genome.get_width()-1)
         which_y = rand_randint(0, genome.get_height()-1)

         final_value = genome[which_y][which_x] * abs(rand_gauss(mu, sigma))

         final_value = min(final_value, genome.get_param("rangemax", CDefRangeMax))
         final_value = max(final_value, genome.get_param("rangemin", CDefRangeMin))

         genome.set_item(which_y, which_x, final_value)

   return int(mutations)

#############################
##     2D Binary String    ##
#############################

def G2DBinaryStringMutatorSwap(genome, **args):
   """ The mutator of G2DBinaryString, Swap Mutator
   
   .. versionadded:: 0.6
      The *G2DBinaryStringMutatorSwap* function
   """
   
   if args["pmut"] <= 0.0: return 0
   height, width = genome.get_size()
   elements = height * width

   mutations = args["pmut"] * elements

   if mutations < 1.0:
      mutations = 0
      for i in xrange(height):
         for j in xrange(width):
            if utils.random_flip_coin(args["pmut"]):
               index_b = (rand_randint(0, height-1), rand_randint(0, width-1))
               utils.list2D_swap_element(genome.genomeString, (i,j), index_b)
               mutations+=1
   else:
      for it in xrange(int(round(mutations))):
         index_a = (rand_randint(0, height-1), rand_randint(0, width-1))
         index_b = (rand_randint(0, height-1), rand_randint(0, width-1))
         utils.list2D_swap_element(genome.genomeString, index_a, index_b)

   return int(mutations)


def G2DBinaryStringMutatorFlip(genome, **args):
   """ A flip mutator for G2DBinaryString
   
   .. versionadded:: 0.6
      The *G2DBinaryStringMutatorFlip* function
   """
   if args["pmut"] <= 0.0: return 0
   height, width = genome.get_size()
   elements = height * width

   mutations = args["pmut"] * elements

   if mutations < 1.0:
      mutations = 0
      
      for i in xrange(genome.get_height()):
         for j in xrange(genome.get_width()):
            if utils.random_flip_coin(args["pmut"]):
               if genome[i][j] == 0: genome.set_item(i, j, 1)
               else:                 genome.set_item(i, j, 0)
               mutations += 1
   else: 

      for it in xrange(int(round(mutations))):
         which_x = rand_randint(0, genome.get_width()-1)
         which_y = rand_randint(0, genome.get_height()-1)

         if genome[i][j] == 0: genome.set_item(which_y, which_x, 1)
         else:                 genome.set_item(which_y, which_x, 0)

   return int(mutations)