"""
:mod:`G2DBinaryString` -- the classical binary string chromosome
=====================================================================

This representation is a 2D Binary String, the string looks like
this matrix:

00101101010
00100011010
00101101010
10100101000

Default Parameters
-------------------------------------------------------------

*Initializator*
   
   :func:`initializators.G2DBinaryStringInitializator`

   The Binatry String Initializator for G2DBinaryString

*Mutator*

   :func:`Mutators.G2DBinaryStringMutatorFlip`

   The Flip Mutator for G2DBinaryString

*Crossover*

   :func:`Crossovers.G2DBinaryStringXSinglePoint`

   The Single Point Crossover for G2DBinaryString

.. versionadded:: 0.6
   Added the module :mod:`G2DBinaryString`

Class
-------------------------------------------------------------
"""

from genome import GenomeBase
import Mutators
import Crossovers
import initializators
import utils
    
# - G2DBinaryString defaults
CDefG2DBinaryStringMutator     = Mutators.G2DBinaryStringMutatorFlip
CDefG2DBinaryStringCrossover   = Crossovers.G2DBinaryStringXUniform
CDefG2DBinaryStringInit        = initializators.G2DBinaryStringInitializator
CDefG2DBinaryStringUniformProb = 0.5

    
class G2DBinaryString(GenomeBase):
    """ G3DBinaryString Class - The 2D Binary String chromosome
    
    Inheritance diagram for :class:`G2DBinaryString.G2DBinaryString`:
 
    .. inheritance-diagram:: G2DBinaryString.G2DBinaryString
 
    Example:
       >>> genome = G2DBinaryString.G2DBinaryString(10, 12)
 
 
    :param height: the number of rows
    :param width: the number of columns
 
    """

    def __init__(self, height, width):
        """ The initializator of G2DBinaryString representation,
        height and width must be specified """
        super(G2DBinaryString, self).__init__()
        self.height = height
        self.width = width
    
        self.genomeString = [None]*height
        for i in xrange(height):
            self.genomeString[i] = [None] * width
    
        self.initializator.set(CDefG2DBinaryStringInit)
        self.mutator.set(CDefG2DBinaryStringMutator)
        self.crossover.set(CDefG2DBinaryStringCrossover)
   
    def __eq__(self, other):
        """ Compares one chromosome with another """
        cond1 = (self.genomeString == other.genomeString)
        cond2 = (self.height     == other.height)
        cond3 = (self.width      == other.width)
        return True if cond1 and cond2 and cond3 else False

    def get_item(self, x, y):
        """ Return the specified gene of List
  
        Example:
            >>> genome.get_item(3, 1)
            0
        
        :param x: the x index, the column
        :param y: the y index, the row
        :rtype: the item at x,y position
        
        """
        return self.genomeString[x][y]

    def set_item(self, x, y, value):
        """ Set the specified gene of List
  
        Example:
            >>> genome.set_item(3, 1, 0)
        
        :param x: the x index, the column
        :param y: the y index, the row
        :param value: the value (integers 0 or 1)
        
        """
        if value not in [0,1]:
             utils.raise_exception("The item value must be 0 or 1 in the G2DBinaryString chromosome", ValueError)
        self.genomeString[x][y] = value


    def __getitem__(self, key):
       """ Return the specified gene of List """
       return self.genomeString[key]

    def __iter__(self):
       """ Iterator support to the list """
       return iter(self.genomeString)
   
    def get_height(self):
       """ Return the height (lines) of the List """
       return self.height

    def get_width(self):
       """ Return the width (lines) of the List """
       return self.width

    def get_size(self):
        """ Returns a tuple (height, widht)
   
        Example:
            >>> genome.get_size()
            (3, 2)
 
        """
        return (self.get_height(), self.get_width())


    def __repr__(self):
        """ Return a string representation of Genome """
        ret = super(G2DBinaryString, self).__repr__()
        ret += "- G2DBinaryString\n"
        ret += "\tList size:\t %s\n" % (self.get_size(),)
        ret += "\tList:\n"
        for line in self.genomeString:
           ret += "\t\t\t"
           for item in line:
              ret += "[%s] " % (item)
           ret += "\n"
        ret += "\n"
        return ret

    def resume_string(self):
        """ Returns a resumed string representation of the Genome
        
        """
        ret = ""
        for line in self.genomeString:
           for item in line:
              ret += "[%s] " % (item)
           ret += "\n"
        return ret
 
    def clear_string(self):
        """ Remove all genes from Genome """
        del self.genomeString[:]
        
        self.genomeString = [None]* self.height
        for i in xrange(self.height):
           self.genomeString[i] = [None] * self.width
    
    def copy(self, g):
        """ Copy genome to 'g'
        
        Example:
            >>> genome_origin.copy(genome_destination)
        
        :param g: the destination G2DBinaryString instance
  
        """
        super(G2DBinaryString, self).copy(g)
        g.height = self.height
        g.width = self.width
        for i in xrange(self.height):
           g.genomeString[i] = self.genomeString[i][:]
    
    def clone(self):
        """ Return a new instace copy of the genome
        
        :rtype: the G2DBinaryString clone instance
  
        """
        newcopy = G2DBinaryString(self.height, self.width)
        self.copy(newcopy)
        return newcopy
 
