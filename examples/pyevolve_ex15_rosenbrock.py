from pyevolve import g1d
from pyevolve import algorithm, selectors, statistics
from pyevolve import constants
from pyevolve import db

# This is the Rosenbrock Function
def rosenbrock(xlist):
   sum_var = 0
   for x in xrange(1, len(xlist)):
      sum_var += 100.0 * (xlist[x] - xlist[x-1]**2)**2 + (1 - xlist[x-1])**2
   return sum_var

def test_run_main():
   # Genome instance
   genome = g1d.G1DList(15)
   genome.set_params(rangemin=-1, rangemax=1.1)
   genome.initializator.set(g1d.initializators.G1DListInitializatorReal)
   genome.mutator.set(g1d.mutators.G1DListMutatorRealRange)

   # The evaluator function (objective function)
   genome.evaluator.set(rosenbrock)

   # Genetic Algorithm Instance
   ga = algorithm.GSimpleGA(genome)
   ga.setMinimax(constants.minimaxType["minimize"])
   ga.selector.set(selectors.GRouletteWheel)
   ga.setGenerations(4000)
   ga.setCrossoverRate(0.9)
   ga.setPopulationSize(100)
   ga.setMutationRate(0.03)

   ga.evolve(freq_stats=500)

   # Best individual
   best = ga.bestIndividual()
   print "\nBest individual score: %.2f" % (best.score,)
   print best


if __name__ == "__main__":
    test_run_main()













