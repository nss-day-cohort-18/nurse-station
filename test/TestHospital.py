import unittest

import sys; sys.path.append('../')
import src.admintasks
from src.hospital import Hospital


class TestHospital(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.vandy = Hospital("Vanderbilt")
        self.vandy.save()

    def test_hospital_has_name(self):
        self.assertEqual(self.vandy.name, "Vanderbilt")

    def test_hospital_has_id(self):
        self.assertIsNotNone(self.vandy.id)


