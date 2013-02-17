from nose.tools import assert_raises, raises
from pyevolve import utils


class utils_functions_Test():

    def setUp(self):
        pass
        
    def random_flip_coin_test(self): 
    
        true_coin = utils.random_flip_coin(1)
        assert true_coin is True
        
        false_coin = utils.random_flip_coin(0)
        assert false_coin is False        
        
        prob_coin = utils.random_flip_coin(0.5)
        assert prob_coin is True or prob_coin is False

        
    def list_swap_element_test(self):
        l = [1, 2, 3]

        utils.list_swap_element(l, 1, 2)
        assert l == [1, 3, 2]

        utils.list_swap_element(l, 1, 2)
        assert l == [1, 2, 3]        

        assert_raises(IndexError, utils.list_swap_element, l, 1, 4)

        
    def list2D_swap_element(self):
        l = [ [1,2,3], [4,5,6] ] 

        utils.list2D_swap_element(l, (0,1), (1,1))
        assert l == [ [1, 5, 3], [4, 2, 6] ]

        utils.list2D_swap_element(l, (0,1), (1,1))
        assert l == [ [1,2,3], [4,5,6] ] 
        
    def raise_exception_test(self):
        
        assert_raises(IndexError, utils.raise_exception, "Some index error", IndexError)        
    
    def import_special_test(self):
        #TODO: how to test this if you have the module installed?
        #assert_raises(ImportError, utils.import_special, "visual.graph")
        #assert_raises(KeyError, utils.import_special, "something_visual.graph")
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

