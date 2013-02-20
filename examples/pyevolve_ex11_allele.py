from pyevolve import g1d
from pyevolve import algorithm
from pyevolve import genomebase

# This function is the evaluation function, we want
# to give high score to more zero'ed chromosomes
def eval_func(chromosome):
   score = 0.0

   # iterate over the chromosome
   for value in chromosome:
      if value == 0:
         score += 0.5

   # Remember from the allele set defined above
   # this value 'a' is possible at this position
   if chromosome[18] == 'a':
      score += 1.0

   # Remember from the allele set defined above
   # this value 'xxx' is possible at this position
   if chromosome[12] == 'xxx':
      score += 1.0

   return score

def test_run_main():
   # Genome instance
   setOfAlleles = genomebase.GAlleles()

   # From 0 to 10 we can have only some
   # defined ranges of integers
   for i in xrange(11):
      a = genomebase.GAlleleRange(0, i)
      setOfAlleles.add(a)

   # From 11 to 19 we can have a set
   # of elements
   for i in xrange(11, 20):
      # You can even add objects instead of strings or 
      # primitive values
      a = genomebase.GAlleleList(['a','b', 'xxx', 666, 0])
      setOfAlleles.add(a)
      
   genome = g1d.G1DList(20)
   genome.set_params(allele=setOfAlleles)

   # The evaluator function (objective function)
   genome.evaluator.set(eval_func)

   # This mutator and initializator will take care of
   # initializing valid individuals based on the allele set
   # that we have defined before
   genome.mutator.set(g1d.mutators.G1DListMutatorAllele)
   genome.initializator.set(g1d.initializators.G1DListInitializatorAllele)

   # Genetic Algorithm Instance
   ga = algorithm.GSimpleGA(genome)
   ga.setGenerations(40)

   # Do the evolution, with stats dump
   # frequency of 10 generations
   ga.evolve(freq_stats=5)

   # Best individual
   print ga.bestIndividual()


if __name__ == "__main__":
   test_run_main()