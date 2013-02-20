from pyevolve import GSimpleGA
from pyevolve.gtree import gtree
from pyevolve import crossovers
from pyevolve import mutators
import time
import random

def eval_func(chromosome):
   score = 0.0
   # If you want to add score values based
   # in the height of the Tree, the extra
   # code is commented.

   #height = chromosome.get_height()

   for node in chromosome:
      score += (100 - node.getData())*0.1

   #if height <= chromosome.get_param("max_depth"):
   #   score += (score*0.8)

   return score

def test_run_main():
   genome = gtree.GTree()
   root = gtree.GTreeNode(2)
   genome.setRoot(root)
   genome.processNodes()

   genome.set_params(max_depth=3, max_siblings=2, method="grow")
   genome.evaluator.set(eval_func)
   genome.crossover.set(crossovers.GTreeCrossoverSinglePointStrict)

   ga = GSimpleGA.GSimpleGA(genome)
   ga.setGenerations(100)
   ga.setMutationRate(0.05)
   
   ga.evolve(freq_stats=10)
   print ga.bestIndividual()

if __name__ == "__main__":
   test_run_main()

  
