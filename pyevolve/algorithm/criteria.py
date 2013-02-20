from .. constants import minimaxType

def RawScoreCriteria(ga_engine):
   """ Terminate the evolution using the **bestrawscore** and **rounddecimal**
   parameter obtained from the individual

   Example:
      >>> genome.set_params(bestrawscore=0.00, rounddecimal=2)
      (...)
      >>> ga_engine.terminationCriteria.set(algorithm.RawScoreCriteria)

   """
   ind = ga_engine.bestIndividual()
   bestRawScore = ind.get_param("bestrawscore")
   roundDecimal = ind.get_param("rounddecimal")

   if bestRawScore is None:
      utils.raise_exception("you must specify the bestrawscore parameter", ValueError)

   if ga_engine.getMinimax() == minimaxType["maximize"]:
      if roundDecimal is not None:
         return round(bestRawScore, roundDecimal) <= round(ind.score, roundDecimal)
      else:
         return bestRawScore <= ind.score
   else:
      if roundDecimal is not None:
         return round(bestRawScore, roundDecimal) >= round(ind.score, roundDecimal)
      else:
         return bestRawScore >= ind.score

def ConvergenceCriteria(ga_engine):
   """ Terminate the evolution when the population have converged

   Example:
      >>> ga_engine.terminationCriteria.set(algorithm.ConvergenceCriteria)

   """
   pop = ga_engine.getPopulation()
   return pop[0] == pop[len(pop)-1]
   
def RawStatsCriteria(ga_engine):
   """ Terminate the evolution based on the raw stats

   Example:
      >>> ga_engine.terminationCriteria.set(algorithm.RawStatsCriteria)

   """
   stats = ga_engine.getStatistics()
   if stats["rawMax"] == stats["rawMin"]:
      if stats["rawAve"] == stats["rawMax"]:
         return True
   return False

def FitnessStatsCriteria(ga_engine):
   """ Terminate the evoltion based on the fitness stats

   Example:
      >>> ga_engine.terminationCriteria.set(algorithm.FitnessStatsCriteria)


   """
   stats = ga_engine.getStatistics()
   if stats["fitMax"] == stats["fitMin"]:
      if stats["fitAve"] == stats["fitMax"]:
         return True
   return False