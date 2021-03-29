from airtest.core.api import *
import unittest


class Swipe_test(unittest.TestCase):
    def test_001(self):
        swipe((420, 1070), (420, 600), duration=4, steps=6)
