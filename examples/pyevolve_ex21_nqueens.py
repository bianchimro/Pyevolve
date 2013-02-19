from pyevolve.G1D import g1dlist
from pyevolve import mutators, Crossovers
from pyevolve import constants, GSimpleGA
from pyevolve import DBAdapters
from random import shuffle

# The "n" in n-queens
BOARD_SIZE = 64

# The n-queens fitness function
def queens_eval(genome):
   collisions = 0
   for i in xrange(0, BOARD_SIZE):
      if i not in genome: return 0
   for i in xrange(0, BOARD_SIZE):
      col = False
      for j in xrange(0, BOARD_SIZE):
         if (i != j) and (abs(i-j) == abs(genome[j]-genome[i])):
            col = True
      if col == True: collisions +=1
   return BOARD_SIZE-collisions

def queens_init(genome, **args):
   genome.genomeList = range(0, BOARD_SIZE)
   shuffle(genome.genomeList)

def test_run_main():
   genome = g1dlist.G1DList(BOARD_SIZE)
   genome.set_params(bestrawscore=BOARD_SIZE, rounddecimal=2)
   genome.initializator.set(queens_init)
   genome.mutator.set(mutators.G1DListMutatorSwap)
   genome.crossover.set(Crossovers.G1DListCrossoverCutCrossfill)
   genome.evaluator.set(queens_eval)

   ga = GSimpleGA.GSimpleGA(genome)
   ga.terminationCriteria.set(GSimpleGA.RawScoreCriteria)
   ga.setMinimax(constants.minimaxType["maximize"])
   
   ga.setPopulationSize(100)
   ga.setGenerations(250)
   ga.setMutationRate(0.02)
   ga.setCrossoverRate(1.0)

   #sqlite_adapter = DBAdapters.DBSQLite(identify="queens")
   #ga.setDBAdapter(sqlite_adapter)

   vpython_adapter = DBAdapters.DBVPythonGraph(identify="queens", frequency=1)
   ga.setDBAdapter(vpython_adapter)
   
   ga.evolve(freq_stats=10)

   best = ga.bestIndividual()
   print best
   print "Best individual score: %.2f\n" % (best.get_raw_score(),)

if __name__ == "__main__":
   test_run_main()
  
