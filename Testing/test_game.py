import unittest
from unittest import result
import game

class TestGame(unittest.TestCase):
    def setUp(self):
        print('#fingerscrossed')

    def test_game(self):
        answer=5
        guess=5
        result=game.run_guess(guess,answer)
        self.assertTrue(result)

    def test_game_wrong_guess(self):
        result=game.run_guess(5,3)
        self.assertFalse(result)

    def test_game_number_out_of_bound(self):
        result=game.run_guess(5,12)
        self.assertFalse(result)

    def test_game_wrong_type(self):
        result=game.run_guess(5,True)
        self.assertFalse(result)

if __name__=='__main__':
    unittest.main()