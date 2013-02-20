from pyevolve import algorithm
from pyevolve import g1d
from pyevolve.population import selectors
from pyevolve import constants
import math

# This is the Rastrigin Function, a deception function
def rastrigin(genome):
   n = len(genome)
   total = 0
   for i in xrange(n):
      total += genome[i]**2 - 10*math.cos(2*math.pi*genome[i])
   return (10*n) + total

def test_run_main():
   # Genome instance
   genome = g1d.G1DList(20)
   genome.set_params(rangemin=-5.2, rangemax=5.30, bestrawscore=0.00, rounddecimal=2)
   genome.initializator.set(g1d.initializators.G1DListInitializatorReal)
   genome.mutator.set(g1d.mutators.G1DListMutatorRealGaussian)

   genome.evaluator.set(rastrigin)

   # Genetic Algorithm Instance
   ga = algorithm.GSimpleGA(genome)
   ga.terminationCriteria.set(algorithm.RawScoreCriteria)
   ga.setMinimax(constants.minimaxType["minimize"])
   ga.setGenerations(3000)
   ga.setCrossoverRate(0.8)
   ga.setPopulationSize(100)
   ga.setMutationRate(0.06)

   ga.evolve(freq_stats=50)

   best = ga.bestIndividual()
   print best

if __name__ == "__main__":
   test_run_main()
