class Employee:
    """A class to represent an employee"""

    def __init__(self, firstname, lastname, annualsalary):
        """Initialize the Employee."""
        self.firstname = firstname
        self.lastname = lastname
        self.annualsalary = annualsalary

    def give_raise(self, amount=5000):
        """Give an employee a raise"""
        self.annualsalary += amount