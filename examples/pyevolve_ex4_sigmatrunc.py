from pyevolve.G1D import g1dlist
from pyevolve import GSimpleGA
from pyevolve import selectors
from pyevolve import initializators, mutators
from pyevolve import Scaling
from pyevolve import constants
import math

def eval_func(ind):
   score = 0.0
   var_x = ind[0]
   var_z = var_x**2+2*var_x+1*math.cos(var_x)
   return var_z

def test_run_main():
   # Genome instance
   genome = g1dlist.G1DList(1)
   genome.set_params(rangemin=-60.0, rangemax=60.0)

   # Change the initializator to Real values
   genome.initializator.set(initializators.G1DListInitializatorReal)

   # Change the mutator to Gaussian Mutator
   genome.mutator.set(mutators.G1DListMutatorRealGaussian)

   # Removes the default crossover
   genome.crossover.clear()

   # The evaluator function (objective function)
   genome.evaluator.set(eval_func)

   # Genetic Algorithm Instance
   ga = GSimpleGA.GSimpleGA(genome)
   ga.setMinimax(constants.minimaxType["minimize"])

   pop = ga.getPopulation()
   pop.scaleMethod.set(Scaling.SigmaTruncScaling)

   ga.selector.set(selectors.GRouletteWheel)
   ga.setGenerations(100)

   # Do the evolution
   ga.evolve(10)

   # Best individual
   print ga.bestIndividual()

if __name__ == "__main__":
   test_run_main()
