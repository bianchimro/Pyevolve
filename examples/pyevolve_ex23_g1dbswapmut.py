from pyevolve.g1d import G1DBinaryString
from pyevolve import GSimpleGA
from pyevolve import selectors
from pyevolve import mutators

# This function is the evaluation function, we want
# to give high score to more zero'ed chromosomes
def eval_func(chromosome):
   score = 0.0

   # iterate over the chromosome
   for value in chromosome:
      if value == 0:
         score += 0.1
      
   return score

def test_run_main():
   # Genome instance
   genome = G1DBinaryString.G1DBinaryString(50)

   # The evaluator function (objective function)
   genome.evaluator.set(eval_func)
   genome.mutator.set(mutators.G1DBinaryStringMutatorSwap)

   # Genetic Algorithm Instance
   ga = GSimpleGA.GSimpleGA(genome)
   ga.selector.set(selectors.GTournamentSelector)
   ga.setGenerations(70)

   # Do the evolution, with stats dump
   # frequency of 10 generations
   ga.evolve(freq_stats=20)

   # Best individual
   print ga.bestIndividual()

if __name__ == "__main__":
   test_run_main()
   