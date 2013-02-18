"""

:mod:`Scaling` -- scaling schemes module
===========================================================

This module have the *scaling schemes* like Linear scaling, etc.

"""
from pyevolve import utils
import math
import logging

# - Scale methods defaults
CDefScaleLinearMultiplier     = 1.2
CDefScaleSigmaTruncMultiplier = 2.0
CDefScalePowerLawFactor       = 1.0005
CDefScaleBoltzMinTemp         = 1.0
CDefScaleBoltzFactor          = 0.05
# 40 temp. = 500 generations
CDefScaleBoltzStart           = 40.0


def LinearScaling(pop):
   """ Linear Scaling scheme

   .. warning :: Linear Scaling is only for positive raw scores

   """
   logging.debug("Running linear scaling.")
   pop.statistics()
   c = CDefScaleLinearMultiplier
   a = b = delta = 0.0

   pop_rawAve = pop.stats["rawAve"]
   pop_rawMax = pop.stats["rawMax"]
   pop_rawMin = pop.stats["rawMin"]
   
   if pop_rawAve == pop_rawMax:
      a = 1.0
      b = 0.0
   elif pop_rawMin > (c * pop_rawAve - pop_rawMax / c - 1.0):
      delta = pop_rawMax - pop_rawAve
      a = (c - 1.0) * pop_rawAve / delta
      b = pop_rawAve * (pop_rawMax - (c * pop_rawAve)) / delta
   else:
      delta = pop_rawAve - pop_rawMin
      a = pop_rawAve / delta
      b = -pop_rawMin * pop_rawAve / delta

   for i in xrange(len(pop)):
      f = pop[i].score
      if f < 0.0:
         utils.raise_exception("Score %r is negative, linear scaling not supported !" % (f,), ValueError)
      f = f * a + b
      if f < 0:
         f = 0.0
      pop[i].fitness = f

def SigmaTruncScaling(pop):
   """ Sigma Truncation scaling scheme, allows negative scores """
   logging.debug("Running sigma truncation scaling.")
   pop.statistics()
   c = CDefScaleSigmaTruncMultiplier
   pop_rawAve = pop.stats["rawAve"]
   pop_rawDev = pop.stats["rawDev"]
   for i in xrange(len(pop)):
      f = pop[i].score - pop_rawAve
      f+= c * pop_rawDev
      if f < 0: f = 0.0
      pop[i].fitness = f

def PowerLawScaling(pop):
   """ Power Law scaling scheme

   .. warning :: Power Law Scaling is only for positive raw scores

   """
   logging.debug("Running power law scaling.")
   k = CDefScalePowerLawFactor
   for i in xrange(len(pop)):
      f = pop[i].score
      if f < 0.0:
         utils.raise_exception("Score %r is negative, power law scaling not supported !" % (f,), ValueError)
      f = math.pow(f, k)
      pop[i].fitness = f


def BoltzmannScaling(pop):
   """ Boltzmann scaling scheme. You can specify the **boltz_temperature** to the
   population parameters, this parameter will set the start temperature. You
   can specify the **boltz_factor** and the **boltz_min** parameters, the **boltz_factor**
   is the value that the temperature will be subtracted and the **boltz_min** is the
   mininum temperature of the scaling scheme.
   
   .. versionadded: 0.6
      The `BoltzmannScaling` function.

   """
   boltz_temperature = pop.get_param("boltz_temperature", CDefScaleBoltzStart)
   boltz_factor      = pop.get_param("boltz_factor", CDefScaleBoltzFactor)
   boltz_min         = pop.get_param("boltz_min", CDefScaleBoltzMinTemp)

   boltz_temperature-= boltz_factor
   boltz_temperature = max(boltz_temperature, boltz_min)
   pop.set_params(boltzTemperature=boltz_temperature)

   boltz_e = []
   avg = 0.0

   for i in xrange(len(pop)):
      val = math.exp(pop[i].score / boltz_temperature)
      boltz_e.append(val)
      avg += val
      
   avg /= len(pop)

   for i in xrange(len(pop)):
      pop[i].fitness = boltz_e[i] / avg
   
def ExponentialScaling(pop):
   """ Exponential Scaling Scheme. The fitness will be the same as (e^score).

   .. versionadded: 0.6
      The `ExponentialScaling` function.
   """
   for i in xrange(len(pop)):
      score = pop[i].score
      pop[i].fitness = math.exp(score)

def SaturatedScaling(pop):
   """ Saturated Scaling Scheme. The fitness will be the same as 1.0-(e^score)

   .. versionadded: 0.6
      The `SaturatedScaling` function.
   """
   for i in xrange(len(pop)):
      score = pop[i].score
      pop[i].fitness = 1.0 - math.exp(score)


