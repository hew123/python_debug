import unittest
from missingChar import findLowestMissingCharacter

class TestMethods(unittest.TestCase):

    def test_missingChar(self):
        self.assertEqual(findLowestMissingCharacter(['a', 'b', 'c'], 'b'), 'd')
        self.assertEqual(findLowestMissingCharacter(['d', 'a', 'e'], 'e'), 'f')
        self.assertEqual(findLowestMissingCharacter(['b', 'c', 'e'], 'b'), 'd')
        self.assertEqual(findLowestMissingCharacter(['e', 'f', 'h'], 'a'), 'b')


if __name__ == '__main__':
    unittest.main()