import unittest
import admintasks


class TestPatient(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.gilbert = Patient(name="Gilbert Diaz")
        self.gilbert.save()

        self.meg = Doctor(name="Meg Ducharme")
        self.meg.save()


    def test_patient_has_a_name(self):
        self.assertEqual(self.gilbert.name, "Gilbert Diaz")

    def test_patient_has_ailment(self):
        self.meg.diagnose(patient=self.gilbert, ailment="Chlamydia")

        self.assertIn("Chlamydia", gilbert.ailments)

    def test_assign_patient_to_doctor(self):
        admintasks.assign_patient_to_doctor(self.gilbert.id, self.meg.id)

        self.assertEqual(self.gilbert.current_doctor, self.meg.id)

    def test_admit_patient_to_hospital(self):
        h = Hospital("Vanderbilt")
        h.save()

        self.meg.admit_patient(self.gilbert.id, h.id)

        self.assertIn(self.gilbert.id, h.patients)



















