# Python

import unittest
from unittest.mock import patch
from io import StringIO
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import assignment1 

class TestAdventureGame(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_print_location(self, mock_stdout):
        assignment1.print_message("Molly", "forest")
        self.assertEqual(mock_stdout.getvalue(), "Molly, you are in the forest.\n")

    @patch('builtins.input', return_value="Pat")
    def test_get_player_name(self, mock_input):
        self.assertEqual(assignment1.get_player_name(), "Pat")
    
    @patch('builtins.input', return_value="mall")
    def test_get_initial_choice(self, mock_input):
        self.assertEqual(assignment1.get_initial_choice(), "mall")

if __name__ == "__main__":
    unittest.main()