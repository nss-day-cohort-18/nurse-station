import unittest

import sys; sys.path.append('../')
import src.admintasks
from src.doctor import Doctor
from src.hospital import Hospital
from src.patient import Patient


class TestDoctor(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.brenda = Patient(name="Brenda Unicorn")
        self.brenda.save()

        self.joe = Doctor(name="Joe Shepherd")
        self.joe.save()

        self.vandy = Hospital("Vanderbilt")
        self.vandy.save()

    def test_doctor_has_name(self):
        self.assertEqual(self.joe.name, "Joe Shepherd")

    def test_doctor_can_admit_patient_to_hospital(self):
        self.joe.admit_patient(self.brenda.id, self.vandy.id)

        self.assertIn(self.brenda.id, self.vandy.patients)
        self.assertEqual(self.brenda.attending_physician, self.joe.id)

    def test_doctor_can_discharge_patient_from_hospital(self):
        self.joe.discharge_patient(self.brenda.id, self.vandy.id)

        self.assertNotIn(self.brenda.id, self.vandy.patients)

    def test_can_register_doctor(self):
        self.assertIsNotNone(self.joe.id)

    def test_doctor_can_diagnose_patient(self):
        self.joe.diagnose_patient(self.brenda.id, "CUFS")
        self.brenda.read_ailments()

        self.assertIn("CUFS", self.brenda.ailments)


















