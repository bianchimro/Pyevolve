from .. import utils
from random import randint as rand_randint, gauss as rand_gauss, uniform as rand_uniform
from random import choice as rand_choice

from .. constants import CDefRangeMin, CDefRangeMax, CDefGaussianGradientMU, CDefGaussianGradientSIGMA
CDefG1DListMutIntMU = 2
CDefG1DListMutIntSIGMA = 10

CDefG1DListMutRealMU = 0
CDefG1DListMutRealSIGMA = 1


#############################
##     1D Binary String    ##
#############################

def G1DBinaryStringMutatorSwap(genome, **args):
   """ The 1D Binary String Swap Mutator """

   if args["pmut"] <= 0.0: return 0
   stringLength = len(genome)
   mutations = args["pmut"] * (stringLength)
   
   if mutations < 1.0:
      mutations = 0
      for it in xrange(stringLength):
         if utils.random_flip_coin(args["pmut"]):
            utils.list_swap_element(genome, it, rand_randint(0, stringLength-1))
            mutations+=1

   else:
      for it in xrange(int(round(mutations))):
         utils.list_swap_element(genome, rand_randint(0, stringLength-1),
                                      rand_randint(0, stringLength-1))

   return int(mutations)

def G1DBinaryStringMutatorFlip(genome, **args):
   """ The classical flip mutator for binary strings """
   if args["pmut"] <= 0.0: return 0
   stringLength = len(genome)
   mutations = args["pmut"] * (stringLength)
   
   if mutations < 1.0:
      mutations = 0
      for it in xrange(stringLength):
         if utils.random_flip_coin(args["pmut"]):
            if genome[it] == 0: genome[it] = 1
            else: genome[it] = 0
            mutations+=1

   else:
      for it in xrange(int(round(mutations))):
         which = rand_randint(0, stringLength-1)
         if genome[which] == 0: genome[which] = 1
         else: genome[which] = 0

   return int(mutations)

####################
##     1D List    ##
####################

def G1DListMutatorSwap(genome, **args):
   """ The mutator of G1DList, Swap Mutator
   
   .. note:: this mutator is :term:`Data Type Independent`

   """
   if args["pmut"] <= 0.0: return 0
   listSize = len(genome) - 1
   mutations = args["pmut"] * (listSize+1)

   if mutations < 1.0:
      mutations = 0
      for it in xrange(listSize+1):
         if utils.random_flip_coin(args["pmut"]):
            utils.list_swap_element(genome, it, rand_randint(0, listSize))
            mutations+=1
   else:
      for it in xrange(int(round(mutations))):
         utils.list_swap_element(genome, rand_randint(0, listSize), rand_randint(0, listSize))

   return int(mutations)

def G1DListMutatorSIM(genome, **args):
   """ The mutator of G1DList, Simple Inversion Mutation
   
   .. note:: this mutator is :term:`Data Type Independent`

   """
   mutations = 0
   if args["pmut"] <= 0.0: return 0

   cuts = [rand_randint(0, len(genome)), rand_randint(0, len(genome))]

   if cuts[0] > cuts[1]:
      utils.list_swap_element(cuts, 0, 1)

   if (cuts[1]-cuts[0]) <= 0:
      cuts[1] = rand_randint(cuts[0], len(genome))

   if utils.random_flip_coin(args["pmut"]):
      part = genome[cuts[0]:cuts[1]]
      if len(part) == 0: return 0
      part.reverse()
      genome[cuts[0]:cuts[1]] = part
      mutations += 1
      
   return mutations

def G1DListMutatorIntegerRange(genome, **args):
   """ Simple integer range mutator for G1DList

   Accepts the *rangemin* and *rangemax* genome parameters, both optional.

   """
   if args["pmut"] <= 0.0: return 0
   listSize = len(genome)
   mutations = args["pmut"] * listSize

   if mutations < 1.0:
      mutations = 0
      for it in xrange(listSize):
         if utils.random_flip_coin(args["pmut"]):
            genome[it] = rand_randint(genome.get_param("rangemin", CDefRangeMin),
                         genome.get_param("rangemax", CDefRangeMax))
            mutations += 1
   
   else: 
      for it in xrange(int(round(mutations))):
         which_gene = rand_randint(0, listSize-1)
         genome[which_gene] = rand_randint(genome.get_param("rangemin", CDefRangeMin),
                              genome.get_param("rangemax", CDefRangeMax))

   return int(mutations)


def G1DListMutatorRealRange(genome, **args):
   """ Simple real range mutator for G1DList

   Accepts the *rangemin* and *rangemax* genome parameters, both optional.

   """
   if args["pmut"] <= 0.0: return 0
   listSize = len(genome)
   mutations = args["pmut"] * (listSize)

   if mutations < 1.0:
      mutations = 0
      for it in xrange(listSize):
         if utils.random_flip_coin(args["pmut"]):
            genome[it] = rand_uniform(genome.get_param("rangemin", CDefRangeMin),
                         genome.get_param("rangemax", CDefRangeMax))
            mutations += 1
   
   else: 
      for it in xrange(int(round(mutations))):
         which_gene = rand_randint(0, listSize-1)
         genome[which_gene] = rand_uniform(genome.get_param("rangemin", CDefRangeMin),
                              genome.get_param("rangemax", CDefRangeMax))

   return int(mutations)

def G1DListMutatorIntegerGaussianGradient(genome, **args):
   """ A gaussian mutator for G1DList of Integers

   Accepts the *rangemin* and *rangemax* genome parameters, both optional. The
   random distribution is set with mu=1.0 and std=0.0333
   
   Same as IntegerGaussian, except that this uses relative gradient rather than
   absolute gaussian. A value is randomly generated about gauss(mu=1, sigma=.0333)
   and multiplied by the gene to drift it up or down (depending on what side of
   1 the random value falls on) and cast to integer

   """
   if args["pmut"] <= 0.0: return 0
   listSize = len(genome)
   mutations = args["pmut"] * (listSize)
   
   mu = CDefGaussianGradientMU
   sigma = CDefGaussianGradientSIGMA

   if mutations < 1.0:
      mutations = 0
      for it in xrange(listSize):
         if utils.random_flip_coin(args["pmut"]):
            final_value = int(genome[it] * abs(rand_gauss(mu, sigma)))

            final_value = min(final_value, genome.get_param("rangemax", CDefRangeMax))
            final_value = max(final_value, genome.get_param("rangemin", CDefRangeMin))

            genome[it] = final_value
            mutations += 1
   else: 
      for it in xrange(int(round(mutations))):
         which_gene = rand_randint(0, listSize-1)
         final_value = int(genome[which_gene] * abs(rand_gauss(mu, sigma)))

         final_value = min(final_value, genome.get_param("rangemax", CDefRangeMax))
         final_value = max(final_value, genome.get_param("rangemin", CDefRangeMin))

         genome[which_gene] = final_value

   return int(mutations)

def G1DListMutatorIntegerGaussian(genome, **args):
   """ A gaussian mutator for G1DList of Integers

   Accepts the *rangemin* and *rangemax* genome parameters, both optional. Also
   accepts the parameter *gauss_mu* and the *gauss_sigma* which respectively
   represents the mean and the std. dev. of the random distribution.

   """
   if args["pmut"] <= 0.0: return 0
   listSize = len(genome)
   mutations = args["pmut"] * (listSize)
   
   mu = genome.get_param("gauss_mu")
   sigma = genome.get_param("gauss_sigma")

   if mu is None:
      mu = CDefG1DListMutIntMU
   
   if sigma is None:
      sigma = CDefG1DListMutIntSIGMA

   if mutations < 1.0:
      mutations = 0
      for it in xrange(listSize):
         if utils.random_flip_coin(args["pmut"]):
            final_value = genome[it] + int(rand_gauss(mu, sigma))

            final_value = min(final_value, genome.get_param("rangemax", CDefRangeMax))
            final_value = max(final_value, genome.get_param("rangemin", CDefRangeMin))

            genome[it] = final_value
            mutations += 1
   else: 
      for it in xrange(int(round(mutations))):
         which_gene = rand_randint(0, listSize-1)
         final_value = genome[which_gene] + int(rand_gauss(mu, sigma))

         final_value = min(final_value, genome.get_param("rangemax", CDefRangeMax))
         final_value = max(final_value, genome.get_param("rangemin", CDefRangeMin))

         genome[which_gene] = final_value

   return int(mutations)


def G1DListMutatorRealGaussian(genome, **args):
   """ The mutator of G1DList, Gaussian Mutator

   Accepts the *rangemin* and *rangemax* genome parameters, both optional. Also
   accepts the parameter *gauss_mu* and the *gauss_sigma* which respectively
   represents the mean and the std. dev. of the random distribution.

   """
   if args["pmut"] <= 0.0: return 0
   listSize = len(genome)
   mutations = args["pmut"] * (listSize)

   mu = genome.get_param("gauss_mu")
   sigma = genome.get_param("gauss_sigma")

   if mu is None:
      mu = CDefG1DListMutRealMU
   
   if sigma is None:
      sigma = CDefG1DListMutRealSIGMA

   if mutations < 1.0:
      mutations = 0
      for it in xrange(listSize):
         if utils.random_flip_coin(args["pmut"]):
            final_value = genome[it] + rand_gauss(mu, sigma)

            final_value = min(final_value, genome.get_param("rangemax", CDefRangeMax))
            final_value = max(final_value, genome.get_param("rangemin", CDefRangeMin))

            genome[it] = final_value
            mutations += 1
   else:
      for it in xrange(int(round(mutations))):
         which_gene = rand_randint(0, listSize-1)
         final_value = genome[which_gene] + rand_gauss(mu, sigma)

         final_value = min(final_value, genome.get_param("rangemax", CDefRangeMax))
         final_value = max(final_value, genome.get_param("rangemin", CDefRangeMin))

         genome[which_gene] = final_value

   return int(mutations)

def G1DListMutatorRealGaussianGradient(genome, **args):
   """ The mutator of G1DList, Gaussian Gradient Mutator

   Accepts the *rangemin* and *rangemax* genome parameters, both optional. The
   random distribution is set with mu=1.0 and std=0.0333
   
   The difference between this routine and the normal Gaussian Real is that the
   other function generates a gaussian value and adds it to the value. If the 
   mu is 0, and the std is 1, a typical value could be 1.8 or -0.5. These small
   values are fine if your range is 0-10, but if your range is much larger, like
   0-100,000, a relative gradient makes sense.
   
   This routine generates a gaussian value with mu=1.0 and std=0.0333 and then
   the gene is multiplied by this value. This will cause the gene to drift
   no matter how large it is.

   """
   if args["pmut"] <= 0.0: return 0
   listSize = len(genome)
   mutations = args["pmut"] * (listSize)

   mu = CDefGaussianGradientMU
   sigma = CDefGaussianGradientSIGMA

   if mutations < 1.0:
      mutations = 0
      for it in xrange(listSize):
         if utils.random_flip_coin(args["pmut"]):
            final_value = genome[it] * abs(rand_gauss(mu, sigma))

            final_value = min(final_value, genome.get_param("rangemax", CDefRangeMax))
            final_value = max(final_value, genome.get_param("rangemin", CDefRangeMin))

            genome[it] = final_value
            mutations += 1
   else:
      for it in xrange(int(round(mutations))):
         which_gene = rand_randint(0, listSize-1)
         final_value = genome[which_gene] * abs(rand_gauss(mu, sigma))

         final_value = min(final_value, genome.get_param("rangemax", CDefRangeMax))
         final_value = max(final_value, genome.get_param("rangemin", CDefRangeMin))

         genome[which_gene] = final_value

   return int(mutations)

def G1DListMutatorIntegerBinary(genome, **args):
   """ The mutator of G1DList, the binary mutator

   This mutator will random change the 0 and 1 elements of the 1D List.

   """
   if args["pmut"] <= 0.0: return 0
   listSize = len(genome)
   mutations = args["pmut"] * (listSize)

   if mutations < 1.0:
      mutations = 0
      for it in xrange(listSize):
         if utils.random_flip_coin(args["pmut"]):
            if genome[it] == 0: genome[it] = 1
            elif genome[it] == 1: genome[it] = 0

            mutations += 1
   else:
      for it in xrange(int(round(mutations))):
         which_gene = rand_randint(0, listSize-1)
         if genome[which_gene] == 0: genome[which_gene] = 1
         elif genome[which_gene] == 1: genome[which_gene] = 0

   return int(mutations)

def G1DListMutatorAllele(genome, **args):
   """ The mutator of G1DList, Allele Mutator

   To use this mutator, you must specify the *allele* genome parameter with the
   :class:`GAllele.GAlleles` instance.

   """
   if args["pmut"] <= 0.0: return 0
   listSize = len(genome) - 1
   mutations = args["pmut"] * (listSize+1)

   allele = genome.get_param("allele", None)
   if allele is None:
      utils.raise_exception("to use the G1DListMutatorAllele, you must specify the 'allele' parameter", TypeError)

   if mutations < 1.0:
      mutations = 0
      for it in xrange(listSize+1):
         if utils.random_flip_coin(args["pmut"]):
            new_val = allele[it].getRandomAllele()
            genome[it] = new_val
            mutations+=1
   else:
      for it in xrange(int(round(mutations))):
         which_gene = rand_randint(0, listSize)
         new_val = allele[which_gene].getRandomAllele()
         genome[which_gene] = new_val

   return int(mutations)