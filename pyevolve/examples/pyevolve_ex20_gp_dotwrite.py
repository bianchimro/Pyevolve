from pyevolve import *
import math

rmse_accum = utils.ErrorAccumulator()

def gp_add(a, b): return a+b
def gp_sub(a, b): return a-b
def gp_mul(a, b): return a*b
def gp_sqrt(a):   return math.sqrt(abs(a))
   
def eval_func(chromosome):
   global rmse_accum
   rmse_accum.reset()
   code_comp = chromosome.getCompiledCode()
   
   for a in xrange(0, 5):
      for b in xrange(0, 5):
         evaluated     = eval(code_comp)
         target        = math.sqrt((a*a)+(b*b))
         rmse_accum   += (target, evaluated)
   return rmse_accum.getRMSE()


def step_callback(engine):
   if engine.getCurrentGeneration() == 0:
      GTree.GTreeGP.writePopulationDotRaw(engine, "pop.dot", 0, 40)
   return False


def main_run():
   genome = GTree.GTreeGP()
   genome.set_params(max_depth=6, method="ramped")
   genome.evaluator += eval_func
   genome.mutator.set(mutators.GTreeGPMutatorSubtree)

   ga = algorithm.GSimpleGA(genome, seed=666)
   ga.stepCallback.set(step_callback)
   ga.set_params(gp_terminals       = ['a', 'b'],
                gp_function_prefix = "gp")

   ga.setMinimax(constants.minimaxType["minimize"])
   ga.setGenerations(2)
   ga.setCrossoverRate(1.0)
   ga.setMutationRate(0.08)
   ga.setPopulationSize(100)
   ga.setMultiProcessing(False)
   
   ga(freq_stats=5)
   
   #GTree.GTreeGP.writePopulationDotRaw(ga, "pop.dot", 0, 14)

   best = ga.bestIndividual()


if __name__ == "__main__":
   main_run()
