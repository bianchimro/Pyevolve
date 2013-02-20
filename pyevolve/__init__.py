"""
:mod:`pyevolve` -- the main pyevolve namespace
================================================================

This is the main module of the pyevolve, every other module
is above this namespace, for example, to import :mod:`mutators`:

   >>> from pyevolve import mutators


"""
__all__ = ["constants", "crossovers", "dbadapters", "functionslot",
           "g1d", "g2d", "GAllele", "genome", "population",
           "GSimpleGA", "gtree", "Migration", "mutators", "network", "scaling", "selectors",
           "statistics", "utils" ]

__version__ =  '0.6'
__author__ =  'Christian S. Perone'

import pyevolve.constants
import sys

if sys.version_info[:2] < constants.CDefPythonRequire:
   raise Exception("Python 2.5+ required, the version %s was found on your system !" % (sys.version_info[:2],))

del sys

def logEnable(filename=constants.CDefLogFile, level=constants.CDefLogLevel):
   """ Enable the log system for pyevolve

   :param filename: the log filename
   :param level: the debugging level

   Example:
      >>> pyevolve.logEnable()

   """
   import logging
   logging.basicConfig(level=level,
                    format='%(asctime)s [%(module)s:%(funcName)s:%(lineno)d] %(levelname)s %(message)s',
                    filename=filename,
                    filemode='w')
   logging.info("Pyevolve v.%s, the log was enabled by user.", __version__)
