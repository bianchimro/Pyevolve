from nose.tools import assert_raises, raises
from pyevolve import utils


class utils_functions_Test():

    def setUp(self):
        pass
        
    def randomFlipCoin_test(self): 
    
        true_coin = utils.randomFlipCoin(1)
        assert true_coin is True
        
        false_coin = utils.randomFlipCoin(0)
        assert false_coin is False        
        
        prob_coin = utils.randomFlipCoin(0.5)
        assert prob_coin is True or prob_coin is False

        
    def listSwapElement_test(self):
        l = [1, 2, 3]

        utils.listSwapElement(l, 1, 2)
        assert l == [1, 3, 2]

        utils.listSwapElement(l, 1, 2)
        assert l == [1, 2, 3]        

        assert_raises(IndexError, utils.listSwapElement, l, 1, 4)

        
    def list2DSwapElement(self):
        l = [ [1,2,3], [4,5,6] ] 

        utils.list2DSwapElement(l, (0,1), (1,1))
        assert l == [ [1, 5, 3], [4, 2, 6] ]

        utils.list2DSwapElement(l, (0,1), (1,1))
        assert l == [ [1,2,3], [4,5,6] ] 
        
    def raiseException_test(self):
        
        assert_raises(IndexError, utils.raiseException, "Some index error", IndexError)
        
    def cmp_individual_raw_test(self):
        #TODO: write test
        pass
        
    def cmp_individual_scaled_test(self):
        #TODO: write test
        pass
        
    
    def importSpecial_test(self):
        #TODO: how to test this if you have the module installed?
        #assert_raises(ImportError, utils.importSpecial, "visual.graph")
        #assert_raises(KeyError, utils.importSpecial, "something_visual.graph")
        pass
        
    def tearDown(self):
        pass


class utils_ErrorAccumulator_Test():

    def setUp(self):
        pass
        

    def test_init(self):
        ac = utils.ErrorAccumulator()
        assert ac.acc == 0
        assert ac.acc_square == 0
        assert ac.acc_len == 0


    def test_reset(self):
        ac = utils.ErrorAccumulator()
        ac.append(1,1)
        ac.append(1,3)
        ac.append(1,13)
        ac.reset()
        assert ac.acc == 0
        assert ac.acc_square == 0
        assert ac.acc_len == 0


    def test_append(self):
        ac = utils.ErrorAccumulator()
        ac.append(1,1)
        assert ac.acc == 0
        assert ac.acc_square == 0
        assert ac.acc_len == 1
        
        ac.append(1,3)
        assert ac.acc == 2
        assert ac.acc_square == 4
        assert ac.acc_len == 2
        
        
    def test_getMean(self):
        ac = utils.ErrorAccumulator()
        ac.append(1,3)
        mean = ac.getMean()
        assert mean == 2
        
        ac.append(1,3)
        mean = ac.getMean()
        assert mean == 2
        
        ac.append(1,6)
        mean = ac.getMean()
        assert mean == 3


    def test_getAdjusted(self):
        ac = utils.ErrorAccumulator()
        ac.append(1,3)
        ac.append(1,3)
        
        expected_value = 1.0/5.0
        value = ac.getAdjusted()
        assert value == expected_value


    def test_getRMSE(self):
        ac = utils.ErrorAccumulator()
        ac.append(1,3)
        ac.append(1,3)
        expected_value = 2
        value = ac.getRMSE()
        assert value == expected_value
        

    def test_getMSE(self):
        ac = utils.ErrorAccumulator()
        ac.append(1,3)
        ac.append(1,3)
        expected_value = 4
        value = ac.getMSE()
        assert value == expected_value
        

    def tearDown(self):
        pass


#TODO: WRITE ALL MISSING TESTS IN utilss module

