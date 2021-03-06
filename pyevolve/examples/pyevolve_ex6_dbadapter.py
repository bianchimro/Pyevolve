from pyevolve.g1d import g1dlist
from pyevolve import algorithm
from pyevolve.population import selectors
from pyevolve import db
from pyevolve import statistics

# This function is the evaluation function, we want
# to give high score to more zero'ed chromosomes
def eval_func(chromosome):
   score = 0.0

   # iterate over the chromosome
   for value in chromosome:
      if value==0:
         score += 0.5
   return score

def test_run_main():
    # Genome instance
    genome = g1dlist.G1DList(100)
    genome.set_params(rangemin=0, rangemax=10)
    
    # The evaluator function (objective function)
    genome.evaluator.set(eval_func)
    
    # Genetic Algorithm Instance
    ga = algorithm.GSimpleGA(genome, 666)
    ga.setGenerations(80)
    ga.setMutationRate(0.2)
    
    # Create DB Adapter and set as adapter
    #sqlite_adapter = DBAdapters.DBSQLite(identify="ex6", resetDB=True)
    #ga.setDBAdapter(sqlite_adapter)
    
    # Using CSV Adapter
    #csvfile_adapter = DBAdapters.DBFileCSV()
    #ga.setDBAdapter(csvfile_adapter)
    
    # Using the URL Post Adapter
    # urlpost_adapter = DBAdapters.DBURLPost(url="http://whatismyip.oceanus.ro/server_variables.php", post=False)
    # ga.setDBAdapter(urlpost_adapter)
    
    # Do the evolution, with stats dump
    # frequency of 10 generations
    ga.evolve(freq_stats=10)
    
    # Best individual
    #print ga.bestIndividual()
    
if __name__ == "__main__":
   test_run_main()

