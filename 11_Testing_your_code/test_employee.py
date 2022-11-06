import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Test for module employee"""
    
    def setUp(self):
        """Make an employee to use in tests"""
        self.employee_1 = Employee("Domen", "Sernc", 30000)


    def test_give_default_raise(self):
        """Test that a default raise works correctly"""
        self.employee_1.give_raise()
        self.assertEqual(self.employee_1.annualsalary, 35000)


    def test_give_custom_raise(self):
        """Test that a custom raise works correctly"""
        self.employee_1.give_raise(15000)
        self.assertEqual(self.employee_1.annualsalary, 45000)

if __name__ == '__main__':
    unittest.main()