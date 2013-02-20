import sys
sys.path.append("../")
from pyevolve.g1d import g1dlist
from pyevolve import GSimpleGA
from pyevolve import selectors
from pyevolve import statistics
from pyevolve import dbadapters

# This function is the evaluation function, we want
# to give high score to more zero'ed chromosomes
def eval_func(genome):
   score = 0.0

   # iterate over the chromosome
   # The same as "score = len(filter(lambda x: x==0, genome))"
   for value in genome:
      if value==0:
         score += 1
   
   return score

def test_run_main():
   # Genome instance, 1D List of 50 elements
   genome = g1dlist.G1DList(50)

   # Sets the range max and min of the 1D List
   genome.set_params(rangemin=0, rangemax=10)

   # The evaluator function (evaluation function)
   genome.evaluator.set(eval_func)

   # Genetic Algorithm Instance
   ga = GSimpleGA.GSimpleGA(genome)

   # Set the Roulette Wheel selector method, the number of generations and
   # the termination criteria
   ga.selector.set(selectors.GRouletteWheel)
   ga.setGenerations(500)
   ga.terminationCriteria.set(GSimpleGA.ConvergenceCriteria)

   # Sets the DB Adapter, the resetDB flag will make the Adapter recreate
   # the database and erase all data every run, you should use this flag
   # just in the first time, after the pyevolve.db was created, you can
   # omit it.
   sqlite_adapter = dbadapters.DBSQLite(identify="ex1", resetDB=True)
   ga.setDBAdapter(sqlite_adapter)

   # Do the evolution, with stats dump
   # frequency of 20 generations
   ga.evolve(freq_stats=20)

   # Best individual
   print ga.bestIndividual()

if __name__ == "__main__":
   test_run_main()
