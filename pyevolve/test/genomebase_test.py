from nose.tools import assert_raises, raises
from pyevolve import genomebase


class FunctionSlot_Test():

    def setUp(self):
        pass
    
    def test_set_params(self):
        gb = genomebase.GenomeBase()
        params = {'a': 100 }
        gb.set_params(**params)
        for key in params:
            assert params[key] == gb.internalParams[key]
        
    def tearDown(self):
        pass


