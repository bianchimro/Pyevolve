"""

:mod:`constants` -- constants module
============================================================================

Pyevolve have defaults in all genetic operators, settings and etc, this is an issue to helps the user in the API use and minimize the source code needed to make simple things. In the module :mod:`constants`, you will find those defaults settings. You are encouraged to see the constants, but not to change directly on the module, there are methods for this.

General constants
----------------------------------------------------------------------------

.. attribute:: CDefPythonRequire
  
   The mininum version required to run Pyevolve.

.. attribute:: CDefLogFile
   
   The default log filename.

.. attribute:: CDefLogLevel

   Default log level.

.. attribute:: sortType
   
   Sort type, raw or scaled.

   Example:
      >>> sort_type = constants.sortType["raw"]
      >>> sort_type = constants.sortType["scaled"]

.. attribute:: minimaxType

   The Min/Max type, maximize or minimize the evaluation function.

   Example:
      >>> minmax = constants.minimaxType["minimize"]
      >>> minmax = constants.minimaxType["maximize]
  
.. attribute:: CDefESCKey

   The ESC key ASCII code. Used to start Interactive Mode.

.. attribute:: CDefRangeMin

   Minimum range. This constant is used as integer and real max/min.

.. attribute:: CDefRangeMax

   Maximum range. This constant is used as integer and real max/min.

.. attribute:: CDefBroadcastAddress
   
   The broadcast address for UDP, 255.255.255.255

.. attribute:: CDefImportList
   
   The import list and messages

.. attribute:: nodeType

   The genetic programming node types, can be "TERMINAL":0 or "NONTERMINAL":1

.. attribute:: CDefGPGenomes

   The classes which are used in Genetic Programming, used to detected the
   correct mode when starting the evolution

Selection methods constants (:mod:`selectors`)
----------------------------------------------------------------------------

.. attribute:: CDefTournamentPoolSize

   The default pool size for the Tournament Selector (:func:`selectors.GTournamentSelector`).

scaling.scheme constants (:mod:`scaling.)
----------------------------------------------------------------------------

.. attribute:: CDefScaleLinearMultiplier

   The multiplier of the Linear (:func:`scaling.Linearscaling.) scaling scheme.

.. attribute:: CDefScaleSigmaTruncMultiplier

   The default Sigma Truncation (:func:`scaling.SigmaTruncscaling.) scaling scheme.

.. attribute:: CDefScalePowerLawFactor

   The default Power Law (:func:`scaling.PowerLawscaling.) scaling scheme factor.

.. attribute:: CDefScaleBoltzMinTemp

   The default mininum temperature of the (:func:`scaling.Boltzmannscaling.) scaling scheme factor.

.. attribute:: CDefScaleBoltzFactor

   The default Boltzmann Factor of (:func:`scaling.Boltzmannscaling.) scaling scheme factor.
   This is the factor that the temperature will be subtracted.

.. attribute:: CDefScaleBoltzStart

   The default Boltzmann start temperature (:func:`scaling.Boltzmannscaling.).
   If you don't set the start temperature parameter, this will be the default initial
   temperature for the Boltzmann scaling scheme.

Population constants (:class:`GPopulation.GPopulation`)
----------------------------------------------------------------------------
   
.. attribute:: CDefPopSortType
   
   Default sort type parameter.

.. attribute:: CDefPopMinimax

   Default min/max parameter.

.. attribute:: CDefPopScale

   Default scaling scheme.


1D Binary String Defaults (:class:`G1DBinaryString.G1DBinaryString`)
----------------------------------------------------------------------------

.. attribute:: CDefG1DBinaryStringMutator

   The default mutator for the 1D Binary String (:class:`G1DBinaryString.G1DBinaryString`) chromosome.

.. attribute:: CDefG1DBinaryStringCrossover

   The default crossover method for the 1D Binary String (:class:`G1DBinaryString.G1DBinaryString`) chromosome.

.. attribute:: CDefG1DBinaryStringInit

   The default initializator for the 1D Binary String (:class:`G1DBinaryString.G1DBinaryString`) chromosome.

.. attribute:: CDefG1DBinaryStringUniformProb

   The default uniform probability used for some uniform genetic operators for the 1D Binary String (:class:`G1DBinaryString.G1DBinaryString`) chromosome.


2D Binary String Defaults (:class:`G2DBinaryString.G2DBinaryString`)
----------------------------------------------------------------------------

.. attribute:: CDefG2DBinaryStringMutator

   The default mutator for the 2D Binary String (:class:`G2DBinaryString.G2DBinaryString`) chromosome.

.. attribute:: CDefG2DBinaryStringCrossover

   The default crossover method for the 2D Binary String (:class:`G2DBinaryString.G2DBinaryString`) chromosome.

.. attribute:: CDefG2DBinaryStringInit

   The default initializator for the 2D Binary String (:class:`G2DBinaryString.G2DBinaryString`) chromosome.

.. attribute:: CDefG2DBinaryStringUniformProb

   The default uniform probability used for some uniform genetic operators for the 2D Binary String (:class:`G2DBinaryString.G2DBinaryString`) chromosome.


1D List chromosome constants (:class:`g1dlist.G1DList
`)
----------------------------------------------------------------------------

.. attribute:: CDefG1DListMutIntMU

   Default *mu* value of the 1D List Gaussian Integer Mutator (:func:`mutators.G1DListMutatorIntegerGaussian`), the *mu* represents the mean of the distribution.
   
.. attribute:: CDefG1DListMutIntSIGMA

   Default *sigma* value of the 1D List Gaussian Integer Mutator (:func:`mutators.G1DListMutatorIntegerGaussian`), the *sigma* represents the standard deviation of the distribution.
   
.. attribute:: CDefG1DListMutRealMU

   Default *mu* value of the 1D List Gaussian Real Mutator (:func:`mutators.G1DListMutatorRealGaussian`), the *mu* represents the mean of the distribution.
   
.. attribute:: CDefG1DListMutRealSIGMA

   Default *sigma* value of the 1D List Gaussian Real Mutator (:func:`mutators.G1DListMutatorRealGaussian`), the *sigma* represents the mean of the distribution.


Tree chromosome constants (:class:`GTree.GTree`)
----------------------------------------------------------------------------

.. attribute:: CDefGTreeInit

   Default initializator of the tree chromosome.
   
.. attribute:: CDefGGTreeMutator

   Default mutator of the tree chromosome.
   
.. attribute:: CDefGTreeCrossover

   Default crossover of the tree chromosome.
  

2D List chromosome constants (:class:`G2DList.G2DList`)
----------------------------------------------------------------------------

.. attribute:: CDefG2DListMutRealMU

   Default *mu* value of the 2D List Gaussian Real Mutator (:func:`mutators.G2DListMutatorRealGaussian`), the *mu* represents the mean of the distribution.

.. attribute:: CDefG2DListMutRealSIGMA

   Default *sigma* value of the 2D List Gaussian Real Mutator (:func:`mutators.G2DListMutatorRealGaussian`), the *sigma* represents the mean of the distribution.

.. attribute:: CDefG2DListMutIntMU

   Default *mu* value of the 2D List Gaussian Integer Mutator (:func:`mutators.G2DListMutatorIntegerGaussian`), the *mu* represents the mean of the distribution.
   
.. attribute:: CDefG2DListMutIntSIGMA

   Default *sigma* value of the 2D List Gaussian Integer Mutator (:func:`mutators.G2DListMutatorIntegerGaussian`), the *sigma* represents the mean of the distribution.

.. attribute:: CDefG2DListMutator

   Default mutator for the 2D List chromosome.

.. attribute:: CDefG2DListCrossover

   Default crossover method for the 2D List chromosome.

.. attribute:: CDefG2DListInit

   Default initializator for the 2D List chromosome.

.. attribute:: CDefG2DListCrossUniformProb

   Default uniform probability for the 2D List Uniform Crossover method (:func:`crossovers.G2DListCrossoverUniform`).


GA Engine constants (:class:`GSimpleGA.GSimpleGA`)
----------------------------------------------------------------------------

.. attribute:: CDefGAGenerations

   Default number of generations.

.. attribute:: CDefGAMutationRate

   Default mutation rate.

.. attribute:: CDefGACrossoverRate

   Default crossover rate.

.. attribute:: CDefGAPopulationSize

   Default population size.

.. attribute:: CDefGASelector

   Default selector method.

DB Adapters constants (:mod:`DBAdapters`)
----------------------------------------------------------------------------
Constants for the DB Adapters


SQLite3 DB Adapter Constants (:class:`DBAdapters.DBSQLite`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. attribute:: CDefSQLiteDBName
   
   Default database filename.

.. attribute:: CDefSQLiteDBTable

   Default statistical table name.

.. attribute:: CDefSQLiteDBTablePop

   Default population statistical table name.

.. attribute:: CDefSQLiteStatsGenFreq

   Default generational frequency for dump statistics.

.. attribute:: CDefSQLiteStatsCommitFreq

   Default commit frequency.


MySQL DB Adapter Constants (:class:`DBAdapters.DBMySQLAdapter`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. attribute:: CDefMySQLDBName
   
   Default database name.

.. attribute:: CDefMySQLDBTable

   Default statistical table name.

.. attribute:: CDefMySQLDBTablePop

   Default population statistical table name.

.. attribute:: CDefMySQLStatsGenFreq

   Default generational frequency for dump statistics.

.. attribute:: CDefMySQLStatsCommitFreq

   Default commit frequency.

.. attribute:: CDefMySQLDBHost

   Default MySQL connection host.

.. attribute:: CDefMySQLDBPort

   Default MySQL connection TCP port.


URL Post DB Adapter Constants (:class:`DBAdapters.DBURLPost`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. attribute:: CDefURLPostStatsGenFreq

   Default generational frequency for dump statistics.


CSV File DB Adapter Constants (:class:`DBAdapters.DBFileCSV`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. attribute:: CDefCSVFileName
   
   The default CSV filename to dump statistics.

.. attribute:: CDefCSVFileStatsGenFreq

   Default generational frequency for dump statistics.


XMP RPC DB Adapter Constants (:class:`DBAdapters.DBXMLRPC`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. attribute:: CDefXMLRPCStatsGenFreq

   Default generational frequency for dump statistics.

Migration Constants (:mod:`Migration`)
----------------------------------------------------------------------------
.. attribute:: CDefGenMigrationRate
   
   The default generations supposed to migrate and receive individuals

.. attribute:: CDefMigrationNIndividuals

   The default number of individuals that will migrate at the *CDefGenMigrationRate*
   interval

.. attribute:: CDefNetworkIndividual

   A migration code for network individual data

.. attribute:: CDefNetworkInfo

   A migration code for network info data

.. attribute:: CDefGenMigrationReplacement

   The default number of individuals to be replaced at the migration stage


"""
import logging

# Required python version 2.5+
CDefPythonRequire = (2, 5)

# Logging system
CDefLogFile = "pyevolve.log"
CDefLogLevel = logging.DEBUG

# Types of sort
# - raw: uses the "score" attribute
# - scaled: uses the "fitness" attribute
sortType = { 
    "raw"    : 0,
    "scaled" : 1
}

# Optimization type
# - Minimize or Maximize the Evaluator Function
minimaxType = { 
    "minimize" : 0,
    "maximize" : 1
}


nodeType = {
    "TERMINAL" : 0, 
    "NONTERMINAL": 1
}

# - This is general used by integer/real ranges defaults
CDefRangeMin = 0
CDefRangeMax = 100

