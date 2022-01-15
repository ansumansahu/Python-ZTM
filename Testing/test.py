#If there are multiple test files while running it on terminal type:
#python -m unittest 
#python -m unittest -v (verbose) gives more details

from typing import Union
import unittest
from unittest import result
import main

class TestMain(unittest.TestCase):
    def setUp(self):
        print('#fingerscrossed')

    def test_do_stuff(self):
        test_param=5
        result=main.do_stuff(test_param)
        self.assertEqual(result,10)
    
    def test_do_stuff2(self):
        test_param='gibberish'
        result=main.do_stuff(test_param)
        self.assertIsInstance(result,ValueError)
        #as err returns Valueerror which is an instance of class ValueError

    def test_do_stuff3(self):
        test_param= None
        result=main.do_stuff(test_param)
        self.assertEqual(result,'Please enter a number')

    def test_do_stuff4(self):
        test_param= ''
        result=main.do_stuff(test_param)
        self.assertEqual(result,'Please enter a number')

    def tearDown(self):
        print('Cleaning Up')

if __name__=='__main__':
    unittest.main()