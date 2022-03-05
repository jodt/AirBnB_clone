#!/usr/bin/python3

"""
Unittest for "console.py"
Execute all tests: python3 -m unittest discover tests
Execute this test: python3 -m unittest tests/test_console.py
"""

from models.user import User
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from unittest.mock import patch
from models import storage
import io
import unittest
from console import HBNBCommand
import console
import pycodestyle
import shutil
import os


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
    path = "console.py"  # models/state.py
    file = os.path.splitext(path)[0].replace("/", ".")  # file to test

    def test_conformance(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files([self.path])
        self.assertEqual(
            result.total_errors, 0,
            f"Found code style errors (pycodestyle) in file test_console.py"
        )

    def test_documentation(self):
        """test all documentation of module"""
        # module documentation
        self.assertIsNotNone(
            console.__doc__,
            "Missing: module documentation of file \"console.py\"")

        # classes documentation
        for key, value in console.__dict__.items():
            if callable(value):
                self.assertIsNotNone(
                    value.__doc__, f"Missing: class documentation \
of class \"{value.__name__}\"")

        # functions documentation
        for key, value in console.__dict__.items():
            if callable(value):
                for key2, value2 in value.__dict__.items():
                    if callable(value2):
                        self.assertIsNotNone(
                            value2.__doc__, f"Missing: function documentation \
of function \"{value2.__name__}\"")

    def setUp(self):
        try:
            shutil.copyfile("file.json", "tmp_file.json")
            os.remove("file.json")
            open("file.json", "w").close()
            storage._FileStorage__objects = {}
        except Exception:
            pass

    def tearDown(self):
        try:
            shutil.copyfile("tmp_file.json", "file.json")
            os.remove("tmp_file.json")
            storage._FileStorage__objects = {}
        except Exception:
            pass

    # test prompt
    def test_prompt(self):
        console = HBNBCommand()
        """This function test the prompt format"""
        self.assertEqual(console.prompt, "(hbnb) ")

    # test create and .create methods

    def test_create_basemodel(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            id = f.getvalue().strip()
            className = "BaseModel." + id
            self.assertIn(className, storage.all().keys())

    def test_create_basemodel_etc(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel etctectetc")
            id = f.getvalue().strip()
            className = "BaseModel." + id
            self.assertIn(className, storage.all().keys())

    def test_basemodel_create(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.create()")
            id = f.getvalue().strip()
            className = "BaseModel." + id
            self.assertIn(className, storage.all().keys())

    def test_basemodel_create_etc(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.create(etcetcetc)")
            id = f.getvalue().strip()
            className = "BaseModel." + id
            self.assertIn(className, storage.all().keys())

    def test_create_user(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create User")
            id = f.getvalue().strip()
            className = "User." + id
            self.assertIn(className, storage.all().keys())

    def test_create_user_etc(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create User etctectec")
            id = f.getvalue().strip()
            className = "User." + id
            self.assertIn(className, storage.all().keys())

    def test_user_create(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("User.create()")
            id = f.getvalue().strip()
            className = "User." + id
            self.assertIn(className, storage.all().keys())

    def test_user_create_etc(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("User.create(etcetcetc)")
            id = f.getvalue().strip()
            className = "User." + id
            self.assertIn(className, storage.all().keys())

    def test_create_state(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create State")
            id = f.getvalue().strip()
            className = "State." + id
            self.assertIn(className, storage.all().keys())

    def test_create_state_etc(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create State etcetetc")
            id = f.getvalue().strip()
            className = "State." + id
            self.assertIn(className, storage.all().keys())

    def test_state_create(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("State.create()")
            id = f.getvalue().strip()
            className = "State." + id
            self.assertIn(className, storage.all().keys())

    def test_state_create_etc(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("State.create(etcetcetc)")
            id = f.getvalue().strip()
            className = "State." + id
            self.assertIn(className, storage.all().keys())

    def test_create_city(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create City")
            id = f.getvalue().strip()
            className = "City." + id
            self.assertIn(className, storage.all().keys())

    def test_create_city_etc(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create City etcetcetc")
            id = f.getvalue().strip()
            className = "City." + id
            self.assertIn(className, storage.all().keys())

    def test_city_create(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("City.create()")
            id = f.getvalue().strip()
            className = "City." + id
            self.assertIn(className, storage.all().keys())

    def test_city_create_etc(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("City.create(etcetcetc)")
            id = f.getvalue().strip()
            className = "City." + id
            self.assertIn(className, storage.all().keys())

    def test_create_amenity(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            id = f.getvalue().strip()
            className = "Amenity." + id
            self.assertIn(className, storage.all().keys())

    def test_create_amenity_etc(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create Amenity etcetcetc")
            id = f.getvalue().strip()
            className = "Amenity." + id
            self.assertIn(className, storage.all().keys())

    def test_amenity_create(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Amenity.create()")
            id = f.getvalue().strip()
            className = "Amenity." + id
            self.assertIn(className, storage.all().keys())

    def test_amenity_create_etc(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Amenity.create(etcetcetc)")
            id = f.getvalue().strip()
            className = "Amenity." + id
            self.assertIn(className, storage.all().keys())

    def test_create_place(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            id = f.getvalue().strip()
            className = "Place." + id
            self.assertIn(className, storage.all().keys())

    def test_create_place_etc(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create Place etcetcetc")
            id = f.getvalue().strip()
            className = "Place." + id
            self.assertIn(className, storage.all().keys())

    def test_place_create(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Place.create()")
            id = f.getvalue().strip()
            className = "Place." + id
            self.assertIn(className, storage.all().keys())

    def test_place_create_etc(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Place.create(etcetcetc)")
            id = f.getvalue().strip()
            className = "Place." + id
            self.assertIn(className, storage.all().keys())

    def test_create_review(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            id = f.getvalue().strip()
            className = "Review." + id
            self.assertIn(className, storage.all().keys())

    def test_create_review_etc(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create Review etcetcetcetc")
            id = f.getvalue().strip()
            className = "Review." + id
            self.assertIn(className, storage.all().keys())

    def test_review_create(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Review.create()")
            id = f.getvalue().strip()
            className = "Review." + id
            self.assertIn(className, storage.all().keys())

    def test_review_create_etc(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Review.create(etcetcetc)")
            id = f.getvalue().strip()
            className = "Review." + id
            self.assertIn(className, storage.all().keys())

    def test_review_create_etc_space(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Review   .create  (   etcetcetc  )")
            id = f.getvalue().strip()
            className = "Review." + id
            self.assertIn(className, storage.all().keys())

    def test_create_without_class(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create")
        output = f.getvalue()
        self.assertEqual(output, "** class name missing **\n")

    def test_create_with_false_class(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create Model")
        output = f.getvalue()
        self.assertEqual(output, "** class doesn't exist **\n")

    # test show method

    def test_show_basemodel(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            id = f.getvalue().strip()
            className = "BaseModel." + id
            expected = storage._FileStorage__objects[className].__str__()
        with patch('sys.stdout', new=io.StringIO()) as g:
            HBNBCommand().onecmd("show BaseModel {}".format(id))
            output = g.getvalue().strip()
            self.assertEqual(output, expected)

    def test_show_basemodel_etc(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            id = f.getvalue().strip()
            className = "BaseModel." + id
            expected = storage._FileStorage__objects[className].__str__()
        with patch('sys.stdout', new=io.StringIO()) as g:
            HBNBCommand().onecmd("show BaseModel {} etctectec".format(id))
            output = g.getvalue().strip()
            self.assertEqual(output, expected)

    def test_show_user(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create User")
            id = f.getvalue().strip()
            className = "User." + id
            expected = storage._FileStorage__objects[className].__str__()
        with patch('sys.stdout', new=io.StringIO()) as g:
            HBNBCommand().onecmd("show User {}".format(id))
            output = g.getvalue().strip()
            self.assertEqual(output, expected)

    def test_show_user_etc(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create User")
            id = f.getvalue().strip()
            className = "User." + id
            expected = storage._FileStorage__objects[className].__str__()
        with patch('sys.stdout', new=io.StringIO()) as g:
            HBNBCommand().onecmd("show User {} etcetcetc".format(id))
            output = g.getvalue().strip()
            self.assertEqual(output, expected)

    def test_show_state(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create State")
            id = f.getvalue().strip()
            className = "State." + id
            expected = storage._FileStorage__objects[className].__str__()
        with patch('sys.stdout', new=io.StringIO()) as g:
            HBNBCommand().onecmd("show State {}".format(id))
            output = g.getvalue().strip()
            self.assertEqual(output, expected)

    def test_show_state_etc(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create State")
            id = f.getvalue().strip()
            className = "State." + id
            expected = storage._FileStorage__objects[className].__str__()
        with patch('sys.stdout', new=io.StringIO()) as g:
            HBNBCommand().onecmd("show State {} etcetcetc".format(id))
            output = g.getvalue().strip()
            self.assertEqual(output, expected)

    def test_show_city(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create City")
            id = f.getvalue().strip()
            className = "City." + id
            expected = storage._FileStorage__objects[className].__str__()
        with patch('sys.stdout', new=io.StringIO()) as g:
            HBNBCommand().onecmd("show City {}".format(id))
            output = g.getvalue().strip()
            self.assertEqual(output, expected)

    def test_show_city_etc(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create City")
            id = f.getvalue().strip()
            className = "City." + id
            expected = storage._FileStorage__objects[className].__str__()
        with patch('sys.stdout', new=io.StringIO()) as g:
            HBNBCommand().onecmd("show City {} etcetcetc".format(id))
            output = g.getvalue().strip()
            self.assertEqual(output, expected)

    def test_show_amenity(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            id = f.getvalue().strip()
            className = "Amenity." + id
            expected = storage._FileStorage__objects[className].__str__()
        with patch('sys.stdout', new=io.StringIO()) as g:
            HBNBCommand().onecmd("show Amenity {}".format(id))
            output = g.getvalue().strip()
            self.assertEqual(output, expected)

    def test_show_amenity_etc(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            id = f.getvalue().strip()
            className = "Amenity." + id
            expected = storage._FileStorage__objects[className].__str__()
        with patch('sys.stdout', new=io.StringIO()) as g:
            HBNBCommand().onecmd("show Amenity {} etcetcetc".format(id))
            output = g.getvalue().strip()
            self.assertEqual(output, expected)

    def test_show_place(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            id = f.getvalue().strip()
            className = "Place." + id
            expected = storage._FileStorage__objects[className].__str__()
        with patch('sys.stdout', new=io.StringIO()) as g:
            HBNBCommand().onecmd("show Place {}".format(id))
            output = g.getvalue().strip()
            self.assertEqual(output, expected)

    def test_show_place_etc(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            id = f.getvalue().strip()
            className = "Place." + id
            expected = storage._FileStorage__objects[className].__str__()
        with patch('sys.stdout', new=io.StringIO()) as g:
            HBNBCommand().onecmd("show Place {} etcetcetc".format(id))
            output = g.getvalue().strip()
            self.assertEqual(output, expected)

    def test_show_review(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            id = f.getvalue().strip()
            className = "Review." + id
            expected = storage._FileStorage__objects[className].__str__()
        with patch('sys.stdout', new=io.StringIO()) as g:
            HBNBCommand().onecmd("show Review {}".format(id))
            output = g.getvalue().strip()
            self.assertEqual(output, expected)

    def test_show_review_etc(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            id = f.getvalue().strip()
            className = "Review." + id
            expected = storage._FileStorage__objects[className].__str__()
        with patch('sys.stdout', new=io.StringIO()) as g:
            HBNBCommand().onecmd("show Review {} etetete".format(id))
            output = g.getvalue().strip()
            self.assertEqual(output, expected)

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

    # test all method

    def test_all(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create User")
            HBNBCommand().onecmd("create City")
            HBNBCommand().onecmd("create State")
        list_result = []
        for k, v in storage._FileStorage__objects.items():
            list_result.append(v.__str__())
        expected = (str(list_result) + "\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("all")
        output = f.getvalue()
        self.assertEqual(output, expected)

        with patch('sys.stdout', new=io.StringIO()) as g:
            HBNBCommand().onecmd("all User")
        output_user = g.getvalue()
        list_result = []
        for k, v in storage._FileStorage__objects.items():
            if isinstance(storage._FileStorage__objects[k], User):
                list_result.append(v.__str__())
        expected = (str(list_result)+"\n")
        self.assertEqual(output_user, expected)

        with patch('sys.stdout', new=io.StringIO()) as h:
            HBNBCommand().onecmd("all User blablabla")
        output_user = h.getvalue()
        list_result = []
        for k, v in storage._FileStorage__objects.items():
            if isinstance(storage._FileStorage__objects[k], User):
                list_result.append(v.__str__())
        expected = (str(list_result)+"\n")
        self.assertEqual(output_user, expected)

        with patch('sys.stdout', new=io.StringIO()) as i:
            HBNBCommand().onecmd("          all      User")
        output_user = h.getvalue()
        list_result = []
        for k, v in storage._FileStorage__objects.items():
            if isinstance(storage._FileStorage__objects[k], User):
                list_result.append(v.__str__())
        expected = (str(list_result)+"\n")
        self.assertEqual(output_user, expected)

    def test_all_with_false_class(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("all Model")
        output = f.getvalue()
        self.assertEqual(output, "** class doesn't exist **\n")

    def test_user_all(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("user.all")
        output = f.getvalue()
        self.assertEqual(output, "*** Unknow syntax: user.all\n")

    # test update method

    def test_all_update_BaseModel(self):
        dict_class = [
            "BaseModel",
            "User",
            "Amenity",
            "City",
            "Place",
            "Review",
            "State"
        ]
        for key_class in dict_class:
            with patch('sys.stdout', new=io.StringIO()) as f:
                HBNBCommand().onecmd(f"create {key_class}")
            existing_id = f.getvalue().replace("\n", "")
            dict_valid_test = [
                f'{key_class}.update("{existing_id}", \
"attribute_name", "100")',
                f'{key_class}.update("{existing_id}", \
"attribute_name", "100.001")',
                f'{key_class}.update("{existing_id}", \
"attribute_name", "string_value")',
                f'{key_class}.update({existing_id}, \
attribute_name, string_value)',
                f'{key_class}.update("{existing_id}", \
"attribute_name", "composed string value")',
                f'update {key_class} "{existing_id}" \
"attribute_name" "string_value"',
                f'update {key_class} "{existing_id}" \
"attribute_name" "composed string value"',
                f'update {key_class} "{existing_id}" \
"attribute_name" "100"',
                f'update {key_class} "{existing_id}" \
"attribute_name" "100.001"',
                f'update {key_class} {existing_id} \
attribute_name string_value'
            ]
            dict_non_valid_test = [
                f'update {key_class} "not_existing_id" \
"attribute_name" "string_value"',
                f'{key_class}.update("not_existing_id", \
"attribute_name", "string_value")',
            ]
            for key in dict_valid_test:
                with patch('sys.stdout', new=io.StringIO()) as f:
                    HBNBCommand().onecmd(key)
                output = f.getvalue()
                self.assertFalse(output)
            for key in dict_non_valid_test:
                with patch('sys.stdout', new=io.StringIO()) as f:
                    HBNBCommand().onecmd(key)
                output = f.getvalue()
                self.assertEqual(output, "** no instance found **\n")

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

    def test_update_without_attribute(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create User")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f"update User {id}")
            output = f.getvalue()
        self.assertEqual(output, "** attribute name missing **\n")

    def test_update_without_value(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create User")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f"update User {id} 'first_name'")
            output = f.getvalue()
        self.assertEqual(output, "** value missing **\n")

    def test_update_simple_attibute(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create User")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f"update User {id} 'first_name' 'John'")
            output = f.getvalue()
        self.assertFalse(output)

    def test_update_composed_attibute(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create User")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f"update User {id} 'first_name' 'John John'")
            output = f.getvalue()
        self.assertFalse(output)

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
        self.assertTrue(output)

    def test_help_destroy(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
        output = f.getvalue()
        self.assertTrue(output)

    def test_help_all(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help all")
        output = f.getvalue()
        self.assertTrue(output)

    def test_help_count(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help count")
        output = f.getvalue()
        self.assertTrue(output)

    def test_help_update(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help update")
        output = f.getvalue()
        self.assertTrue(output)

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

    def test_destroy_user_instance(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create User")
        key = "User"+"."+f.getvalue().strip('\n')
        self.assertIn(key, storage._FileStorage__objects)
        HBNBCommand().onecmd("destroy User {}".format(f.getvalue()))
        self.assertNotIn(key, storage._FileStorage__objects)
