from pyevolve.g1d import g1dlist
from pyevolve import mutators, initializators
from pyevolve import GSimpleGA, constants

# This is the Sphere Function
def sphere(xlist):
   total = 0
   for i in xlist:
      total += i**2
   return total

def test_run_main():
   genome = g1dlist.G1DList(140)
   genome.set_params(rangemin=-5.12, rangemax=5.13)
   genome.initializator.set(initializators.G1DListInitializatorReal)
   genome.mutator.set(mutators.G1DListMutatorRealGaussian)
   genome.evaluator.set(sphere)

   ga = GSimpleGA.GSimpleGA(genome, seed=666)
   ga.setMinimax(constants.minimaxType["minimize"])
   ga.setGenerations(1500)
   ga.setMutationRate(0.01)
   ga.evolve(freq_stats=500)

   best = ga.bestIndividual()

if __name__ == "__main__":
   test_run_main()
   

