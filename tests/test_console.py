#!/usr/bin/python3

"""
Unittest for "console.py"
Execute all tests: python3 -m unittest discover tests
Execute this test: python3 -m unittest tests/test_console.py
"""

import io
import unittest
from console import HBNBCommand
from models.user import User
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
from unittest.mock import patch, Mock
from contextlib import redirect_stdout


class_dict = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}


class TestConsole(unittest.TestCase):
    """
    class that test console
    """

    def setUp(self):
        self.console = HBNBCommand()
        pass

    def tearDown(self):
        pass

    # test prompt

    def test_prompt(self):
        """This function test the prompt format"""
        self.assertEqual(self.console.prompt, "(hbnb) ")

    # test create method

    def test_create(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create")
        output = f.getvalue()
        self.assertEqual(output, "** class name missing **\n")

    # test show method

    def test_show(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("show")
        output = f.getvalue()
        self.assertEqual(output, "** class name missing **\n")

    def test_show_with_false_class(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("show Model")
        output = f.getvalue()
        self.assertEqual(output, "** class doesn't exist **\n")

    def test_show_without_id(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("show User")
        output = f.getvalue()
        self.assertEqual(output, "** instance id missing **\n")

    def test_show_with_incorrect_id(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("show User 1212")
        output = f.getvalue()
        self.assertEqual(output, "** no instance found **\n")

    # test destroy method

    def test_destroy(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("destroy")
        output = f.getvalue()
        self.assertEqual(output, "** class name missing **\n")

    def test_destroy_with_false_class(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("destroy Model")
        output = f.getvalue()
        self.assertEqual(output, "** class doesn't exist **\n")

    def test_destroy_without_id(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("destroy User")
        output = f.getvalue()
        self.assertEqual(output, "** instance id missing **\n")

    def test_destroy_with_incorrect_id(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("destroy User 1212")
        output = f.getvalue()
        self.assertEqual(output, "** no instance found **\n")

    # test destroy method

    def test_all_with_false_class(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("all Model")
        output = f.getvalue()
        self.assertEqual(output, "** class doesn't exist **\n")

    # test update method

    def test_update(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("update")
        output = f.getvalue()
        self.assertEqual(output, "** class name missing **\n")

    def test_update_with_false_class(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("update Model")
        output = f.getvalue()
        self.assertEqual(output, "** class doesn't exist **\n")

    def test_update_without_id(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("update User")
        output = f.getvalue()
        self.assertEqual(output, "** instance id missing **\n")

    def test_update_with_incorrect_id(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("update User 1212")
        output = f.getvalue()
        self.assertEqual(output, "** no instance found **\n")

    # test help command

    def test_help_create(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help create")
        output = f.getvalue()
        self.assertEqual(
            output, "Create command to create an instance of a class\n")

    def test_help_show(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help show")
        output = f.getvalue()
        self.assertEqual(
            output, "Show command to print the string representation \
of an instance based on the class name and id\n")

    def test_help_destroy(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
        output = f.getvalue()
        self.assertEqual(
            output, "Destroy command to delete an instance \
based on the class name and id\n")

    def test_help_all(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help all")
        output = f.getvalue()
        self.assertEqual(output, "All command to print all string \
representation of all instances\n")

    def test_help_count(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help count")
        output = f.getvalue()
        self.assertEqual(output, "Count command to retrieve \
the number of instances of a class\n")

    def test_help_update(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help update")
        output = f.getvalue()
        self.assertEqual(output, "Update command to update an \
instance based on the class name and id by adding or updating attribute\n")
