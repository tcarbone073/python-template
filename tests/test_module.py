import unittest

from tests import MyTestCase


class ExampleTestCase(MyTestCase):
    def test_something(self):
        self.assertTrue(True)


class AnotherExampleTestCase(MyTestCase):
    def test_something(self):
        self.assertFalse(False)
