#!/usr/bin/python3
"""
Unit tests for the console module
"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel


class TestConsole(unittest.TestCase):
    """Unit tests for the HBNB console"""

    def setUp(self):
        """Setup for tests"""
        self.console = HBNBCommand()

    def tearDown(self):
        """Cleanup after tests"""
        storage.reset()

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_missing_class(self, mock_stdout):
        """Test creating an object with missing class name"""
        self.console.onecmd("create")
        self.assertEqual(mock_stdout.getvalue(), "** class name missing **\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_invalid_class(self, mock_stdout):
        """Test creating an object with an invalid class name"""
        self.console.onecmd("create InvalidClass")
        self.assertEqual(mock_stdout.getvalue(), "** class doesn't exist **\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_valid_class(self, mock_stdout):
        """Test creating an object with a valid class name"""
        self.console.onecmd("create BaseModel")
        output = mock_stdout.getvalue().strip()
        self.assertTrue(len(output) > 0)
        self.assertTrue(output in storage.all().keys())

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_with_parameters(self, mock_stdout):
        """Test creating an object with parameters"""
        self.console.onecmd('create BaseModel name="MyModel" number=42')
        output = mock_stdout.getvalue().strip()
        self.assertTrue(len(output) > 0)
        obj_id = "BaseModel." + output
        self.assertIn(obj_id, storage.all())
        obj = storage.all()[obj_id]
        self.assertEqual(obj.name, "MyModel")
        self.assertEqual(obj.number, 42)


if __name__ == '__main__':
    unittest.main()
