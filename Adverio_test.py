import unittest
from Adverio import *
class Test_Adverio(unittest.TestCase):
    def setUp(self):
        self.pagination = {
            "current_page":10,
            "total_pages":500000,
            "boundaries":2,
            "around":2,
            }

    def test_check_list(self):
        self.assertEqual(check_list(self.pagination), [1, 2, 8, 9, 10, 11, 12, 499999, 500000] )
        
    def test_get_limts(self):
        self.assertEqual(get_limts(list(range(1,pagination["total_pages"]+1)),-1,0), [1,500000] )
    def test_boundaties_call(self):
        self.assertEqual(boundaties_call(pagination["boundaries"], list(range(1,pagination["total_pages"]+1))), [1, 2, 499999, 500000])
    def test_call_around(self):
        self.assertEqual(callaround(pagination["around"],pagination["current_page"]),[8, 9, 10, 11, 12])
if __name__ == '__main__':
    unittest.main()