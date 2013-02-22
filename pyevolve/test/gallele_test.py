from nose.tools import assert_raises, raises
from pyevolve.genomebase import gallele
from pyevolve import constants


class GAlleles_Test():

    def setUp(self):
        pass
        
    def test_init(self):
        instance = gallele.GAlleles()
        assert instance.allele_list == []
        assert instance.homogeneous == False
        instance_2 = gallele.GAlleles(allele_list = [1,2,3], homogeneous=True)
        assert instance_2.allele_list == [1,2,3]
        assert instance_2.homogeneous == True
        
    def test_add(self):
        instance = gallele.GAlleles()
        instance.add(1)
        assert instance.allele_list == [1]
        instance.add(2)
        assert instance.allele_list == [1,2]        
        
    def test_iadd(self):
        instance = gallele.GAlleles()
        instance += 1
        assert instance.allele_list == [1]
        instance += 2
        assert instance.allele_list == [1,2]        
        
    def test_get_slice(self):
        instance = gallele.GAlleles(allele_list=[1,2,3,4])
        slice = instance[:2]
        assert slice == [1,2]
        
    def test_get_item(self):
        instance = gallele.GAlleles(allele_list=[1,2,3,4])
        item = instance[1]
        assert item == 2
        instance_2 = gallele.GAlleles(homogeneous=True)
        instance_2 += 1
        item = instance_2[1]
        assert item == 1
    
    def test_iter(self):
        instance = gallele.GAlleles(allele_list=[1,2,3,4])
        li = []
        for x in instance:
            li.append(x)
        assert li == instance.allele_list
        instance_2 = gallele.GAlleles(homogeneous=True)
        instance_2 += 1
        li = []
        for x in instance_2:
            li.append(x)
        assert li == [1]
        
    def test_len(self):
        instance = gallele.GAlleles(allele_list=[1,2,3,4])
        assert len(instance) == 4
        instance_2 = gallele.GAlleles(homogeneous=True)
        instance_2 += 1
        assert len(instance_2) == 1
        
    def tearDown(self):
        pass


class GAlleleList_Test():

    def setUp(self):
        pass
        
    def test_init(self):
        instance = gallele.GAlleleList()
        assert instance.options == []
        instance_2 = gallele.GAlleleList([1,2,3])
        assert instance_2.options == [1,2,3]
        
    def test_clear(self):
        instance = gallele.GAlleleList([1,2,3])
        assert instance.options == [1,2,3]
        instance.clear()
        assert instance.options == []
        
    def test_get_random_allele(self):
        instance = gallele.GAlleleList([1,2,3])
        allele = instance.getRandomAllele()
        assert allele in [1,2,3]
        
    def test_add(self):
        instance = gallele.GAlleleList([1,2,3])
        assert instance.options == [1,2,3]
        instance.add(4)
        assert instance.options == [1,2,3,4]
        
    def test_get_slice(self):
        instance = gallele.GAlleleList([1,2,3])
        slice = instance[:2]
        assert slice == [1,2]
        
    def test_get_item(self):
        instance = gallele.GAlleleList([1,2,3])
        item = instance[1]
        assert item == 2
        
    def test_set_item(self):
        instance = gallele.GAlleleList([1,2,3])
        instance[1] = 4
        assert instance.options[1] == 4
        
    def test_len(self):
        instance = gallele.GAlleleList([1,2,3])
        assert len(instance) == 3
    
    def tearDown(self):
        pass


class GAlleleRange_Test():

    def setUp(self):
        pass
        
    def test_init(self):
        instance = gallele.GAlleleRange()
        assert instance.beginEnd == [(constants.CDefRangeMin, constants.CDefRangeMax)]
        assert instance.real == False
        assert instance.minimum == constants.CDefRangeMin
        assert instance.maximum == constants.CDefRangeMax
        assert instance.getMinimum() == instance.minimum
        assert instance.getMaximum() == instance.maximum
        assert instance.getReal() == instance.real
    
    def test_process_min_max(self):
        instance = gallele.GAlleleRange(end=constants.CDefRangeMax, 
            begin=constants.CDefRangeMin)
        assert instance.minimum == constants.CDefRangeMin
        assert instance.maximum == constants.CDefRangeMax
        
    def test_add(self):
        instance = gallele.GAlleleRange(begin=0, end=100)
        instance.add(110, 200)
        assert instance.beginEnd == [(0,100),(110, 200)]
        assert instance.minimum == 0
        assert instance.maximum == 200
        
    def test_get_item(self):
        instance = gallele.GAlleleRange(begin=0, end=100)
        instance.add(110, 200)
        r = instance[1]
        assert r == (110, 200)
        
    def test_set_item(self):
        instance = gallele.GAlleleRange(begin=0, end=100)
        instance[0] = (110, 200)
        assert instance.minimum == 110
        assert instance.maximum == 200
        
    def test_clear(self):
        instance = gallele.GAlleleRange(begin=0, end=100)
        instance.clear()
        assert instance.beginEnd == []
        assert instance.minimum == None
        assert instance.maximum == None       
        
    def test_len(self):
        instance = gallele.GAlleleRange(begin=0, end=100)
        assert len(instance) == 1         
        
    def test_set_real(self):
        instance = gallele.GAlleleRange(begin=0, end=100)
        assert instance.real == False
        instance.setReal(True)
        assert instance.real == True
    
    def test_get_random_allele(self):
        instance = gallele.GAlleleRange(begin=0, end=100)
        x = instance.getRandomAllele()
        assert x in range(0,100)
        assert type(x) == type(1)
        instance_2 = gallele.GAlleleRange(begin=0, end=100, real=True)
        x_2 = instance_2.getRandomAllele()        
        assert x_2 >= 0 and x_2 <= 100
        assert type(x_2) == type(1.0)
    
    def tearDown(self):
        pass


