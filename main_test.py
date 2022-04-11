

import unittest

from main import hasWon


class TestMain(unittest.TestCase):
    def test_right_diag(self):
        board = [
            ['x', 'o', 'x'], 
            ['o', 'x', 'o'], 
            ['o', 'x', 'x']]

        self.assertEquals(hasWon(board), 'x')

    def test_1(self):
        board = [
            ['x', 'o', 'x'], 
            ['o', 'o', 'o'], 
            ['o', 'o', 'x']]

        self.assertEquals(hasWon(board), 'o')
    def test_2(self):
        board = [
            ['x', 'o', 'x'], 
            ['o', 'o', 'o'], 
            ['o', 'o', 'x']]

        self.assertEquals(hasWon(board), 'o')
    def test_3(self):
        board = [
            ['x', 'o', 'x'], 
            ['o', 'x', 'o'], 
            ['o', 'x', 'o']]

        self.assertEquals(hasWon(board), None)
