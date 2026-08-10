# test_autoquery.py
"""
Tests for AutoQuery module.
"""

import unittest
from autoquery import AutoQuery

class TestAutoQuery(unittest.TestCase):
    """Test cases for AutoQuery class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AutoQuery()
        self.assertIsInstance(instance, AutoQuery)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AutoQuery()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
