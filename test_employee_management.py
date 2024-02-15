import unittest
from employees import Employees, EmployeeManagementSystem

class TestEmployeeManagement(unittest.TestCase):
    def test_add_employee(self):
        self.ems = EmployeeManagementSystem()
        initial_count = len(self.ems.employees)
        self.ems.create_employee("Fahad", 25, 540, "IT")
        self.ems.create_employee("Khaled", 28, 541, "CS")
        self.ems.create_employee("Noora", 27, 542, "IS")
        final_count = len(self.ems.employees)
        self.assertEqual(final_count-initial_count,3)

    def test_get_employee(self):
        self.ems = EmployeeManagementSystem()
        self.ems.create_employee("Fahad", 25, 540, "IT")
        self.ems.create_employee("Khaled", 28, 541, "CS")
        self.ems.create_employee("Noora", 27, 542, "IS")
        get_employee1 = self.ems.get_employee(540)
        self.assertIsNotNone(get_employee1)
        self.assertEqual(get_employee1.age, 25)
        self.assertEqual(get_employee1.name, "Fahad")
        self.assertEqual(get_employee1.e_id, 540)
        self.assertEqual(get_employee1.department, "IS")

if __name__ == "__main__":
    unittest.main()
