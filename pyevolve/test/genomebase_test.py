from nose.tools import assert_raises, raises
from pyevolve import genomebase

#TODO: test untested methods

def initializator_example(genome):
    genome.test_member = 100

def mutator_example(genome):
    genome.test_member /= 2
    return 1

def evaluator_example(genome):
    return genome.test_member

class GenomeBase_Test():

    def setUp(self):
        pass
    
    def test_set_params(self):
        gb = genomebase.GenomeBase()
        params = {'a': 100 }
        gb.set_params(**params)
        for key in params:
            assert params[key] == gb.internalParams[key]
            
    def test_get_param(self):
        gb = genomebase.GenomeBase()
        params = {'a': 100 }
        gb.set_params(**params)
        a = gb.get_param('a')
        assert a == 100
        b = gb.get_param('b', None)
        assert b == None
        
    def test_init(self):
        gb = genomebase.GenomeBase()
        assert gb.score == 0
        assert gb.fitness == 0
        assert gb.evaluator.isEmpty() == True
        assert gb.initializator.isEmpty() == True
        assert gb.initializator.isEmpty() == True
        assert gb.crossover.isEmpty() == True
        assert gb.internalParams.keys() == []
        
    def test_initialize(self):
        gb = genomebase.GenomeBase()
        gb.initializator.set(initializator_example)
        gb.initialize()
        assert gb.test_member == 100
        
    def test_mutate(self):
        gb = genomebase.GenomeBase()
        gb.initializator.set(initializator_example)
        gb.mutator.set(mutator_example)
        gb.initialize()
        assert gb.test_member == 100
        gb.mutate()
        assert gb.test_member == 50
        
    def test_evaluate(self):
        gb = genomebase.GenomeBase()
        gb.initializator.set(initializator_example)
        gb.initialize()
        gb.evaluator.set(evaluator_example)
        gb.evaluate()
        assert gb.score == 100
        


    def tearDown(self):
        pass


