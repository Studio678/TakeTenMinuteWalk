from unittest import TestCase
from walks import Walks

class Test(TestCase):
    def setUp(self):
        self.walk1 = Walks(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']) 
        self.walk2 = Walks(['w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e'])
        self.walk3 = Walks(['w'])
        self.walk4 = Walks(['n', 'n', 'n', 's', 'n', 's', 'n', 's', 'n', 's'])
    #should return True
    def test_is_valid_walk(self):
        self.assertAlmostEqual(self.walk1.is_valid_walk(), True)
    
    
    #should return False
    def test_is_valid_walk(self):
        self.assertAlmostEqual(self.walk2.is_valid_walk(), False)

    # should return False
    def test_is_valid_walk(self):
        self.assertAlmostEqual(self.walk3.is_valid_walk(), False)

    # should return False
    def test_is_valid_walk(self):
        self.assertAlmostEqual(self.walk3.is_valid_walk(), False)