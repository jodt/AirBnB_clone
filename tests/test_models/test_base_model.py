#!/usr/bin/python3
"""
Unittest for "base_model.py"
Execute all tests: python3 -m unittest discover tests
Execute this test: python3 -m unittest tests/test_models/test_base_model.py
"""

from datetime import datetime
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    class that test BaseModel
    """

    def test_data_initialization(self):
        """This fonction tests datat initialization"""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89

        self.assertEqual(my_model.name, "My First Model")
        self.assertEqual(my_model.my_number, 89)

    def test_parameters_passed(self):
        with self.assertRaises(TypeError):
            BaseModel("joel")

    def test_uniq_id(self):
        """This function tests if id is different for all models"""
        my_model1 = BaseModel()
        my_model2 = BaseModel()
        my_model3 = BaseModel()
        my_model4 = BaseModel()
        my_model5 = BaseModel()
        id_list = [my_model1.id, my_model2.id,
                   my_model3.id, my_model4.id, my_model5.id]
        for id in range(len(id_list)-1):
            self.assertNotEqual(id_list[id], id_list[id+1])

    def test_create_at(self):
        """This function test if the return of create_at method
        is a datetime object"""
        my_model8 = BaseModel()
        self.assertIsInstance(my_model8.created_at, datetime)

    def test_update_at(self):
        """This function test if the return of update_at method
        is a datetime object"""
        my_model9 = BaseModel()
        self.assertIsInstance(my_model9.created_at, datetime)

    def test_str(self):
        """This function tests if __str__ method returns a string"""
        my_model6 = BaseModel()
        self.assertIsInstance((my_model6.__str__()), str)

    def test_to_dict(self):
        """This function tests if to_dict method returns dict """
        my_model7 = BaseModel()
        self.assertIsInstance(my_model7.to_dict(), dict)
