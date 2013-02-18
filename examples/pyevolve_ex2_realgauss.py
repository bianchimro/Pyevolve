from pyevolve import GSimpleGA
from pyevolve import g1dlist
from pyevolve import Selectors
from pyevolve import Initializators, Mutators

# Find negative element
def eval_func(genome):
   score = 0.0

   for element in genome:
      if element < 0: score += 0.1

   return score

def run_main():
   # Genome instance
   genome = g1dlist.G1DList(20)
   genome.set_params(rangemin=-6.0, rangemax=6.0)

   # Change the initializator to Real values
   genome.initializator.set(Initializators.G1DListInitializatorReal)

   # Change the mutator to Gaussian Mutator
   genome.mutator.set(Mutators.G1DListMutatorRealGaussian)

   # The evaluator function (objective function)
   genome.evaluator.set(eval_func)

   # Genetic Algorithm Instance
   ga = GSimpleGA.GSimpleGA(genome)
   ga.selector.set(Selectors.GRouletteWheel)
   ga.setGenerations(100)

   # Do the evolution
   ga.evolve(freq_stats=10)

   # Best individual
   print ga.bestIndividual()

if __name__ == "__main__":
   run_main()

