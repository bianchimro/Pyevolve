from random import randint as rand_randint, choice as rand_choice
from random import random as rand_random
import math
from .. import utils

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