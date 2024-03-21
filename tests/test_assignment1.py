# Python

import unittest
from unittest.mock import patch
from io import StringIO

import assignment1  # assuming the above code is in assignment1.py

class TestAdventureGame(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_print_location(self, mock_stdout):
        assignment1.print_location("Bob", "forest")
        self.assertEqual(mock_stdout.getvalue(), "Bob, you are in the forest. You see a bear.\n")

if __name__ == "__main__":
    unittest.main()