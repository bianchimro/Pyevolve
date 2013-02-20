from nose.tools import assert_raises, raises
from pyevolve import functionslot


def a_function(x):
    return 1
def b_function(x):
    return x
def c_function(c, name="x"):
    return str(c)+name


    
an_integer = 10


class FunctionSlot_Test():

    def setUp(self):
        pass
    
    def test___typeCheck(self):
        slot = functionslot.FunctionSlot()
        slot._FunctionSlot__typeCheck(a_function)
        assert_raises(TypeError, slot._FunctionSlot__typeCheck, an_integer)
        
    def test____iadd__(self):
        slot = functionslot.FunctionSlot()
        slot += a_function
        assert slot.funcList == [a_function]
        assert slot.funcWeights == [0.5]
    
    def test_add(self):
        slot = functionslot.FunctionSlot()
        slot.add(a_function)
        assert slot.funcList == [a_function]
        assert slot.funcWeights == [0.5]
    
    def test___len__(self):
        slot = functionslot.FunctionSlot()
        assert len(slot) == 0    
        slot.add(a_function)
        slot.add(a_function)
        assert len(slot) == 2    
    
    def test_isEmpty(self):
        slot = functionslot.FunctionSlot()
        assert slot.isEmpty() == True
        slot.add(a_function)
        assert slot.isEmpty() == False        
        
    def test_clear(self):
        slot = functionslot.FunctionSlot()
        slot.add(a_function)
        assert slot.isEmpty() == False                
        slot.clear()
        assert slot.isEmpty() == True
    
    def test_setRandomApply(self):
        slot = functionslot.FunctionSlot()
        assert slot.rand_apply == False
        slot.setRandomApply(True)
        assert slot.rand_apply == True
        assert_raises(TypeError, slot.setRandomApply, 12)
    
    def test_set(self):
        slot = functionslot.FunctionSlot()
        slot.add(a_function)
        slot.add(a_function)
        assert len(slot) == 2    
        slot.set(a_function)
        assert len(slot) == 1
        assert slot.funcList == [a_function]
        assert slot.funcWeights == [0.5]
        
    def test_apply(self):
        slot = functionslot.FunctionSlot()
        assert_raises(NotImplementedError, slot.apply, 0, 1)        
        slot.add(a_function)
        slot.add(b_function)
        slot.add(c_function)
        assert slot.apply(0, 1) == 1
        assert slot.apply(1, 2) == 2
        assert slot.apply(2, 2, name='pierre') == '2pierre'
        assert_raises(IndexError, slot.apply, 3, 1)
    
    def test_applyFunctions(self):
        slot = functionslot.FunctionSlot()
        slot.add(a_function)
        slot.add(b_function)
        slot.add(c_function)
        
        results = []
        for result in slot.applyFunctions(1):
            results.append(result)
        assert results == [1, 1, '1x']
                        
        
    def tearDown(self):
        pass


