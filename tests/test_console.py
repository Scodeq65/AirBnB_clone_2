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

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_missing_class(self, mock_stdout):
        """Test showing an object with missing class name"""
        self.console.onecmd("show")
        self.assertEqual(mock_stdout.getvalue(), "** class name missing **\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_invalid_class(self, mock_stdout):
        """Test showing an object with invalid class name."""
        self.console.onecmd("show InvalidClass")
        self.assertEqual(mock_stdout.getvalue(), "** no instance found **\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_valid(self, mock_stdout):
        """Test showing a valid object"""
        obj = BaseModel()
        obj.save()
        self.console.onecmd(f"show BaseModel {obj.id}")
        expected_output = f"{obj}\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_missing_class(self, mock_stdout):
        """Test destroying an object with missing class name"""
        self.console.onecmd("destroy")
        self.assertEqual(mock_stdout.getvalue(), "** class name missing **\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_invalid_class(self, mock_stdout):
        """Test destroying an object with an invalid class name"""
        self.console.onecmd("destroy InvalidClass")
        self.assertEqual(mock_stdout.getvalue(), "** class doesn't exist **\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_missing_id(self, mock_stdout):
        """Test destroying an object with missing id"""
        self.console.onecmd("destroy BaseModel")
        self.assertEqual(mock_stdout.getvalue(), "** instance id missing **\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_no_instance_found(self, mock_stdout):
        """Test destroying an object that doesn't exist"""
        self.console.onecmd("destroy BaseModel 1234-1234-1234")
        self.assertEqual(mock_stdout.getvalue(), "** no instance found **\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_valid(self, mock_stdout):
        """Test destroying a valid object"""
        obj = BaseModel()
        obj.save()
        self.console.onecmd(f"destroy BaseModel {obj.id}")
        self.assertNotIn(f"BaseModel.{obj.id}", storage.all())

    @patch('sys.stdout', new_callable=StringIO)
    def test_all_invalid_class(self, mock_stdout):
        """Test all with invalid class"""
        self.console.onecmd("all InvalidClass")
        self.assertEqual(mock_stdout.getvalue(), "** class doesn't exist **\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_all_valid_class(self, mock_stdout):
        """Test all with valid class"""
        obj = BaseModel()
        obj.save()
        self.console.onecmd("all BaseModel")
        expected_output = f"[{obj}]\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_all_no_class(self, mock_stdout):
        """Test all with no class"""
        obj1 = BaseModel()
        obj2 = User()
        obj1.save()
        obj2.save()
        self.console.onecmd("all")
        expected_output = f"[{obj1}, {obj2}]\n"
        self.assertIn(f"{obj1}", mock_stdout.getvalue())
        self.assertIn(f"{obj2}", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_missing_class(self, mock_stdout):
        """Test updating an object with missing class name"""
        self.console.onecmd("update")
        self.assertEqual(mock_stdout.getvalue(), "** class name missing **\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_invalid_class(self, mock_stdout):
        """Test updating an object with an invalid class name"""
        self.console.onecmd("update InvalidClass")
        self.assertEqual(mock_stdout.getvalue(), "** class doesn't exist **\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_missing_id(self, mock_stdout):
        """Test updating an object with missing id"""
        self.console.onecmd("update BaseModel")
        self.assertEqual(mock_stdout.getvalue(), "** instance id missing **\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_invalid_id(self, mock_stdout):
        """Test updating an object with invalid id"""
        self.console.onecmd("update BaseModel invalid_id")
        self.assertEqual(mock_stdout.getvalue(), "** no instance found **\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_missing_attribute_name(self, mock_stdout):
        """Test updating an object with missing attribute name"""
        self.console.onecmd("create BaseModel")
        obj_id = list(storage.all().keys())[0]
        self.console.onecmd(f"update BaseModel {obj_id}")
        self.assertEqual(mock_stdout.getvalue(), "** attribute name missing **\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_missing_value(self, mock_stdout):
        """Test updating an object with missing value"""
        self.console.onecmd("create BaseModel")
        obj_id = list(storage.all().keys())[0]
        self.console.onecmd(f"update BaseModel {obj_id} name")
        self.assertEqual(mock_stdout.getvalue(), "** value missing **\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_valid(self, mock_stdout):
        """Test updating an object with valid parameters"""
        self.console.onecmd("create BaseModel")
        obj_id = list(storage.all().keys())[0]
        self.console.onecmd(f"update BaseModel {obj_id} name 'UpdatedName'")
        obj = storage.all()[obj_id]
        self.assertEqual(obj.name, "UpdatedName")


if __name__ == '__main__':
    unittest.main()
