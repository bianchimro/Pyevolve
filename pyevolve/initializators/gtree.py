####################
##      Tree      ##
####################

def GTreeInitializatorInteger(genome, **args):
   """ Integer initialization function of GTree

   This initializator accepts the *rangemin* and *rangemax* genome parameters.
   It accepts the following parameters too:
      
   *max_depth*
      The max depth of the tree

   *max_siblings*
      The number of maximum siblings of an node

   *method*
      The method, accepts "grow", "full" or "ramped".

   .. versionadded:: 0.6
      The *GTreeInitializatorInteger* function.
   """
   max_depth = genome.get_param("max_depth", 5)
   max_siblings = genome.get_param("max_siblings", 2)

   range_min = genome.get_param("rangemin", 0)
   range_max = genome.get_param("rangemax", 100)

   lambda_generator = lambda: rand_randint(range_min, range_max)

   method = genome.get_param("method", "grow")

   if method == "grow":
      root = gtree.buildGTreeGrow(0, lambda_generator, max_siblings, max_depth)
   elif method == "full":
      root = gtree.buildGTreeFull(0, lambda_generator, max_siblings, max_depth)
   elif method == "ramped":
      if utils.random_flip_coin(0.5):
         root = gtree.buildGTreeGrow(0, lambda_generator, max_siblings, max_depth)
      else:
         root = gtree.buildGTreeFull(0, lambda_generator, max_siblings, max_depth)
   else:
      utils.raise_exception("Unknown tree initialization method [%s] !" % method)

   genome.setRoot(root)
   genome.processNodes()
   assert genome.get_height() <= max_depth

def GTreeInitializatorAllele(genome, **args):
   """ Allele initialization function of GTree

   To use this initializator, you must specify the *allele* genome parameter with the
   :class:`GAllele.GAlleles` instance.

   .. warning:: the :class:`GAllele.GAlleles` instance **must** have the homogeneous flag enabled

   .. versionadded:: 0.6
      The *GTreeInitializatorAllele* function.
   """
   max_depth    = genome.get_param("max_depth", 5)
   max_siblings = genome.get_param("max_siblings", 2)
   method       = genome.get_param("method", "grow")

   allele = genome.get_param("allele", None)
   if allele is None:
      utils.raise_exception("to use the GTreeInitializatorAllele, you must specify the 'allele' parameter")

   if allele.homogeneous == False:
      utils.raise_exception("to use the GTreeInitializatorAllele, the 'allele' must be homogeneous")

   if method == "grow":
      root = gtree.buildGTreeGrow(0, allele[0].getRandomAllele, max_siblings, max_depth)
   elif method == "full":
      root = gtree.buildGTreeFull(0, allele[0].getRandomAllele, max_siblings, max_depth)
   elif method == "ramped":
      if utils.random_flip_coin(0.5):
         root = gtree.buildGTreeGrow(0, allele[0].getRandomAllele, max_siblings, max_depth)
      else:
         root = gtree.buildGTreeFull(0, allele[0].getRandomAllele, max_siblings, max_depth)
   else:
      utils.raise_exception("Unknown tree initialization method [%s] !" % method)


   genome.setRoot(root)
   genome.processNodes()
   assert genome.get_height() <= max_depth

####################
##      Tree GP   ##
####################

def GTreeGPInitializator(genome, **args):
   """This initializator accepts the follow parameters:
      
   *max_depth*
      The max depth of the tree

   *method*
      The method, accepts "grow", "full" or "ramped"

   .. versionadded:: 0.6
      The *GTreeGPInitializator* function.
   """

   max_depth = genome.get_param("max_depth", 5)
   method    = genome.get_param("method", "grow")
   ga_engine = args["ga_engine"]

   if method == "grow":
      root = gtree.buildGTreeGPGrow(ga_engine, 0, max_depth)
   elif method == "full":
      root = gtree.buildGTreeGPFull(ga_engine, 0, max_depth)
   elif method == "ramped":
      if utils.random_flip_coin(0.5):
         root = gtree.buildGTreeGPFull(ga_engine, 0, max_depth)
      else:
         root = gtree.buildGTreeGPGrow(ga_engine, 0, max_depth)
   else:
      utils.raise_exception("Unknown tree initialization method [%s] !" % method)

   genome.setRoot(root)
   genome.processNodes()
   assert genome.get_height() <= max_depth
