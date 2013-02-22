"""

:mod:`G1DDict` -- the 1D dict chromosome

"""
from pyevolve.genomebase import GenomeBase
from .. import constants
from .. import utils

import random
import copy


def G1DDictInitializatorInteger(genome, **args):
    """ Integer initialization function of G1DList
    
    This initializator accepts the *rangemin* and *rangemax* genome parameters.
    
    """
    
    attrs = genome.attrs
    
    
    for attr_name in attrs:
        attr = attrs[attr_name]
        range_min = attr.get("rangemin", 0)
        range_max = attr.get("rangemax", 100)
        genome.genomeDict[attr_name] = random.randint(range_min, range_max)
    

def G1DDictMutatorDummy(genome, **args):
    """ The mutator of G1DList, Swap Mutator
    
    .. note:: this mutator is :term:`Data Type Independent`
    
    """
   
    if args["pmut"] <= 0.0:
         return 0
    
    mutations = 0
    for attr_name in genome:
        if utils.random_flip_coin(args["pmut"]):

            attr = genome.attrs[attr_name]
            range_min = attr.get("rangemin", 0)
            range_max = attr.get("rangemax", 100)

            genome.genomeDict[attr_name] = random.randint(range_min, range_max)
            mutations+=1
    
    return mutations
    
    



class G1DDict(GenomeBase):
    def __init__(self, attrs={}, cloning=False):
        super(G1DDict,self).__init__()
        self.attrs = attrs
        self.genomeDict = {}
        self.genomeSize = len(self.attrs.keys())
        
        if not cloning:
            self.initializator.set(G1DDictInitializatorInteger)
            self.mutator.set(G1DDictMutatorDummy)
        
        
    def __iadd__(self, item):
        """ To add more items using the += operator """
        self.genomeDict.update(item)
        return self
    
    def __eq__(self, other):
        """ Compares one chromosome with another """
        cond1 = (self.genomeDict == other.genomeDict)
        return cond1
        
    def __iter__(self):
        """ Iterator support to the dict """
        return iter(self.genomeDict)
    
    def __getitem__(self, key):
        """ Return the specified gene of List """
        return self.genomeDict[key]
        
    def __setitem__(self, key, value):
        """ Set the specified value for an gene of List """
        self.genomeDict[key] = value
    
    def copy(self, g):
        """ Copy genome to 'g'
        
        Example:
           >>> genome_origin.copy(genome_destination)
        
        :param g: the destination instance
        
        """
        super(G1DDict,self).copy(g)
        g.genomeDict = copy.copy(self.genomeDict)
        g.genomeSize = self.genomeSize
        

    def clone(self):
      """ Return a new instace copy of the genome
      
      :rtype: the G1DList clone instance

      """
      newcopy = G1DDict(self.attrs, True)
      self.copy(newcopy)
      return newcopy


    def __repr__(self):
      """ Return a string representation of Genome """
      ret = GenomeBase.__repr__(self)
      ret += "- G1DDict\n"
      ret += "\Dict size:\t %s\n" % (self.genomeSize)
      ret += "\Dict:\t\t %s\n\n" % (self.genomeDict)
      return ret