import sys
sys.path.append("../")

#from pyevolve import G1DList


from pyevolve import algorithm
from pyevolve.population import selectors
from pyevolve import statistics
from pyevolve import db
from pyevolve import g1d
from pyevolve.constants import minimaxType
import random

#import G1DDict
i = 0
# This function is the evaluation function, we want
# to give high score to more zero'ed chromosomes
def eval_func(genome):
    #score = 10.0
        
    score = float((abs(genome['a'] - genome['b'])))
    return score

def test_run_main():
  
    genome = g1d.G1DDict({ 'a' : {}, 'b' : {}}) 
  
    # The evaluator function (evaluation function)
    genome.evaluator.set(eval_func)
    
    # Genetic Algorithm Instance
    ga = algorithm.GSimpleGA(genome)
    ga.setMinimax(minimaxType['minimize'])
    
    # Set the Roulette Wheel selector method, the number of generations and
    # the termination criteria
    ga.selector.set(selectors.GRouletteWheel)
    ga.setGenerations(500)
    ga.terminationCriteria.set(algorithm.criteria.ConvergenceCriteria)
        
    # Do the evolution, with stats dump
    # frequency of 20 generations
    ga.evolve(freq_stats=20)
    
    # Best individual
    print ga.bestIndividual()

if __name__ == "__main__":
    test_run_main()
