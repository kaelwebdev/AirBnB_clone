#!/usr/bin/python3
""" BaseModel class unittests file"""
import os
import unittest
import models
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """test class BaseModel"""
    def test_create_model(self):
        """pending"""
        self.bm1 = BaseModel()

    def test_uuid(self):
        """pending"""
        self.assertTrue(hasattr(self.bm1, 'id'))

if __name__ == '__main__':
    unittest.main()
