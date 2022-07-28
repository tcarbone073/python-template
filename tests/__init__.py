import unittest


class MyTestCase(unittest.TestCase):
    def shortDescription(self):
        """Don't show doc string when running tests."""
        return None

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass
