from pyevolve import g2d
from pyevolve import algorithm
from pyevolve.population import selectors

# This function is the evaluation function, we want
# to give high score to more zero'ed chromosomes
def eval_func(chromosome):
    score = 0.0
 
    # iterate over the chromosome
    for i in xrange(chromosome.get_height()):
        for j in xrange(chromosome.get_width()):
          # You can use the chromosome.get_item(i, j)
            if chromosome[i][j]==0:
                score += 0.1
    return score

def test_run_main():

    # Genome instance
    genome = g2d.G2DBinaryString(8, 5)
    
    # The evaluator function (objective function)
    genome.evaluator.set(eval_func)
    genome.crossover.set(g2d.crossovers.G2DBinaryStringXSingleHPoint)
    genome.mutator.set(g2d.mutators.G2DBinaryStringMutatorSwap)
    
    # Genetic Algorithm Instance
    ga = algorithm.GSimpleGA(genome)
    ga.setGenerations(200)
    
    # Do the evolution, with stats dump
    # frequency of 10 generations
    ga.evolve(freq_stats=10)
    
    # Best individual
    print ga.bestIndividual()

if __name__ == "__main__":
   test_run_main()