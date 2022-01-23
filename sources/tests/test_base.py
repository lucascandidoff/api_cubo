from sources.application import create_application

import unittest


class TestBase(unittest.TestCase):

    def setUp(self):
        self.application = create_application('testing').test_client()
